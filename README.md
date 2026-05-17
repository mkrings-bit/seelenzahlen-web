# Seelenzahlen Deep-Dive — Webseite

Eine Flask-Webseite, auf der Besucher:innen ihr Geburtsdatum eingeben und sofort ihren persönlichen Seelenzahlen Deep-Dive als 14-seitiges PDF herunterladen können.

Basierend auf Maxim Mankevichs Soul-Codes-System.

---

## Projektstruktur

```
seelenzahlen-web/
├── app.py                 # Flask-App (Routen, Validierung, Rate-Limit)
├── lib/
│   ├── numerology.py      # Berechnung aller Zahlen aus einem Datum
│   ├── content.py         # Content-Bibliothek (Texte zu jeder Zahl)
│   └── pdf_builder.py     # PDF-Generierung (ReportLab) in-memory
├── templates/
│   └── index.html         # Landingpage mit Formular
├── static/
│   └── style.css          # Styling (Gold, Cormorant Garamond, Inter)
├── requirements.txt       # Flask, gunicorn, reportlab
├── Procfile               # Für Railway/Render/Heroku
├── runtime.txt            # Python-Version
└── README.md
```

---

## Lokal starten

Voraussetzung: Python 3.11+ installiert.

```bash
# 1. In das Projekt-Verzeichnis wechseln
cd seelenzahlen-web

# 2. Virtuelle Umgebung anlegen (empfohlen)
python3 -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\activate            # Windows

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. Server starten
python app.py
```

Dann im Browser öffnen: <http://localhost:5000>

---

## Online deployen

Drei einfache Optionen — alle haben einen kostenlosen Tier, der für den Start mehr als reicht.

### Option A: Railway (empfohlen, am einfachsten)

1. Konto anlegen auf <https://railway.app>.
2. Projekt-Ordner als Git-Repo initialisieren und auf GitHub pushen:

   ```bash
   cd seelenzahlen-web
   git init
   git add .
   git commit -m "Erster Push"
   gh repo create seelenzahlen-web --public --source=. --push
   # Oder manuell ein Repo auf github.com anlegen und pushen.
   ```

3. In Railway „New Project" → „Deploy from GitHub repo" → das Repo auswählen.
4. Railway erkennt automatisch Python, installiert `requirements.txt`, startet `Procfile`.
5. Nach ein paar Minuten gibt Railway dir eine URL wie `seelenzahlen-web-production.up.railway.app`.
6. Optional: eigene Domain in Railway-Settings → „Domains" → „Custom domain" hinzufügen.

### Option B: Render

1. Konto auf <https://render.com> anlegen.
2. Auf GitHub pushen wie oben.
3. In Render: „New +" → „Web Service" → GitHub-Repo auswählen.
4. Einstellungen:
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free reicht für den Anfang
5. „Create Web Service" → fertig.

### Option C: Fly.io

```bash
# Fly-CLI installieren: https://fly.io/docs/hands-on/install-flyctl/
fly launch              # Folge dem Wizard, wähle Region "fra" für Europa
fly deploy
```

Eine eigene Domain via `fly certs add deinedomain.de` einbinden.

---

## Wie der User-Flow läuft

1. Besucher:in landet auf der Startseite, sieht Hero mit Erklärung und Formular.
2. Gibt Vornamen (optional) und Geburtsdatum (TT.MM.JJJJ) ein.
3. Klickt „Meinen Deep-Dive erstellen".
4. JavaScript schickt einen `POST /generate`-Request, Server validiert + erzeugt PDF in-memory.
5. PDF kommt als Blob zurück, JavaScript startet den Download.
6. Datei landet im Downloads-Ordner als `Seelenzahlen_TT-MM-JJJJ_Name_Deep-Dive.pdf`.

Wenn JavaScript deaktiviert ist, funktioniert das Formular auch ohne — das Browser-Standardverhalten lädt das PDF direkt herunter.

---

## Sicherheits- und Anti-Missbrauchs-Maßnahmen

Eingebaut:
- **Rate-Limiting:** maximal 10 Anfragen pro IP in 5 Minuten (siehe `app.py` → `_RATE_LIMIT`).
- **Eingabe-Validierung:** Datum wird strikt geparst, unmögliche Daten (30.02.) abgelehnt. Name nur mit Buchstaben + Sonderzeichen.
- **MAX_CONTENT_LENGTH:** Formulargrößen über 64 KB werden abgelehnt.
- **Keine Persistenz:** Datum + Name werden nicht gespeichert (kein DB, keine Logfiles).

Wenn du mehr brauchst (z.B. weil die Seite viral geht):
- Cloudflare davorschalten (kostenlos, schützt automatisch vor Bots).
- Rate-Limit-Werte in `app.py` anpassen.

---

## Branding anpassen

Will man die Seite an ein eigenes Branding anpassen, sind hier die Stellen:

| Was | Datei | Stelle |
|---|---|---|
| Seitenname „Seelenzahlen" | `templates/index.html` | `<title>`, `.brand-name` |
| Hauptfarbe Gold | `static/style.css` | `:root { --gold: ...; --gold-light: ...; }` |
| Hero-Titel | `templates/index.html` | `<h1 class="hero-title">` |
| Texte unter „Was im PDF steht" | `templates/index.html` | `.content-grid` |
| PDF-Footer-Branding | `lib/pdf_builder.py` | `make_chrome()` Funktion |
| Disclaimer im PDF | `lib/pdf_builder.py` | letzter Absatz in `build_story()` |

---

## Tests

```bash
# CLI-Test (PDF direkt aus dem Modul)
python -m lib.pdf_builder "06.10.2001" --name "Test User" --out /tmp/test.pdf

# Lokalen Server testen
python app.py &
curl -X POST http://localhost:5000/generate \
  -F "name=Test User" \
  -F "date=06.10.2001" \
  --output /tmp/test.pdf
```

---

## Lizenz / Hinweise

Die Numerologie-Deutungen orientieren sich an Maxim Mankevichs Soul-Codes-System. Sie sind keine wissenschaftliche Aussage und kein Ersatz für professionelle Beratung.

Der Code in diesem Repository darf frei verwendet und angepasst werden.
