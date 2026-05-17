"""Seelenzahlen Deep-Dive — Flask-Webseite.

Lokales Starten:
    pip install -r requirements.txt
    python app.py

Production (Railway/Render):
    gunicorn app:app
"""
import os
import re
import time
from collections import deque
from datetime import datetime

from flask import (
    Flask, render_template, request, send_file, jsonify, abort, make_response
)

from lib.pdf_builder import generate_pdf_bytes, suggested_filename
from lib import numerology as nm


app = Flask(__name__, static_folder="static", template_folder="templates")

# Maximale Anfrage-Größe begrenzen (Schutz vor Missbrauch)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024  # 64 KB reicht für ein Formular dicke

# Einfaches In-Memory-Rate-Limiting (IP → Liste von Zeitstempeln)
_REQ_LOG: dict[str, deque] = {}
_RATE_LIMIT = 10        # Anfragen pro Fenster
_RATE_WINDOW = 60 * 5   # Fenster in Sekunden (5 Minuten)


def _client_ip() -> str:
    """Liefert die Client-IP, auch hinter Reverse-Proxies (Railway/Render setzen X-Forwarded-For)."""
    forwarded = request.headers.get("X-Forwarded-For", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.remote_addr or "unknown"


def _rate_limit_ok(ip: str) -> bool:
    now = time.time()
    dq = _REQ_LOG.setdefault(ip, deque())
    # Alte Einträge wegräumen
    while dq and dq[0] < now - _RATE_WINDOW:
        dq.popleft()
    if len(dq) >= _RATE_LIMIT:
        return False
    dq.append(now)
    return True


# Akzeptiere DD.MM.YYYY, DD-MM-YYYY, DD/MM/YYYY, auch HTML5-date 'YYYY-MM-DD'
_DATE_RE_DMY = re.compile(r"^\s*(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{4})\s*$")
_DATE_RE_YMD = re.compile(r"^\s*(\d{4})-(\d{1,2})-(\d{1,2})\s*$")
_NAME_RE = re.compile(r"^[\wÄÖÜäöüß\s\-'\.]{1,80}$", re.UNICODE)


def _normalize_date(s: str) -> str:
    """Bringe Datum in DD.MM.YYYY-Form. Wirft ValueError bei ungültigem Format."""
    s = s.strip()
    m = _DATE_RE_DMY.match(s)
    if m:
        d, mo, y = m.groups()
        return f"{int(d):02d}.{int(mo):02d}.{int(y):04d}"
    m = _DATE_RE_YMD.match(s)
    if m:
        y, mo, d = m.groups()
        return f"{int(d):02d}.{int(mo):02d}.{int(y):04d}"
    raise ValueError("Datum muss im Format TT.MM.JJJJ angegeben werden.")


def _validate_date_makes_sense(date_norm: str) -> None:
    """Plausibilitätscheck: Datum wirklich gültiges Datum, Jahr 1900-aktuell."""
    try:
        dt = datetime.strptime(date_norm, "%d.%m.%Y")
    except ValueError:
        raise ValueError("Das Datum existiert nicht (z.B. 30.02.).")
    if dt.year < 1900 or dt.year > datetime.now().year:
        raise ValueError("Bitte ein Geburtsdatum zwischen 1900 und heute angeben.")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/healthz")
def healthz():
    """Health-Check für Deployment-Plattformen."""
    return {"status": "ok"}, 200


@app.route("/generate", methods=["POST"])
def generate():
    ip = _client_ip()
    if not _rate_limit_ok(ip):
        return _error_response(
            "Du hast in letzter Zeit ein paar Anfragen geschickt. Warte ein paar Minuten und versuch es erneut.",
            429,
        )

    name = (request.form.get("name") or "").strip()
    date_raw = (request.form.get("date") or "").strip()

    # Name validieren (optional, aber wenn da, muss er sauber sein)
    if name:
        if not _NAME_RE.match(name):
            return _error_response(
                "Der Name enthält ungültige Zeichen. Buchstaben, Leerzeichen, Bindestriche und Punkte sind erlaubt.",
                400,
            )

    # Datum validieren
    try:
        date_norm = _normalize_date(date_raw)
        _validate_date_makes_sense(date_norm)
    except ValueError as e:
        return _error_response(str(e), 400)

    # PDF erzeugen
    try:
        pdf_buffer = generate_pdf_bytes(date_norm, name=name or None)
    except Exception as e:
        app.logger.exception("PDF-Generierung fehlgeschlagen")
        return _error_response(
            "Beim Erstellen des PDFs ist etwas schiefgegangen. Bitte versuch es noch einmal.",
            500,
        )

    filename = suggested_filename(date_norm, name or None)
    response = make_response(send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=filename,
    ))
    # Kein Caching — jedes PDF ist personalisiert
    response.headers["Cache-Control"] = "no-store, max-age=0"
    return response


def _error_response(message: str, status: int):
    """Wenn der Request per fetch() von der Webseite kam, liefere JSON; sonst HTML."""
    accept = request.headers.get("Accept", "")
    if "application/json" in accept or request.is_json or request.headers.get("X-Requested-With") == "fetch":
        return jsonify({"error": message}), status
    # Fallback: kleine HTML-Fehlerseite
    return render_template("index.html", error=message), status


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
