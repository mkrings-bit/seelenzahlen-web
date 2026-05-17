#!/usr/bin/env python3
"""Seelenzahlen Deep-Dive PDF Generator.

Usage:
    python3 build_pdf.py "DD.MM.YYYY" [--name "Name"] [--out path.pdf] [--year 2026]

Liest ein Geburtsdatum, berechnet alle relevanten Zahlen über das numerology-Modul
und kombiniert sie mit der Content-Bibliothek zu einem 14-seitigen PDF im Stil
von Maxim Mankevichs Soul-Codes-System.
"""
from __future__ import annotations
import argparse
import io
import os
import sys
from datetime import date

# Imports aus dem eigenen lib-Verzeichnis (Package-Modus)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable,
)

# Beide Import-Stile unterstützen: als Package (lib.numerology) und als direkter Aufruf
try:
    from . import numerology as nm
    from . import content as co
except ImportError:
    import numerology as nm
    import content as co

# ---------- Farben ----------
GOLD = colors.HexColor("#c9a44a")
GOLD_LIGHT = colors.HexColor("#f6efdc")
DARK = colors.HexColor("#0e1a2b")
BODY = colors.HexColor("#1f2530")
MUTED = colors.HexColor("#7a7a7a")
RULE = colors.HexColor("#e0e0e0")
GOLD_DEEP = colors.HexColor("#b8893a")

# ---------- Seitenrahmen ----------
PAGE_W, PAGE_H = A4
MARGIN_L, MARGIN_R = 22*mm, 20*mm
MARGIN_T, MARGIN_B = 22*mm, 22*mm

# ---------- Styles ----------
def make_style(name, **kwargs):
    base = ParagraphStyle(
        name=name, fontName='Helvetica', fontSize=10, leading=14,
        textColor=BODY, spaceBefore=0, spaceAfter=6,
    )
    for k, v in kwargs.items():
        setattr(base, k, v)
    return base

H1 = make_style('H1', fontName='Helvetica-Bold', fontSize=30, leading=34, textColor=DARK, spaceAfter=4)
H1_SUB = make_style('H1Sub', fontSize=11, textColor=MUTED, spaceAfter=10)
H2 = make_style('H2', fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=DARK, spaceBefore=0, spaceAfter=2)
H2_SUB = make_style('H2Sub', fontSize=11, leading=14, textColor=GOLD_DEEP, fontName='Helvetica-Oblique', spaceAfter=12)
H3 = make_style('H3', fontName='Helvetica-Bold', fontSize=12.5, leading=15, textColor=DARK, spaceBefore=12, spaceAfter=4)
H4 = make_style('H4', fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=GOLD_DEEP, spaceBefore=10, spaceAfter=2)
BODYP = make_style('Body', fontSize=10.5, leading=15, alignment=TA_JUSTIFY, spaceAfter=7)
BODYP_TIGHT = make_style('BodyTight', fontSize=10.5, leading=14, alignment=TA_JUSTIFY, spaceAfter=4)
BULLET = make_style('Bullet', fontSize=10.5, leading=14, leftIndent=14, bulletIndent=4, spaceAfter=3, alignment=TA_LEFT)
QUOTE = make_style('Quote', fontSize=10.5, leading=15, fontName='Helvetica-Oblique', leftIndent=10, rightIndent=10, spaceBefore=8, spaceAfter=8, textColor=colors.HexColor("#2a2a2a"))
SMALL = make_style('Small', fontSize=9, leading=12, textColor=MUTED, fontName='Helvetica-Oblique', spaceAfter=4)
DISC = make_style('Disc', fontSize=8.5, leading=11, textColor=MUTED, fontName='Helvetica-Oblique', spaceAfter=2)
HERO_NUM = make_style('HeroNum', fontName='Helvetica-Bold', fontSize=72, leading=78, textColor=GOLD, alignment=TA_CENTER, spaceAfter=2)
HERO_LABEL = make_style('HeroLabel', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=DARK, alignment=TA_CENTER, spaceAfter=2)
HERO_TAG = make_style('HeroTag', fontSize=10, leading=12, textColor=MUTED, alignment=TA_CENTER, spaceAfter=0)
WARN_BODY = make_style('Warn', fontSize=10, leading=13, alignment=TA_JUSTIFY, spaceAfter=4)


# ---------- UI-Bausteine ----------
def bullet_list(items):
    return [Paragraph(f"&bull; &nbsp;{txt}", BULLET) for txt in items]


def number_intro(num, text):
    box_style = ParagraphStyle('Box', fontName='Helvetica-Bold', fontSize=42, textColor=GOLD, alignment=TA_CENTER, leading=42)
    box = Paragraph(str(num), box_style)
    txt = Paragraph(text, BODYP_TIGHT)
    t = Table([[box, txt]], colWidths=[26*mm, None], rowHeights=[26*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), GOLD_LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('VALIGN', (1,0), (1,0), 'TOP'),
        ('LEFTPADDING', (1,0), (1,0), 10),
        ('TOPPADDING', (1,0), (1,0), 2),
        ('BOTTOMPADDING', (1,0), (1,0), 2),
        ('RIGHTPADDING', (1,0), (1,0), 0),
    ]))
    return t


def hero_box(num, label, tagline):
    inner = Table(
        [[Paragraph(str(num), HERO_NUM)],
         [Paragraph(label, HERO_LABEL)],
         [Paragraph(tagline, HERO_TAG)]],
        colWidths=[None],
    )
    inner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD_LIGHT),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (0,0), 16),
        ('BOTTOMPADDING', (0,0), (0,0), 0),
        ('TOPPADDING', (0,1), (0,1), 0),
        ('BOTTOMPADDING', (0,1), (0,1), 0),
        ('TOPPADDING', (0,2), (0,2), 0),
        ('BOTTOMPADDING', (0,2), (0,2), 16),
    ]))
    return inner


def calc_table(rows):
    data = [["Zahl", "Bedeutung", "Berechnung", "Ergebnis"]] + rows
    t = Table(data, colWidths=[34*mm, 44*mm, 60*mm, 22*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 9.5),
        ('FONT', (0,1), (-1,-1), 'Helvetica', 9.5),
        ('TEXTCOLOR', (3,1), (3,-1), GOLD_DEEP),
        ('FONT', (3,1), (3,-1), 'Helvetica-Bold', 10),
        ('ALIGN', (3,0), (3,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LINEBELOW', (0,1), (-1,-1), 0.4, RULE),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#fafafa')]),
    ]))
    return t


def compat_table(rows):
    data = [["Zahl", "Beziehung", "Effekt"]] + rows
    t = Table(data, colWidths=[14*mm, 32*mm, None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 9.5),
        ('FONT', (0,1), (-1,-1), 'Helvetica', 9.5),
        ('FONT', (0,1), (0,-1), 'Helvetica-Bold', 10),
        ('TEXTCOLOR', (0,1), (0,-1), GOLD_DEEP),
        ('FONT', (1,1), (1,-1), 'Helvetica-Bold', 9.5),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LINEBELOW', (0,1), (-1,-1), 0.4, RULE),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t


def cycle_table(rows):
    data = [["Zyklus", "Zahl", "Etwa Alter", "Thema"]] + rows
    t = Table(data, colWidths=[26*mm, 28*mm, 24*mm, None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 9.5),
        ('FONT', (0,1), (-1,-1), 'Helvetica', 9.5),
        ('FONT', (1,1), (1,-1), 'Helvetica-Bold', 10),
        ('TEXTCOLOR', (1,1), (1,-1), GOLD_DEEP),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LINEBELOW', (0,1), (-1,-1), 0.4, RULE),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t


def toc_table(items):
    data = [[str(num), title, page] for num, title, page in items]
    t = Table(data, colWidths=[8*mm, None, 16*mm])
    t.setStyle(TableStyle([
        ('FONT', (0,0), (0,-1), 'Helvetica-Bold', 10.5),
        ('TEXTCOLOR', (0,0), (0,-1), GOLD_DEEP),
        ('FONT', (1,0), (1,-1), 'Helvetica', 10.5),
        ('FONT', (2,0), (2,-1), 'Helvetica', 10.5),
        ('TEXTCOLOR', (2,0), (2,-1), MUTED),
        ('ALIGN', (2,0), (2,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor("#cccccc")),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    return t


def quote_box(text):
    p = Paragraph(text, QUOTE)
    t = Table([[p]], colWidths=[None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD_LIGHT),
        ('LINEBEFORE', (0,0), (0,-1), 2.5, GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    return t


def warning_box(text):
    p = Paragraph(text, WARN_BODY)
    t = Table([[p]], colWidths=[None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fdf5e8")),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 9),
    ]))
    return t


# ---------- Page Chrome ----------
def make_chrome(footer_text: str):
    def draw_page_chrome(canv, doc):
        canv.saveState()
        canv.setStrokeColor(GOLD)
        canv.setLineWidth(1.5)
        canv.line(MARGIN_L, PAGE_H - MARGIN_T + 8*mm,
                  PAGE_W - MARGIN_R, PAGE_H - MARGIN_T + 8*mm)
        canv.setFillColor(MUTED)
        canv.setFont('Helvetica', 9)
        canv.drawString(MARGIN_L, MARGIN_B - 12, footer_text)
        canv.drawRightString(PAGE_W - MARGIN_R, MARGIN_B - 12,
                             f"Seite {canv.getPageNumber()}")
        canv.restoreState()
    return draw_page_chrome


# ---------- Story-Builder ----------
def build_story(r: nm.NumerologyReading) -> list:
    story = []

    # Cover-Bezeichnung
    date_str = f"{r.day:02d}.{r.month:02d}.{r.year:04d}"
    if r.name:
        deck_subtitle = f"Deep-Dive  ·  {r.name}  ·  Geburtsdatum {date_str}"
    else:
        deck_subtitle = f"Deep-Dive  ·  Geburtsdatum {date_str}"

    lz = r.lebenszahl
    sz = r.seelenzahl
    pz = r.persoenlichkeit
    az = r.ausdruckszahl

    lz_data = co.LEBENSZAHL_CONTENT[lz]
    sz_data = co.LEBENSZAHL_CONTENT[sz]   # für Seelenzahl-Tiefenporträt nehmen wir denselben Pool
    pz_data = co.PERSOENLICHKEIT_CONTENT[pz]
    az_data = co.AUSDRUCK_CONTENT[az]

    # ============= SEITE 1 — Cover =============
    story.append(Paragraph("Seelenzahlen", H1))
    story.append(Paragraph(deck_subtitle, H1_SUB))
    story.append(HRFlowable(width="100%", thickness=2, color=GOLD, spaceBefore=2, spaceAfter=14))
    story.append(hero_box(str(lz), "LEBENSZAHL", lz_data["tagline"]))
    story.append(Spacer(1, 14))

    story.append(Paragraph(
        "Diese Analyse geht über die Standard-Deutung hinaus. Sie verbindet die klassische "
        "Numerologie nach Maxim Mankevichs Soul-Codes-System mit konkreten Hinweisen für "
        f"Beruf, Beziehung, Geld, Körper und Schattenarbeit — angewandt auf das Geburtsdatum "
        f"<b>{date_str}</b>.", BODYP))

    karma_str = ", ".join(str(k) for k in r.karma_aspekte) if r.karma_aspekte else "—"
    story.append(Paragraph(
        f"Inhalt: ausführliche Berechnung mit allen Nebenzahlen, Tiefenporträt jeder Einzelzahl "
        f"(Lebenszahl {lz}, Seelenzahl {sz}, Persönlichkeit {pz}, Ausdruck {az}), die Dynamik der "
        f"Zahlen untereinander, persönliche Jahresnummer {r.persoenliches_jahr_jahr}, Kompatibilität "
        f"mit anderen Zahlen, typische Lebensphasen und konkrete Reflexionsfragen.", BODYP))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Was du in dieser PDF findest", H3))
    story.append(toc_table([
        (1, "Vollständige Berechnung", "S. 2"),
        (2, f"Lebenszahl {lz} — Tiefenporträt", "S. 3"),
        (3, f"Seelenzahl {sz} — Tiefenporträt", "S. 5"),
        (4, f"Persönlichkeitszahl {pz} — Tiefenporträt", "S. 7"),
        (5, f"Ausdruckszahl {az} — Tiefenporträt", "S. 8"),
        (6, "Karma-Aspekte & Tageszahl", "S. 9"),
        (7, f"Die Dynamik {lz}–{sz}–{pz}–{az} im Zusammenspiel", "S. 10"),
        (8, "Persönliches Jahr & Lebenszyklen", "S. 11"),
        (9, "Kompatibilität & Beziehungen", "S. 12"),
        (10, "Reflexionsfragen & Praxis-Tools", "S. 13"),
    ]))
    story.append(PageBreak())

    # ============= SEITE 2 — Berechnung =============
    story.append(Paragraph("1 · Vollständige Berechnung", H2))
    story.append(Paragraph(f"Alle Zahlen aus {date_str} — Schritt für Schritt", H2_SUB))

    story.append(Paragraph(
        "In der Numerologie nach Mankevich wird das Geburtsdatum auf mehreren Ebenen ausgewertet. "
        "Die Quersumme jedes Datumsteils wird so lange addiert, bis eine einstellige Zahl (1–9) "
        "übrig bleibt. Zweistellige Zwischensummen (11, 22, 33 = Meisterzahlen, 13, 14, 16, 17, 19 "
        "= Karma-Zahlen) tragen eigene Bedeutung und werden mitgelesen.", BODYP))

    story.append(calc_table([
        ["Lebenszahl", "Mission, roter Faden", r.lebenszahl_calc, str(r.lebenszahl)],
        ["Tages-/Seelenzahl", "Innerer Antrieb, „warum“", r.seelenzahl_calc, str(r.seelenzahl)],
        ["Persönlichkeit", "Wie du auftrittst (Monat)", r.persoenlichkeit_calc, str(r.persoenlichkeit)],
        ["Ausdruckszahl", "Wie du wirkst (Jahr)", r.ausdruckszahl_calc, str(r.ausdruckszahl)],
        ["Karma-Aspekte", "Lernimpulse / Meister-Energien", karma_str, ""],
        ["Tageszahl unreduziert", "Geburtstags-Energie", str(r.tageszahl_unreduziert), str(r.tageszahl_unreduziert)],
        ["Wachstumszahl", "Schicksals-Ergänzung", r.wachstumszahl_calc, str(r.wachstumszahl)],
        ["Realisationszahl", "Lebenszahl + Ausdruck", r.realisationszahl_calc, str(r.realisationszahl)],
    ]))

    story.append(Paragraph("Besonderheiten in deinem Code", H3))

    # Karma-Aspekte erläutern (max 3, sonst zu lang)
    explained = 0
    for k in r.karma_aspekte:
        if k in co.KARMA_CONTENT and explained < 3:
            story.append(Paragraph(co.KARMA_CONTENT[k]["title"], H4))
            story.append(Paragraph(co.KARMA_CONTENT[k]["text"], BODYP))
            explained += 1

    if not r.karma_aspekte:
        story.append(Paragraph("Klares Profil ohne klassische Karma-Zahlen", H4))
        story.append(Paragraph(
            "Bei dir taucht in der Reduktionskette keine der klassischen Karma-Zahlen (13, 14, 16, 17, 19) "
            "und keine Meisterzahl (11, 22, 33) direkt auf. Das ist weder „besser“ noch „schlechter“ — es "
            "bedeutet, dass dein Code in einer reinen Form vorliegt und die Themen über die Einzelzahlen "
            "selbst getragen werden.", BODYP))

    story.append(PageBreak())

    # ============= SEITE 3-4 — Lebenszahl Tiefenporträt =============
    story.append(Paragraph(f"2 · Lebenszahl {lz}", H2))
    story.append(Paragraph(lz_data["tagline"], H2_SUB))
    story.append(number_intro(str(lz), lz_data["intro"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Das Kernthema", H3))
    story.append(Paragraph(lz_data["kernthema"], BODYP))

    story.append(Paragraph("Stärken im Vollausbau", H3))
    for p in bullet_list(lz_data["stärken"]):
        story.append(p)

    story.append(Paragraph("Schatten im Vollausbau", H3))
    for p in bullet_list(lz_data["schatten"]):
        story.append(p)

    story.append(PageBreak())

    story.append(Paragraph(f"Berufung der {lz}", H3))
    story.append(Paragraph(lz_data["berufung"], BODYP))

    story.append(Paragraph(f"Geld und {lz}", H3))
    story.append(Paragraph(lz_data["geld"], BODYP))

    story.append(Paragraph(f"Körper und {lz}", H3))
    story.append(Paragraph(lz_data["körper"], BODYP))

    story.append(Paragraph(f"Beziehungen und {lz}", H3))
    story.append(Paragraph(lz_data["beziehungen"], BODYP))

    story.append(Paragraph(f"Die größte Falle der {lz}", H3))
    story.append(quote_box(lz_data["falle"]))

    story.append(PageBreak())

    # ============= SEITE 5-6 — Seelenzahl =============
    story.append(Paragraph(f"3 · Seelenzahl {sz}", H2))
    story.append(Paragraph(sz_data["tagline"], H2_SUB))
    story.append(number_intro(str(sz), sz_data["intro"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Innerer Antrieb — was deine Seele wirklich will", H3))
    story.append(Paragraph(co.SEELENZAHL_KERN[sz], BODYP))

    story.append(Paragraph("Stärken der Seele", H3))
    for p in bullet_list(sz_data["stärken"]):
        story.append(p)

    story.append(Paragraph("Schatten der Seele", H3))
    for p in bullet_list(sz_data["schatten"]):
        story.append(p)

    story.append(PageBreak())

    # Kombination Lebenszahl + Seelenzahl
    story.append(Paragraph(f"Die {sz} in Kombination mit der {lz}", H3))
    kombi = co.kombi_variants(lz, sz)
    story.append(Paragraph(kombi["intro"], BODYP))
    story.append(Spacer(1, 4))
    story.append(Paragraph(kombi["a"], BODYP))
    story.append(Paragraph(kombi["b"], BODYP))
    story.append(Paragraph(kombi["c"], BODYP))
    story.append(Spacer(1, 6))
    story.append(quote_box(
        f"Die {lz} ist dein Weg. Die {sz} ist dein Antrieb. Wer beides trennt, lebt nur halb. "
        "Wer beides verbindet, hinterlässt etwas."
    ))

    story.append(PageBreak())

    # ============= SEITE 7 — Persönlichkeit =============
    story.append(Paragraph(f"4 · Persönlichkeitszahl {pz}", H2))
    story.append(Paragraph(pz_data["tagline"], H2_SUB))
    story.append(number_intro(str(pz), pz_data["intro"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Stärken", H3))
    for p in bullet_list(pz_data["stärken"]):
        story.append(p)

    story.append(Paragraph("Schatten", H3))
    for p in bullet_list(pz_data["schatten"]):
        story.append(p)

    if pz == lz:
        story.append(Paragraph(f"Doppel-{lz} (Lebenszahl + Persönlichkeit)", H3))
        story.append(Paragraph(
            f"Du hast die {lz} sowohl als Lebenszahl als auch als Persönlichkeitszahl. Das ist eine "
            f"sehr starke Verdoppelung — was du tust und wie du wirkst, sind dasselbe. Das gibt dir "
            f"Klarheit und Glaubwürdigkeit, macht dich aber gleichzeitig schwer fassbar für Menschen, "
            f"die dich nur oberflächlich kennen.", BODYP))

    story.append(PageBreak())

    # ============= SEITE 8 — Ausdruck =============
    story.append(Paragraph(f"5 · Ausdruckszahl {az}", H2))
    story.append(Paragraph(az_data["tagline"], H2_SUB))
    story.append(number_intro(str(az), az_data["intro"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Stärken", H3))
    for p in bullet_list(az_data["stärken"]):
        story.append(p)

    story.append(Paragraph("Schatten", H3))
    for p in bullet_list(az_data["schatten"]):
        story.append(p)

    if az == lz:
        story.append(Paragraph(f"Doppel-{lz} (Lebenszahl + Ausdruck)", H3))
        story.append(Paragraph(
            f"Du hast die {lz} sowohl als Lebenszahl als auch als Ausdruck. Deine Mission und deine "
            f"Wirkung in der Welt sind dieselbe Energie — was selten ist und enorme Klarheit gibt.", BODYP))

    story.append(PageBreak())

    # ============= SEITE 9 — Karma-Aspekte & Tageszahl =============
    story.append(Paragraph("6 · Karma-Aspekte & Tageszahl", H2))
    story.append(Paragraph("Die versteckten Hebel deines Codes", H2_SUB))

    if r.karma_aspekte:
        for k in r.karma_aspekte:
            if k in co.KARMA_CONTENT:
                story.append(Paragraph(co.KARMA_CONTENT[k]["title"], H3))
                story.append(Paragraph(co.KARMA_CONTENT[k]["text"], BODYP))
    else:
        story.append(Paragraph("Kein klassischer Karma-Aspekt", H3))
        story.append(Paragraph(
            "Dein Code enthält keine klassische Karma- oder Meisterzahl direkt. Die Lernfelder liegen "
            "dann primär in der Einzelzahl selbst und in den Zahlen, die fehlen (siehe nächste Seite).", BODYP))

    # Tageszahl-Energie
    story.append(Paragraph(f"Tageszahl {r.tageszahl_unreduziert} als Energie-Signatur", H3))
    if r.tageszahl_unreduziert == r.seelenzahl:
        signatur = co.SEELENZAHL_KERN[r.seelenzahl]
        story.append(Paragraph(
            f"Der Geburtstag ({r.tageszahl_unreduziert}) ist bei dir bereits einstellig — die "
            f"Energie ist „rein“. {signatur}", BODYP))
    else:
        # 2-stellige Tageszahl: trägt beide Komponenten
        d1 = r.tageszahl_unreduziert // 10
        d2 = r.tageszahl_unreduziert % 10
        story.append(Paragraph(
            f"Der Tag selbst ({r.tageszahl_unreduziert}) trägt zwei Aspekte: die <b>{d1}</b> "
            f"({co.ZAHL_THEMA.get(d1, '')}) und die <b>{d2}</b> ({co.ZAHL_THEMA.get(d2, '')}). "
            f"Sie reduzieren sich auf die {r.seelenzahl} ({co.ZAHL_THEMA.get(r.seelenzahl, '')}) — "
            f"das ist deine eigentliche Seelen-Frequenz. Aber die beiden Vor-Energien wirken mit: "
            f"sie färben, wie deine Seele in den Alltag eintritt.", BODYP))

    story.append(PageBreak())

    # ============= SEITE 10 — Dynamik =============
    story.append(Paragraph(f"7 · Die Dynamik {lz} – {sz} – {pz} – {az} im Zusammenspiel", H2))
    story.append(Paragraph("Wie deine Zahlen miteinander reden", H2_SUB))

    story.append(Paragraph(
        "Numerologisch interessant ist nicht die Einzelzahl, sondern <b>wie die Zahlen zueinander "
        "stehen</b>. Bei dir bilden sich folgende Felder:", BODYP))

    story.append(Paragraph(f"Die Achse {lz} ↔ {sz} — Mission und Antrieb", H3))
    story.append(Paragraph(
        f"Das ist die <b>vertikale Achse</b> deines Codes. Sie verbindet, was du im Leben tun sollst "
        f"({lz_data['tagline'].split(' · ')[0]}) mit dem, was deine Seele will "
        f"({co.SEELENZAHL_LABEL.get(sz, '')}). Reine Mission ohne inneren Antrieb wird leer. Reiner "
        f"Antrieb ohne Mission wird ziellos. Du musst beide Sprachen sprechen.", BODYP))

    story.append(Paragraph(f"Die Achse {pz} ↔ {az} — Auftritt und Wirkung", H3))
    story.append(Paragraph(
        f"Das ist deine <b>horizontale Achse</b> — die Außenwirkung. Wie du auftrittst ({pz}, "
        f"{pz_data['tagline'].split(' · ')[0]}) und wie deine Wirkung in der Welt landet ({az}, "
        f"{az_data['tagline'].split(' · ')[0]}). Wenn diese beiden gleich sind, wirkst du sehr klar — "
        f"wenn sie verschieden sind, wirst du oft falsch eingeschätzt.", BODYP))

    # Was fehlt
    present = {lz, sz, pz, az, r.wachstumszahl, r.realisationszahl}
    fehlt = co.fehlende_zahlen(*present)

    story.append(Paragraph("Was fehlt — und was das bedeutet", H3))
    if fehlt:
        story.append(Paragraph(
            f"In deinem Code fehlen offen die Zahlen <b>{', '.join(str(n) for n in fehlt)}</b>. In "
            "der Numerologie sind das Lernfelder, nicht Defekte:", BODYP))
        for n in fehlt:
            story.append(Paragraph(f"{n} — {co.ZAHL_THEMA[n]}", H4))
            text = MISSING_TEXTS.get(n, f"Die {n} ist nicht in deinem Code — dieses Thema musst du dir aktiv ins Leben holen, statt darauf zu warten, dass es von alleine kommt.")
            story.append(Paragraph(text, BODYP))
    else:
        story.append(Paragraph(
            "Bei dir kommen alle Zahlen 1-9 in deinem Code vor — eine sehr vollständige Konstellation. "
            "Du hast viele Saiten auf deinem Instrument; die Herausforderung ist eher, sie zusammen zu "
            "stimmen, statt fehlende zu ergänzen.", BODYP))

    story.append(PageBreak())

    # ============= SEITE 11 — Persönliches Jahr =============
    story.append(Paragraph("8 · Persönliches Jahr & Lebenszyklen", H2))
    story.append(Paragraph("Wo du gerade stehst — und was kommt", H2_SUB))

    pj = r.persoenliches_jahr
    pj_data = co.JAHR_CONTENT[pj]
    story.append(Paragraph(f"Persönliches Jahr {r.persoenliches_jahr_jahr}", H3))
    story.append(Paragraph(
        f"Die persönliche Jahreszahl errechnet sich aus Tag + Monat + dem aktuellen Jahr: "
        f"<b>{r.persoenliches_jahr_calc}</b>. Du befindest dich {r.persoenliches_jahr_jahr} in einem "
        f"<b>persönlichen {pj}er-Jahr</b> ({pj_data['tagline']}).", BODYP))

    story.append(Paragraph(pj_data["text"], BODYP))

    # Warnungen bei Karma-Zahlen im pers. Jahr
    pj_path = r.persoenliches_jahr_pfad
    karmic_in_pj = [p for p in pj_path if p in nm.KARMA_ZAHLEN or p in nm.MEISTER_ZAHLEN or p in nm.SPECIAL_ZAHLEN]
    if karmic_in_pj:
        karmic_str = ", ".join(str(k) for k in karmic_in_pj)
        story.append(warning_box(
            f"<b>Hinweis:</b> Dein persönliches Jahr läuft über die Zwischensumme(n) "
            f"<b>{karmic_str}</b>. Das verleiht dem Jahr eine zusätzliche Energie und Lernlektion — "
            f"siehe die Karma-Erklärungen auf Seite 2/9 dieses Dokuments."))

    story.append(Paragraph("Die großen Lebenszyklen", H3))
    rows = []
    for cyc in r.zyklen:
        alter = f"{cyc.alter_von}–{cyc.alter_bis}" if cyc.alter_bis else f"{cyc.alter_von}+"
        rows.append([cyc.label, f"{cyc.zahl} ({cyc.quelle})", alter, cyc.thema])
    story.append(cycle_table(rows))

    # Aktuelles Alter / Zyklus
    today = date.today()
    alter = today.year - r.year - ((today.month, today.day) < (r.month, r.day))
    if alter < 28:
        zyklus_text = f"Du befindest dich mit {alter} Jahren noch im <b>1. Zyklus</b> — der Phase, in der die <b>{r.persoenlichkeit}</b> ({co.ZAHL_THEMA[r.persoenlichkeit]}) dominiert."
    elif alter < 56:
        zyklus_text = f"Du befindest dich mit {alter} Jahren im <b>2. Zyklus</b> — der Phase, in der die <b>{r.seelenzahl}</b> ({co.ZAHL_THEMA[r.seelenzahl]}) dominiert."
    else:
        zyklus_text = f"Du befindest dich mit {alter} Jahren im <b>3. Zyklus</b> — der Phase, in der die <b>{r.ausdruckszahl}</b> ({co.ZAHL_THEMA[r.ausdruckszahl]}) dominiert."
    story.append(Paragraph(zyklus_text, BODYP))

    story.append(PageBreak())

    # ============= SEITE 12 — Kompatibilität =============
    story.append(Paragraph("9 · Kompatibilität & Beziehungen", H2))
    story.append(Paragraph("Welche Zahlen mit deinem Code resonieren", H2_SUB))

    story.append(Paragraph(
        "Numerologische Kompatibilität ist keine Garantie und kein Ausschluss — aber sie zeigt, "
        f"wo Reibung produktiv ist und wo sie nur müde macht. Bezogen auf deine Lebenszahl {lz} "
        f"und Seelenzahl {sz}:", BODYP))

    story.append(compat_table(co.kompatibilitaets_zeilen(lz)))

    story.append(Paragraph("Für deinen Code besonders relevant", H3))
    if fehlt:
        story.append(Paragraph(
            f"Du hast in deinem eigenen Code keine <b>{', '.join(str(n) for n in fehlt)}</b>. "
            f"Menschen mit diesen Zahlen <b>ergänzen dich am stärksten</b>. Achte auf sie in deinem "
            f"engsten Kreis — Partner:in, beste Freund:in, Mentor:in, COO/Co-Founder:in. Wo du sie "
            f"schon hast, ehre sie. Wo nicht, halte die Augen offen.", BODYP))
    else:
        story.append(Paragraph(
            "Da du alle Zahlen 1-9 in deinem Code hast, ist Kompatibilität bei dir weniger eine "
            "Frage von „was fehlt“, sondern „was schwingt mit meiner Lebens- und Seelenzahl mit“. "
            "Die obige Tabelle gibt dir die Hauptlinien.", BODYP))

    story.append(PageBreak())

    # ============= SEITE 13 — Reflexion =============
    story.append(Paragraph("10 · Reflexionsfragen & Praxis-Tools", H2))
    story.append(Paragraph("Was du mit der Analyse machst", H2_SUB))

    # Fragen für die Lebenszahl
    story.append(Paragraph(f"Reflexionsfragen für die Lebenszahl {lz}", H3))
    for p in bullet_list(REFLEXION_FRAGEN.get(lz, REFLEXION_FRAGEN[1])):
        story.append(p)

    # Fragen für die Seele
    story.append(Paragraph(f"Reflexionsfragen für die Seele {sz}", H3))
    for p in bullet_list(REFLEXION_FRAGEN.get(sz, REFLEXION_FRAGEN[6])):
        story.append(p)

    # Fragen für Karma (wenn vorhanden)
    if r.karma_aspekte:
        story.append(Paragraph("Reflexionsfragen für die Karma-Aspekte", H3))
        for p in bullet_list(KARMA_FRAGEN_GENERAL):
            story.append(p)

    story.append(Paragraph("Konkrete Praxis-Tools", H3))

    story.append(Paragraph("Tägliches Tool", H4))
    story.append(Paragraph(
        "<b>5 Minuten morgens schreiben — nur für dich.</b> Kein Plan, keine To-Dos. Eine Frage: "
        "„Was will ich heute wirklich?“ Die meisten Antworten kommen leiser, als man denkt — und "
        "ehrlicher als die, die man laut formuliert.", BODYP))

    story.append(Paragraph("Wöchentliches Tool", H4))
    story.append(Paragraph(
        "<b>Eine echte Begegnung pro Woche — ohne Output.</b> Mit einem Menschen, der dir wichtig "
        "ist. Kein „wie läuft's bei dir?“-Smalltalk, sondern eine ehrliche Stunde.", BODYP))

    story.append(Paragraph(f"Für dein persönliches {pj}er-Jahr {r.persoenliches_jahr_jahr} konkret", H4))
    for p in bullet_list(pj_data["todo"]):
        story.append(p)

    story.append(PageBreak())

    # ============= SEITE 14 — Abschluss =============
    story.append(Spacer(1, 60))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceBefore=4, spaceAfter=10))
    story.append(Paragraph(
        f"„Die {lz} ist dein Weg. Die {sz} ist dein Antrieb. Die {pz} ist dein Auftritt. Die {az} "
        f"ist deine Spur. Wenn alle vier in dir am selben Tisch sitzen, bist du jemand, der nicht "
        "nur Erfolg hat, sondern Spuren hinterlässt.“",
        ParagraphStyle('FQ', fontName='Helvetica-Oblique', fontSize=11, leading=15,
                       textColor=colors.HexColor("#2a2a2a"), spaceAfter=4, alignment=TA_JUSTIFY)
    ))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceBefore=10, spaceAfter=18))

    story.append(Paragraph(
        "Quelle & weiterführend: Maxim Mankevich, Soul-Codes-System (akademie.maximmankevich.com), "
        "Podcast {ungeskriptet} #123, Buch <i>Soul Master</i>. Klassische Numerologie-Literatur: "
        "Dan Millman, „Die Lebenszahl als Lebensplan“.", SMALL))

    story.append(Spacer(1, 8))
    target = f"das Geburtsdatum {date_str}"
    if r.name:
        target = f"{r.name} ({date_str})"
    story.append(Paragraph(
        f"Hinweis: Numerologie ist ein spirituell-symbolisches Deutungssystem ohne wissenschaftlichen "
        f"Wirksamkeitsnachweis. Diese PDF ist ein Reflexionsangebot, keine Empfehlung für Lebens-, "
        f"Karriere-, Gesundheits- oder Finanzentscheidungen. Erstellt für {target} als persönliche "
        f"Lektüre — keine Beratung im Sinne einer professionellen Therapie, Coaching- oder "
        f"Finanzdienstleistung.", DISC))

    return story


# ---------- Static texts not in content.py ----------

MISSING_TEXTS = {
    1: "Die 1 fehlt — heißt: Pionier-Energie und „eigener Weg gehen“ sind für dich kein Selbstläufer. Du musst dir Initiative aktiv antrainieren, anstatt darauf zu warten, dass dich jemand führt.",
    2: "Die 2 fehlt — heißt: Augenhöhe, Sensibilität und echte Partnerschaft sind Lernfeld. Du musst aktiv lernen, in Beziehungen nicht zu führen, sondern zu hören.",
    3: "Die 3 fehlt — heißt: Sichtbarkeit, Kreativität und Sprache sind nicht angeboren. Du darfst dir bewusst Räume für Ausdruck schaffen, in denen es nicht „nützlich“, sondern spielerisch ist.",
    4: "Die 4 fehlt — heißt: Disziplin, Routine, Boden. Strukturen, die ohne dich laufen, baust du nicht von selbst. Du musst sie dir antrainieren, sonst macht dein System früher oder später schlapp.",
    5: "Die 5 fehlt — heißt: Bewegung, Vielfalt, Risiko. Reisen, neue Umfelder, fremde Branchen — das musst du dir aktiv geben, sonst engt sich dein Leben in einer schmalen Spur.",
    6: "Die 6 fehlt — heißt: Familie, Harmonie, Schönheit. Es liegt dir nicht von selbst, dich um Beziehungen, dein Heim, dein Umfeld ästhetisch zu kümmern. Bewusst pflegen, sonst kommt es zu kurz.",
    7: "Die 7 fehlt — heißt: Innenarbeit ist Lernfeld. Therapie, Meditation, Tagebuch, ehrliche Freunde — das sind keine Hobbies, das sind Tools, die du dir bewusst ins Leben einbauen darfst.",
    8: "Die 8 fehlt — heißt: Macht, Geld und Manifestation sind nicht dein Hauptthema. Du kannst sie kultivieren, aber sie kommen dir nicht zu, wenn du sie nicht aktiv suchst.",
    9: "Die 9 fehlt — heißt: das große „warum, was bleibt von mir?“-Thema ist nicht angeboren. Mach dir keinen Stress, wenn du keine fertige „Mission“ hast — du findest sie auf dem Weg.",
}


REFLEXION_FRAGEN = {
    1: [
        "Wo lebe ich gerade noch jemand anderes Weg — meiner Eltern, meiner Freunde, einer Erwartung — und tue so, als wäre es meiner?",
        "Wann habe ich zuletzt etwas <i>angefangen</i>, ohne erst Erlaubnis zu suchen?",
        "Welcher Schritt wäre dran, wenn ich wüsste, dass niemand zuschaut?",
        "Wo verwechsle ich „alleine sein“ mit „stark sein“?",
    ],
    2: [
        "Wo halte ich gerade den Frieden auf Kosten meiner Wahrheit?",
        "Wem in meinem Leben sage ich nicht, was ich wirklich denke — und warum?",
        "Wann hat mir zuletzt jemand etwas gegeben, ohne dass ich vorher etwas leisten musste?",
        "Wo verwechsle ich Selbstaufgabe mit Liebe?",
    ],
    3: [
        "Wo nutze ich Charme, um mich vor Tiefe zu drücken?",
        "Welche Anerkennung suche ich gerade unbewusst — und von wem?",
        "Wann habe ich zuletzt etwas <i>ohne</i> Publikum gemacht, einfach nur für mich?",
        "Welche Maske kann ich mir gerade nicht mehr leisten?",
    ],
    4: [
        "Welche Struktur, die ich mir aufgebaut habe, dient mir noch — und welche dient nur sich selbst?",
        "Wo bin ich aus Sicherheit, nicht aus Liebe geblieben?",
        "Wann habe ich zuletzt etwas Spontanes gemacht, ohne es zu planen?",
        "Wem in meinem Leben gebe ich keinen Raum, weil er/sie nicht „verlässlich“ ist?",
    ],
    5: [
        "Wo laufe ich gerade weg, statt durchzugehen?",
        "Welche Routine wäre für mich gerade <i>befreiend</i>, nicht einschränkend?",
        "Was hat mich zuletzt wirklich gelangweilt — und was sagt das?",
        "Welche Bindung fürchte ich, weil ich mich darin verlieren könnte?",
    ],
    6: [
        "Für wen sorge ich gerade, der/die meine Sorge gar nicht braucht?",
        "Welche Beziehung halte ich aus Loyalität, obwohl sie mich kleiner macht?",
        "Wann hat mir zuletzt jemand gegeben, ohne dass ich vorher etwas geleistet habe?",
        "Was hieße es konkret, mir selbst die Wärme zu geben, die ich anderen gebe?",
    ],
    7: [
        "Welche Wahrheit weiß ich seit Jahren, ohne sie auszusprechen?",
        "Wo nutze ich Rückzug als Ausrede, statt als Heilmittel?",
        "Welcher Mensch in meinem Leben darf meine Tiefe wirklich sehen?",
        "Wo bin ich „über“ den anderen geflogen, statt mit ihnen zu sein?",
    ],
    8: [
        "Welche Zahl auf meinem Konto würde ausreichen, damit ich aufhören würde, mich zu beweisen?",
        "Welche Aufgabe mache ich noch selbst, obwohl es längst Zeit wäre loszulassen?",
        "Wann habe ich zuletzt drei Tage nichts produziert — ohne dass es zur Krise wurde?",
        "Wem in meinem Team/Umfeld gebe ich Vertrauen, nicht weil er „liefert“, sondern weil er <i>ist</i>?",
    ],
    9: [
        "Was möchte ich, dass von mir bleibt?",
        "Welche Themen kommen immer wieder zu mir — auch wenn ich sie nicht suche?",
        "Wo opfere ich mich für etwas, das mich gar nicht mehr braucht?",
        "Welche Wahrheit weiß ich seit Jahren, ohne sie auszusprechen?",
    ],
}

KARMA_FRAGEN_GENERAL = [
    "Welcher wiederkehrende Lebens-Loop will gerade entweder verstanden oder verlassen werden?",
    "Wo missbrauche ich gerade — auch leise — eine Position, einen Status, eine Beziehung?",
    "Welche Wahrheit würde, wenn ich sie aussprechen würde, gerade eine alte Struktur kollabieren lassen?",
    "Welcher Glaubenssatz über mich („ich bin der/die, der/die …“) müsste eigentlich einstürzen, damit ich freier wäre?",
]


# ---------- Public API: in-memory generation ----------

def generate_pdf_bytes(date_str: str, name: str = None,
                       year_for_personal: int = None) -> io.BytesIO:
    """Erzeugt das PDF in-memory und gibt einen BytesIO-Stream zurück.

    Verwendet von der Flask-Webseite. Wirft ValueError bei ungültigem Datum.

    Args:
        date_str: Geburtsdatum als 'DD.MM.YYYY' (auch mit '-' oder '/' als Trenner).
        name: Optionaler Name, der auf Cover und Footer erscheint.
        year_for_personal: Kalenderjahr für „persönliches Jahr". Default: aktuelles Jahr.

    Returns:
        BytesIO mit dem fertigen PDF, gespult auf Position 0.
    """
    day, month, year = nm.parse_date_string(date_str)
    if year_for_personal is None:
        year_for_personal = date.today().year

    reading = nm.compute(day, month, year, name=name,
                         year_for_personal=year_for_personal)

    if name:
        footer = f"Seelenzahlen Deep-Dive  ·  {name} · {day:02d}.{month:02d}.{year:04d}"
    else:
        footer = f"Seelenzahlen Deep-Dive  ·  {day:02d}.{month:02d}.{year:04d}"

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        leftMargin=MARGIN_L, rightMargin=MARGIN_R,
        topMargin=MARGIN_T, bottomMargin=MARGIN_B,
        title=f"Seelenzahlen Deep-Dive — {day:02d}.{month:02d}.{year:04d}",
        author="Seelenzahlen Deep-Dive",
        subject="Numerologie nach Maxim Mankevich",
    )
    chrome = make_chrome(footer)
    story = build_story(reading)
    doc.build(story, onFirstPage=chrome, onLaterPages=chrome)
    buffer.seek(0)
    return buffer


def suggested_filename(date_str: str, name: str = None) -> str:
    """Liefert einen sauberen Download-Dateinamen."""
    day, month, year = nm.parse_date_string(date_str)
    date_compact = f"{day:02d}-{month:02d}-{year:04d}"
    if name:
        slug = "_" + "-".join(name.split())
    else:
        slug = ""
    return f"Seelenzahlen_{date_compact}{slug}_Deep-Dive.pdf"


# ---------- CLI (für lokale Tests) ----------
def main():
    parser = argparse.ArgumentParser(description="Seelenzahlen Deep-Dive PDF Generator")
    parser.add_argument("datum", help="Geburtsdatum als DD.MM.YYYY")
    parser.add_argument("--name", default=None, help="Optionaler Name (erscheint im Cover/Footer)")
    parser.add_argument("--out", default=None, help="Output-Pfad (Default: ./Seelenzahlen_<datum>.pdf)")
    parser.add_argument("--year", type=int, default=None,
                        help="Jahr für persönliches Jahr (Default: aktuelles Kalenderjahr)")
    args = parser.parse_args()

    buffer = generate_pdf_bytes(args.datum, name=args.name, year_for_personal=args.year)
    out_path = args.out or suggested_filename(args.datum, args.name)
    with open(out_path, "wb") as f:
        f.write(buffer.read())
    print(f"OK: {out_path}")


if __name__ == "__main__":
    main()
