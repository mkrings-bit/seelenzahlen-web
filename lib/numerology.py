"""Numerologie-Berechnungen nach Maxim Mankevichs Soul-Codes-System.

Eingabe: Geburtsdatum als (Tag, Monat, Jahr).
Ausgabe: Dictionary mit allen relevanten Zahlen plus den Reduktionspfaden,
damit das PDF die Berechnungsschritte sauber darstellen kann.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import List, Tuple, Optional


KARMA_ZAHLEN = {13, 14, 16, 17, 19}      # Klassische Karma-Zahlen
MEISTER_ZAHLEN = {11, 22, 33}            # Meisterzahlen
SPECIAL_ZAHLEN = {10, 28, 37}            # Eigenständige Energien jenseits Karma/Meister


def digit_sum(n: int) -> int:
    """Quersumme einer nicht-negativen Zahl."""
    return sum(int(c) for c in str(n))


def reduce_path(n: int, keep_master: bool = False) -> List[int]:
    """Reduziert eine Zahl auf 1-9 und gibt den ganzen Pfad zurück.

    Beispiel: 37 -> [37, 10, 1]
    Wenn keep_master=True, hält Reduktion bei 11/22/33 an.
    """
    path = [n]
    while path[-1] > 9:
        if keep_master and path[-1] in MEISTER_ZAHLEN:
            break
        path.append(digit_sum(path[-1]))
    return path


def reduce(n: int, keep_master: bool = False) -> int:
    """Reduziert n auf eine einstellige Zahl (oder Meisterzahl, falls keep_master)."""
    return reduce_path(n, keep_master)[-1]


def find_special_in_path(path: List[int]) -> List[int]:
    """Liefert alle Karma-/Meister-/Special-Zahlen, die auf dem Reduktionspfad auftauchen."""
    interesting = KARMA_ZAHLEN | MEISTER_ZAHLEN | SPECIAL_ZAHLEN
    return [n for n in path if n in interesting]


def all_digits_of_date(day: int, month: int, year: int) -> List[int]:
    """Alle einzelnen Ziffern des Datums (mit Nullen für einstellige Werte)."""
    s = f"{day:02d}{month:02d}{year:04d}"
    return [int(c) for c in s]


def format_calc(digits: List[int], total: int) -> str:
    """Hübsche Darstellung wie '0+6+1+0+2+0+0+1 = 10'."""
    return "+".join(str(d) for d in digits) + f" = {total}"


def format_reduce_chain(path: List[int]) -> str:
    """Stellt den Reduktionspfad als '37 → 10 → 1' dar (ohne Doppelung des Starts)."""
    if len(path) <= 1:
        return str(path[0])
    return " → ".join(str(p) for p in path)


@dataclass
class CycleInfo:
    """Ein einzelner Lebenszyklus."""
    label: str        # "1. Zyklus"
    quelle: str       # "Monat" / "Tag" / "Jahr"
    zahl: int         # Endgültige (reduzierte) Zahl
    zahl_pfad: List[int]  # Berechnungspfad
    alter_von: int
    alter_bis: Optional[int]  # None = "+"
    thema: str        # Kurztext


@dataclass
class NumerologyReading:
    """Das vollständige Ergebnis einer Berechnung."""
    day: int
    month: int
    year: int
    name: Optional[str] = None

    # Hauptzahlen (immer als finale 1-9)
    lebenszahl: int = 0
    seelenzahl: int = 0       # = Tageszahl reduziert
    persoenlichkeit: int = 0  # = Monatszahl reduziert
    ausdruckszahl: int = 0    # = Jahreszahl reduziert
    wachstumszahl: int = 0    # Tag + Monat, reduziert
    realisationszahl: int = 0  # Lebenszahl + Ausdruck, reduziert
    tageszahl_unreduziert: int = 0  # Tag als 1- oder 2-stellige Zahl
    persoenliches_jahr: int = 0     # Persönliches Jahr für aktuelles Kalenderjahr
    persoenliches_jahr_jahr: int = 0  # Welches Kalenderjahr

    # Reduktionspfade für Anzeige
    lebenszahl_pfad: List[int] = field(default_factory=list)
    ausdruckszahl_pfad: List[int] = field(default_factory=list)
    wachstumszahl_pfad: List[int] = field(default_factory=list)
    persoenliches_jahr_pfad: List[int] = field(default_factory=list)
    tageszahl_pfad: List[int] = field(default_factory=list)
    monatszahl_pfad: List[int] = field(default_factory=list)

    # Karma- bzw. Special-Aspekte
    karma_aspekte: List[int] = field(default_factory=list)

    # Lebenszyklen
    zyklen: List[CycleInfo] = field(default_factory=list)

    # Rohdaten der Berechnungstabelle als Strings
    lebenszahl_calc: str = ""
    seelenzahl_calc: str = ""
    persoenlichkeit_calc: str = ""
    ausdruckszahl_calc: str = ""
    wachstumszahl_calc: str = ""
    realisationszahl_calc: str = ""
    persoenliches_jahr_calc: str = ""


def compute(day: int, month: int, year: int, name: Optional[str] = None,
            year_for_personal: Optional[int] = None) -> NumerologyReading:
    """Berechnet alle Zahlen für ein Geburtsdatum."""
    r = NumerologyReading(day=day, month=month, year=year, name=name)

    # ----- Lebenszahl -----
    digits = all_digits_of_date(day, month, year)
    total = sum(digits)
    r.lebenszahl_pfad = reduce_path(total)
    r.lebenszahl = r.lebenszahl_pfad[-1]
    r.lebenszahl_calc = (
        format_calc(digits, total) + " → " + format_reduce_chain(r.lebenszahl_pfad)
    )

    # ----- Tages-/Seelenzahl -----
    r.tageszahl_unreduziert = day
    r.tageszahl_pfad = reduce_path(day)
    r.seelenzahl = r.tageszahl_pfad[-1]
    if day < 10:
        r.seelenzahl_calc = f"0+{day}"
    elif day == digit_sum(day):
        r.seelenzahl_calc = str(day)
    else:
        d_digits = [int(c) for c in f"{day:02d}"]
        r.seelenzahl_calc = "+".join(str(d) for d in d_digits)

    # ----- Persönlichkeit aus Monat -----
    r.monatszahl_pfad = reduce_path(month)
    r.persoenlichkeit = r.monatszahl_pfad[-1]
    m_digits = [int(c) for c in f"{month:02d}"]
    r.persoenlichkeit_calc = "+".join(str(d) for d in m_digits) if month >= 10 else str(month)

    # ----- Ausdruck aus Jahr -----
    y_digits = [int(c) for c in f"{year:04d}"]
    y_sum = sum(y_digits)
    r.ausdruckszahl_pfad = reduce_path(y_sum)
    r.ausdruckszahl = r.ausdruckszahl_pfad[-1]
    chain = format_reduce_chain([y_sum] + r.ausdruckszahl_pfad[1:]) if len(r.ausdruckszahl_pfad) > 1 else str(r.ausdruckszahl)
    r.ausdruckszahl_calc = "+".join(str(d) for d in y_digits) + (
        f" = {y_sum} → " + " → ".join(str(p) for p in r.ausdruckszahl_pfad[1:])
        if y_sum > 9 else ""
    )

    # ----- Wachstumszahl: Tag + Monat -----
    wach_total = day + month
    r.wachstumszahl_pfad = reduce_path(wach_total)
    r.wachstumszahl = r.wachstumszahl_pfad[-1]
    r.wachstumszahl_calc = f"{day} + {month} = {wach_total}"
    if wach_total > 9:
        r.wachstumszahl_calc += " → " + " → ".join(str(p) for p in r.wachstumszahl_pfad[1:])

    # ----- Realisationszahl: Lebenszahl + Ausdruck -----
    real_total = r.lebenszahl + r.ausdruckszahl
    real_pfad = reduce_path(real_total)
    r.realisationszahl = real_pfad[-1]
    if real_total > 9:
        r.realisationszahl_calc = (
            f"{r.lebenszahl} + {r.ausdruckszahl} = {real_total} → " +
            " → ".join(str(p) for p in real_pfad[1:])
        )
    else:
        r.realisationszahl_calc = f"{r.lebenszahl} + {r.ausdruckszahl} = {real_total}"

    # ----- Persönliches Jahr -----
    pj_year = year_for_personal or date.today().year
    r.persoenliches_jahr_jahr = pj_year
    pj_digits = ([int(c) for c in f"{day:02d}"] +
                 [int(c) for c in f"{month:02d}"] +
                 [int(c) for c in f"{pj_year:04d}"])
    pj_total = sum(pj_digits)
    r.persoenliches_jahr_pfad = reduce_path(pj_total)
    r.persoenliches_jahr = r.persoenliches_jahr_pfad[-1]
    r.persoenliches_jahr_calc = (
        "+".join(str(d) for d in pj_digits) + f" = {pj_total}"
        + (" → " + " → ".join(str(p) for p in r.persoenliches_jahr_pfad[1:])
           if pj_total > 9 else "")
    )

    # ----- Karma-/Special-Aspekte: alles Karma/Meister/Special, das auf einem Pfad auftaucht -----
    aspekte = set()
    for pfad in (r.lebenszahl_pfad, r.ausdruckszahl_pfad, r.wachstumszahl_pfad,
                 r.persoenliches_jahr_pfad, r.tageszahl_pfad, r.monatszahl_pfad,
                 real_pfad):
        for n in pfad:
            if n in KARMA_ZAHLEN or n in MEISTER_ZAHLEN or n in SPECIAL_ZAHLEN:
                aspekte.add(n)
    r.karma_aspekte = sorted(aspekte)

    # ----- Lebenszyklen -----
    # 1. Zyklus: aus Geburtsmonat reduziert, 0-28
    # 2. Zyklus: aus Geburtstag reduziert, 28-56
    # 3. Zyklus: aus Geburtsjahr reduziert, 56+
    zyklen_themen = {
        1: "Den eigenen Weg finden, Eigenständigkeit, erste Spuren legen",
        2: "Partnerschaft, Sensibilität, Geduld, in echter Augenhöhe wachsen",
        3: "Ausdruck, Kreativität, Sichtbarkeit, soziale Sprache finden",
        4: "Disziplin, Struktur, Boden, etwas Solides bauen",
        5: "Erfahrung sammeln, Wandel, Welt erkunden, Identität durch Wechsel finden",
        6: "Familie, Beziehung, Verantwortung, Schönheit erschaffen",
        7: "Innenarbeit, Studium, Tiefe, eigene Wahrheit finden",
        8: "Manifestation, Macht, materieller Aufbau, Verantwortung tragen",
        9: "Vollendung, Lehrer-Rolle, Mission, das wirklich Eigene bauen",
    }

    r.zyklen = [
        CycleInfo("1. Zyklus", "Monat", r.persoenlichkeit, r.monatszahl_pfad,
                  0, 28, zyklen_themen.get(r.persoenlichkeit, "")),
        CycleInfo("2. Zyklus", "Tag", r.seelenzahl, r.tageszahl_pfad,
                  28, 56, zyklen_themen.get(r.seelenzahl, "")),
        CycleInfo("3. Zyklus", "Jahr", r.ausdruckszahl, r.ausdruckszahl_pfad,
                  56, None, zyklen_themen.get(r.ausdruckszahl, "")),
    ]

    return r


def parse_date_string(s: str) -> Tuple[int, int, int]:
    """Akzeptiert 'DD.MM.YYYY', 'D.M.YYYY' und liefert (day, month, year)."""
    s = s.strip()
    parts = s.replace("-", ".").replace("/", ".").split(".")
    if len(parts) != 3:
        raise ValueError(f"Datum '{s}' nicht im Format DD.MM.YYYY")
    d, m, y = int(parts[0]), int(parts[1]), int(parts[2])
    if y < 100:
        # zweistelliges Jahr: 00-30 = 2000er, 31-99 = 1900er (pragmatisch)
        y = 2000 + y if y <= 30 else 1900 + y
    if not (1 <= d <= 31 and 1 <= m <= 12 and 1900 <= y <= 2100):
        raise ValueError(f"Datum {s} außerhalb plausibler Grenzen.")
    return d, m, y


if __name__ == "__main__":
    # Schnelltest
    for ds in ["18.05.2001", "06.10.2001", "06.12.1999"]:
        d, m, y = parse_date_string(ds)
        r = compute(d, m, y, year_for_personal=2026)
        print(f"--- {ds} ---")
        print(f"Lebenszahl: {r.lebenszahl} ({r.lebenszahl_calc})")
        print(f"Seelenzahl: {r.seelenzahl} ({r.seelenzahl_calc})")
        print(f"Persönlichkeit: {r.persoenlichkeit}")
        print(f"Ausdruck: {r.ausdruckszahl} ({r.ausdruckszahl_calc})")
        print(f"Wachstum: {r.wachstumszahl} ({r.wachstumszahl_calc})")
        print(f"Realisation: {r.realisationszahl} ({r.realisationszahl_calc})")
        print(f"Karma-Aspekte: {r.karma_aspekte}")
        print(f"Pers. Jahr 2026: {r.persoenliches_jahr} ({r.persoenliches_jahr_calc})")
        print()
