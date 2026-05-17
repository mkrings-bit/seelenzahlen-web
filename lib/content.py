"""Content-Bibliothek für den Seelenzahlen Deep-Dive PDF Generator.

Stil: warm, klar, manchmal pointiert. Sprache duzt. Nicht esoterisch-schwurbelig.
Quelle der Deutungen: Maxim Mankevich (Soul-Codes-System), erweitert.

Pro Position gibt es Content für die Zahlen 1-9. Karma-Zahlen separat.
"""

# =======================================================================
# LEBENSZAHL — pro Zahl: tagline, intro, kernthema, stärken, schatten,
# berufung, geld, körper, beziehungen, falle (Quote)
# =======================================================================

LEBENSZAHL_CONTENT = {
    1: {
        "tagline": "Pionier · Initiative · Eigenständigkeit",
        "intro": (
            "Die 1 ist im numerologischen System die <b>Zahl des Ursprungs</b>. Sie ist der erste Impuls, "
            "der „Es werde“, der Punkt, an dem aus Nichts etwas wird. In Mankevichs Lesart ist sie die "
            "Zahl der Pioniere, Erfinder, Gründer, Solokünstler. 1er sind hier, um etwas anzustoßen, "
            "was es vorher so nicht gab."
        ),
        "kernthema": (
            "Die 1 ist hier, um <b>einen eigenen Weg zu gehen</b> — nicht den der Eltern, nicht den der "
            "Schule, nicht den, den „man so macht“. Sie lernt nicht durch Anpassung, sondern durch "
            "Ausbrechen, Hinfallen, neu Beginnen. Eine 1, die sich zu lange unterordnet, wird im Inneren "
            "krank — sie verliert Saft, Mut, Lebenslust. Der eigene Weg ist für die 1 nicht Luxus, sondern "
            "Existenz-Bedingung."
        ),
        "stärken": [
            "<b>Initiativ-Kraft</b> — die 1 fängt an, wo andere noch diskutieren.",
            "<b>Mut zur Einsamkeit</b> — sie kann allein vorgehen, wenn niemand mitkommt.",
            "<b>Klares Ich</b> — weiß, was sie will, sobald sie es ehrlich sucht.",
            "<b>Original-Faktor</b> — kopiert nicht, sondern erfindet eine eigene Sprache.",
            "<b>Schnelligkeit</b> — entscheidet zügig, korrigiert zügig, bleibt nicht stecken.",
            "<b>Inspirationskraft</b> — andere folgen ihr, weil sie spürt, wohin der Weg geht.",
        ],
        "schatten": [
            "<b>Ego-Aufblähung</b> — Ich-Stärke kippt leicht in Selbstüberhöhung.",
            "<b>Einsamkeit</b> — wer immer vorgeht, hat selten jemanden an seiner Seite.",
            "<b>Sturheit</b> — Rat von außen wird als Angriff auf die Autonomie gelesen.",
            "<b>Ungeduld</b> — wartet ungern auf andere, brennt schnell aus.",
            "<b>„Ich gegen die Welt“-Haltung</b> — sieht Allianzen als Schwäche.",
            "<b>Härte gegen sich selbst</b> — eine 1 verzeiht sich Versagen schlechter als jeder andere.",
        ],
        "berufung": (
            "Die 1 ist nicht hier, um angestellt zu sein. Sie kann es eine Zeitlang sein — meistens, um "
            "die Branche zu lernen — aber irgendwann muss sie loslaufen. Klassische Berufungen: "
            "<b>Gründer:in, Unternehmer:in, Erfinder:in, Künstler:in mit eigener Handschrift, Sportler:in, "
            "Coach, Pionier:in in irgendeinem Feld</b>. Auch das klassische Solo-Format passt: Autor:in, "
            "Musiker:in, Speaker:in, Berater:in. Wichtig ist, dass die 1 ihren <i>eigenen Namen</i> sieht — "
            "nicht den der Firma. Wer sie zwingt, anonym zu sein, verliert sie."
        ),
        "geld": (
            "Die 1 verdient Geld, sobald sie ihr Eigenes macht. Solange sie für andere arbeitet, deckelt "
            "sie sich selbst. 1er, die sich selbstständig machen, erleben oft einen sprunghaften Anstieg "
            "ihres Einkommens — nicht weil sie plötzlich klüger sind, sondern weil das System mit ihnen "
            "ausrichtet. <b>Falle:</b> Die 1 glaubt manchmal, sie müsse <i>alles</i> selbst können. Genau "
            "dadurch deckelt sie sich später erneut — diesmal als ihre eigene Chefin."
        ),
        "körper": (
            "Klassische 1er-Themen: <b>Kopf</b> (Migräne, Stirn, Augen), <b>Nacken</b> (zu viel „nach vorne“), "
            "<b>Herz</b> (wenn sie sich verschließt). Die 1 ist eine „heiße“ Energie — Yang, vorwärts, "
            "brennend. Heilmittel: Natur, langsame Bewegung, Atemtechniken, die <b>nach unten</b> führen."
        ),
        "beziehungen": (
            "Die 1 ist im Außen oft hart, im Inneren überraschend weich. Sie braucht jemanden, der "
            "ihren <i>Weg</i> respektiert, sie aber nicht „erträgt“ wie ein launisches Genie. Gefahr: die "
            "1 sucht oft jemanden, der sie bewundert — und merkt zu spät, dass Bewunderung keine "
            "Augenhöhe ist. <b>Geliebt werden ist nicht dasselbe wie bewundert werden.</b>"
        ),
        "falle": (
            "Zu glauben, dass „alleine“ und „eigenständig“ dasselbe sind. Eine 1 ist nicht alleine — "
            "sie geht voran. Wer den Unterschied nicht versteht, baut sein Leben als Mauer und nennt "
            "es Freiheit."
        ),
    },
    2: {
        "tagline": "Partnerschaft · Sensibilität · Balance",
        "intro": (
            "Die 2 ist die <b>Zahl der Beziehung</b>. Sie ist die erste Zahl, die nicht für sich alleine "
            "stehen will, sondern für das, was zwischen zwei Menschen entsteht. In Mankevichs Lesart "
            "ist sie die Zahl der Diplomatinnen, Heilerinnen, Vermittlerinnen — Menschen, die nicht durch "
            "Macht wirken, sondern durch Resonanz."
        ),
        "kernthema": (
            "Die 2 ist hier, um <b>Brücken zu bauen</b>. Sie spürt feiner als andere, hört zwischen "
            "den Zeilen, ahnt Stimmungen, bevor sie ausgesprochen werden. Sie lernt nicht im Alleingang, "
            "sondern im Dialog. Eine 2, die sich isoliert, verliert ihren Resonanzraum — und damit sich "
            "selbst."
        ),
        "stärken": [
            "<b>Hochsensibilität</b> — nimmt mehr wahr als die meisten, schneller.",
            "<b>Diplomatie</b> — kann zwischen Welten übersetzen, ohne zu lügen.",
            "<b>Geduld</b> — wartet, bis Dinge reif sind, statt zu erzwingen.",
            "<b>Empathie</b> — fühlt sich in andere ein, ohne sich zu verlieren.",
            "<b>Kooperation</b> — kann mit anderen wachsen, statt gegen sie.",
            "<b>Treue</b> — hält durch, auch wenn’s zwischendurch zäh wird.",
        ],
        "schatten": [
            "<b>Selbstverlust</b> — gibt sich auf, um Frieden zu wahren.",
            "<b>Konfliktangst</b> — vermeidet Klartext, bis es eskaliert.",
            "<b>Co-Abhängigkeit</b> — lebt durch den anderen statt mit ihm.",
            "<b>Überempfindlichkeit</b> — nimmt Dinge persönlich, die nicht so gemeint sind.",
            "<b>Stille Bitterkeit</b> — schluckt, statt zu benennen.",
            "<b>Unentschiedenheit</b> — sieht beide Seiten so klar, dass sie nicht handelt.",
        ],
        "berufung": (
            "Die 2 ist nicht hier, um zu führen. Sie ist hier, um zu <b>verbinden</b>. Klassische Berufungen: "
            "Therapeut:in, Mediator:in, Pflege, HR, Diplomatie, Beratung, Co-Founder:in. Auch Kunst, in der "
            "Resonanz wichtiger ist als Solo-Brillanz: Musik im Ensemble, Tanz, Schauspiel."
        ),
        "geld": (
            "Die 2 verdient Geld über Beziehung. Sie hat Schwierigkeiten, sich „aufzudrängen“ — was "
            "geschäftlich teuer wird. Heilmittel: erkennen, dass das, was sie spürt und vermittelt, einen "
            "echten Wert hat. Eine 2, die ihren Wert klar benennt, wird sehr gut entlohnt."
        ),
        "körper": (
            "Klassische 2er-Themen: <b>Magen</b> (was schlucke ich runter?), <b>Bauch</b> (Bauchgefühl als "
            "Wahrheitsorgan), <b>Hormonsystem</b> (Sensibilität für Zyklen). Eine 2 braucht ruhige "
            "Umgebungen, weiche Materialien, Wasser, Natur. Reizüberflutung ist ihr ärgster Feind."
        ),
        "beziehungen": (
            "Die 2 ist <i>die</i> Beziehungs-Zahl. Sie sucht Verbindung, lebt durch sie. Gefahr: sie wählt "
            "Partner, deren Schatten sie heilen will — und merkt nicht, dass sie sich selbst dabei "
            "auslöscht. Heilung kommt, wenn die 2 lernt: <b>Augenhöhe ist mehr wert als Symbiose.</b>"
        ),
        "falle": (
            "Zu glauben, dass Liebe heißt, sich selbst kleinzumachen, damit der andere groß bleibt. Eine "
            "2 in voller Größe ist kein Konkurrent — sie ist der Resonanzraum, in dem beide wachsen."
        ),
    },
    3: {
        "tagline": "Kreativität · Sprache · Sichtbarkeit",
        "intro": (
            "Die 3 ist die <b>Zahl des Ausdrucks</b>. Wo die 1 schweigt und macht, redet die 3 — und "
            "macht damit etwas Eigenes hörbar. In Mankevichs Lesart ist sie die Zahl der Künstler:innen, "
            "Speaker:innen, Schauspieler:innen, Autor:innen, Influencer:innen. Wer „Charisma“ hat, hat "
            "meistens eine 3 im Code."
        ),
        "kernthema": (
            "Die 3 ist hier, um <b>sichtbar zu sein</b> — und damit anderen Mut zur eigenen Sichtbarkeit "
            "zu geben. Sie lernt durch Performance, durch Versuch und Irrtum auf der Bühne (im weitesten "
            "Sinn). Eine 3, die ihr Talent versteckt, verkümmert. Sie braucht Ausdruck wie Sauerstoff."
        ),
        "stärken": [
            "<b>Sprachgefühl</b> — findet den Satz, der ankommt.",
            "<b>Charisma</b> — zieht Räume auf sich, ohne es zu wollen.",
            "<b>Humor</b> — entwaffnet Spannung mit Leichtigkeit.",
            "<b>Storytelling</b> — kann Visionen so erzählen, dass Leute mitgehen.",
            "<b>Optimismus</b> — sieht Möglichkeiten, wo andere Probleme sehen.",
            "<b>Sozialer Klebstoff</b> — verbindet verschiedene Gruppen.",
        ],
        "schatten": [
            "<b>Anerkennungs-Hunger</b> — merkt nicht, wie sehr sie gesehen werden will.",
            "<b>Selbstdarstellung</b> — wenn die Substanz fehlt, wird die 3 zur Fassade.",
            "<b>Vermeidung von Tiefe</b> — über Schmerz lieber Witze machen.",
            "<b>Zerstreuung</b> — fängt zehn Dinge an, beendet drei.",
            "<b>Theatralik</b> — kann Drama produzieren, wo Klarheit reichen würde.",
            "<b>Maskerade</b> — kann so charmant sein, dass niemand merkt, wie’s ihr geht.",
        ],
        "berufung": (
            "Die 3 ist nicht hier, um im Hintergrund zu arbeiten. Sie ist hier, um <b>zu zeigen, zu erzählen, "
            "zu inspirieren</b>. Klassische Berufungen: Schauspiel, Musik, Schreiben, Comedy, Marketing, "
            "Vertrieb, Lehre, Coaching mit Bühnen-Element. Auch Mode, Design, alles Visuelle."
        ),
        "geld": (
            "Die 3 verdient Geld über Reichweite und Charme. Sie muss aufpassen, dass sie nicht ihre "
            "Substanz verkauft, sondern ihre Wirkung. Wer nur lacht, verdient nicht. Wer lacht und liefert, "
            "wird sehr gut bezahlt."
        ),
        "körper": (
            "Klassische 3er-Themen: <b>Hals/Stimme</b> (Ausdruck zugehalten?), <b>Haut</b> (Sichtbarkeit), "
            "<b>Nervensystem</b> (Reizüberflutung durch zu viele Bühnen)."
        ),
        "beziehungen": (
            "Die 3 ist charmant, aber oft schwer fassbar — Partner wissen nicht immer, ob sie wirklich da "
            "ist oder gerade „Show“ macht. Heilung: die 3 lernt, hinter der Fassade verletzlich zu sein. "
            "Dann wird sie wirklich geliebt, nicht nur bewundert."
        ),
        "falle": (
            "Zu glauben, dass Applaus dasselbe ist wie Liebe. Eine 3 ohne private Tiefe ist ein Feuerwerk: "
            "schön, kurz, dann dunkel."
        ),
    },
    4: {
        "tagline": "Struktur · Disziplin · Boden",
        "intro": (
            "Die 4 ist die <b>Zahl des Hauses</b> — Wände, Fundament, Dach. In Mankevichs Lesart ist sie "
            "die Zahl der Handwerker:innen, Ingenieur:innen, Architekt:innen, Bauern, Verwalter:innen — "
            "aller, die etwas Bleibendes errichten. Eine 4 baut. Langsam, gründlich, oft unbemerkt."
        ),
        "kernthema": (
            "Die 4 ist hier, um <b>Struktur in die Welt zu bringen</b>. Sie lernt nicht durch große "
            "Sprünge, sondern durch tägliche Wiederholung. Eine 4, die zu früh aufgibt, verliert ihren "
            "Trumpf: die Zeit auf ihrer Seite zu haben."
        ),
        "stärken": [
            "<b>Disziplin</b> — macht, was gemacht werden muss, auch ohne Lust.",
            "<b>Zuverlässigkeit</b> — was sie sagt, gilt. Punkt.",
            "<b>Geduld</b> — kann Jahre an einer Sache arbeiten.",
            "<b>Praktische Klugheit</b> — Hand und Kopf koordiniert, Lösungen statt Theorie.",
            "<b>Loyalität</b> — bleibt, wenn andere gehen.",
            "<b>Ressourcen-Sinn</b> — verschwendet weder Geld, Zeit noch Material.",
        ],
        "schatten": [
            "<b>Sturheit</b> — hält an Strukturen fest, die längst kollabieren sollten.",
            "<b>Pessimismus</b> — sieht zuerst, was schiefgehen könnte.",
            "<b>Engstirnigkeit</b> — was nicht in den Bauplan passt, gibt es nicht.",
            "<b>Sparsamkeit, die zu Geiz wird</b> — Angst, dass nicht genug da ist.",
            "<b>Workaholic-Disposition</b> — verwechselt Arbeit mit Identität.",
            "<b>Mangel an Spontaneität</b> — alles muss geplant sein.",
        ],
        "berufung": (
            "Die 4 ist eine der wenigen Zahlen, die in Strukturen blüht. Klassische Berufungen: "
            "Handwerk, Bauwesen, Logistik, Verwaltung, Buchhaltung, Operations, COO-Rollen, Ingenieurwesen, "
            "Landwirtschaft. Auch alles, was lange Zeit braucht: Wein, Spirituosen, klassische Musik."
        ),
        "geld": (
            "Die 4 verdient Geld langsam und nachhaltig. Sie macht keine Sprünge, baut aber unbemerkt "
            "Vermögen auf. Falle: sie kann so sehr sparen, dass sie das Leben dabei vergisst."
        ),
        "körper": (
            "Klassische 4er-Themen: <b>Knochen, Gelenke, Knie</b> (Last der Verantwortung), <b>Rücken</b>, "
            "<b>Immunsystem</b> (kann lange durchhalten — bis es bricht)."
        ),
        "beziehungen": (
            "Die 4 ist verlässlich und treu — aber selten leidenschaftlich-überraschend. Sie braucht "
            "jemanden, der ihre Beständigkeit nicht mit Langweiligkeit verwechselt. Heilung: die 4 lernt, "
            "auch im Beziehungsalltag Räume für Verspieltheit zu öffnen."
        ),
        "falle": (
            "Zu glauben, dass Sicherheit dasselbe ist wie Leben. Eine 4 in voller Form baut nicht gegen "
            "die Angst, sondern durch sie hindurch — und merkt, dass das eigentliche Haus innen ist."
        ),
    },
    5: {
        "tagline": "Freiheit · Bewegung · Wandel",
        "intro": (
            "Die 5 ist die <b>Zahl der Erfahrung</b>. Sie ist die einzige Zahl, die das Risiko liebt — "
            "weil sie weiß, dass Lernen nur dort passiert, wo es kippen könnte. In Mankevichs Lesart "
            "ist sie die Zahl der Reisenden, Vertriebsmenschen, Pionier:innen, Schauspieler:innen, "
            "Journalist:innen — aller, die nicht stehen bleiben."
        ),
        "kernthema": (
            "Die 5 ist hier, um <b>die Welt zu erfahren</b>. Sie lernt nicht durch Bücher, sondern durch "
            "Reisen, Begegnungen, Wechsel. Sie braucht Vielfalt wie andere Sauerstoff. Eine 5, die zu "
            "lange im selben Raum sitzt, wird körperlich krank."
        ),
        "stärken": [
            "<b>Schnelle Auffassung</b> — versteht Menschen und Märkte in Sekunden.",
            "<b>Kommunikation</b> — kann in jeder Schicht andocken.",
            "<b>Mut</b> — entscheidet schnell, korrigiert schnell.",
            "<b>Vertrieb</b> — die klassische Verkäufer:innen-Zahl.",
            "<b>Anpassungsfähigkeit</b> — findet sich überall ein.",
            "<b>Neugier</b> — verliert nie das Interesse an Neuem.",
        ],
        "schatten": [
            "<b>Sprunghaftigkeit</b> — fängt zehn Dinge an, beendet drei.",
            "<b>Suchtanfälligkeit</b> — braucht Reize; ohne Disziplin wird daraus Stoff, Spiel, Sex.",
            "<b>Bindungsangst</b> — alles „Endgültige“ löst Flucht aus.",
            "<b>Oberflächlichkeit</b> — wenn Tiefe nicht eingreift, bleibt es Show.",
            "<b>Verantwortungs-Scheu</b> — meidet, was sie festlegen würde.",
            "<b>Hyperaktivität</b> — kann nicht still sitzen, auch wenn der Körper schreit.",
        ],
        "berufung": (
            "Die 5 lebt von Wechsel. Klassische Berufungen: Reise, Vertrieb, Journalismus, Übersetzung, "
            "Kommunikation, internationales Geschäft, Schauspiel, Speaker, Pilot:in, Trainer:in."
        ),
        "geld": (
            "Die 5 verdient Geld in Wellen — manchmal viel, manchmal nichts. Sie muss lernen, in den "
            "fetten Phasen für die mageren zu sparen. Klassische 5er-Falle: alles wieder verbraten, "
            "weil das nächste Abenteuer ruft."
        ),
        "körper": (
            "Klassische 5er-Themen: <b>Bewegungsapparat</b> (Hyperaktivität), <b>Nerven</b> (Reizüberflutung), "
            "<b>Suchtsystem</b> (Dopamin-Hunger). Heilmittel: Disziplin, Routine, Atemarbeit."
        ),
        "beziehungen": (
            "Die 5 fürchtet die Endgültigkeit. Eine reife 5 lernt, dass Bindung keine Falle ist, sondern "
            "ein Raum, in dem auch sie wachsen darf — ohne wegzulaufen."
        ),
        "falle": (
            "Zu glauben, dass Freiheit Abwesenheit von Verbindung ist. Eine wirklich freie 5 ist gebunden — "
            "an Werte, an Menschen, an sich selbst. Alles andere ist nur Flucht in höherer Auflösung."
        ),
    },
    6: {
        "tagline": "Liebe · Verantwortung · Schönheit",
        "intro": (
            "Die 6 ist die <b>Herz-Zahl</b>. Sie steht für Familie, Beziehung, Schönheit, Heim, "
            "Verantwortung. In Mankevichs Lesart ist sie die Zahl der Heiler:innen, Eltern, Lehrer:innen, "
            "Designer:innen — aller, die <i>für etwas oder jemanden</i> da sind."
        ),
        "kernthema": (
            "Die 6 ist hier, um <b>zu lieben und Schönheit zu erschaffen</b>. Sie lernt nicht durch "
            "Eroberung, sondern durch Pflege. Eine 6, die nichts mehr zu hüten hat, verwelkt — "
            "sie braucht ein Gegenüber, das ihre Wärme empfängt."
        ),
        "stärken": [
            "<b>Bindungsfähigkeit</b> — kann tiefe, langjährige Beziehungen halten.",
            "<b>Ästhetisches Auge</b> — sieht Schönheit überall.",
            "<b>Loyalität</b> — wenn sie liebt, hält sie. Auch durch Schweres.",
            "<b>Verantwortungsgefühl</b> — übernimmt, ohne dass es gesagt werden muss.",
            "<b>Wärme</b> — Menschen fühlen sich in ihrer Nähe gehalten.",
            "<b>Intuition für andere</b> — spürt, was jemand braucht, bevor er es sagt.",
        ],
        "schatten": [
            "<b>Selbst-Aufopferung</b> — gibt, bis nichts mehr da ist.",
            "<b>Co-Abhängigkeit</b> — hält Partner fest, die nicht guttun.",
            "<b>„Retter“-Syndrom</b> — sucht Menschen, die sie „heilen“ muss.",
            "<b>Perfektionismus</b> — wenn das Zuhause nicht stimmt, stimmt nichts.",
            "<b>Kontrolle als Liebe getarnt</b> — „ich tu das nur für dich“.",
            "<b>Verlust-Angst</b> — fürchtet Trennung mehr als jede andere Zahl.",
        ],
        "berufung": (
            "Die 6 lebt von Beziehung. Klassische Berufungen: Familie, Pädagogik, Pflege, Therapie, Design, "
            "Innenarchitektur, Kunst mit Mensch-Bezug, Ernährung, Schönheit (Mode, Kosmetik), "
            "Beratungsberufe. Auch Eltern-Sein ist für die 6 eine vollwertige Berufung."
        ),
        "geld": (
            "Die 6 verdient Geld über Wärme und Vertrauen. Sie hat oft Schwierigkeiten, Preise hoch genug "
            "anzusetzen — weil sie ihre Sorgearbeit für selbstverständlich hält. Heilung: erkennen, dass "
            "ihre Präsenz einen echten Wert hat."
        ),
        "körper": (
            "Klassische 6er-Themen: <b>Hals/Herz</b> (Liebe blockiert?), <b>Schilddrüse</b> (Stimme zugehalten?), "
            "<b>Hüfte/Becken</b> (Verantwortung für andere zu lange getragen)."
        ),
        "beziehungen": (
            "Die 6 ist die Beziehungs-Expertin schlechthin — und auch die anfälligste für ungesunde "
            "Muster. Eine reife 6 lernt: <b>sich selbst zu lieben ist nicht egoistisch, es ist die Bedingung "
            "für gesunde Liebe zu anderen.</b>"
        ),
        "falle": (
            "Zu glauben, dass Lieben heißt, sich selbst zu vergessen. Eine 6, die sich selbst nicht mehr "
            "wahrnimmt, kann auch andere nicht wirklich wahrnehmen — sie produziert nur noch Fürsorge "
            "als Reflex."
        ),
    },
    7: {
        "tagline": "Innenwelt · Wahrheit · Studium",
        "intro": (
            "Die 7 ist die <b>Zahl der Mystik und der Wahrheit</b>. Sie ist die einsamste der Zahlen — "
            "nicht weil sie keine Menschen mag, sondern weil sie tiefer schaut, als die meisten ertragen. "
            "In Mankevichs Lesart ist sie die Zahl der Forscher:innen, Mystiker:innen, Therapeut:innen, "
            "Wissenschaftler:innen, Mönche, Künstler:innen mit metaphysischem Anspruch."
        ),
        "kernthema": (
            "Die 7 ist hier, um <b>die Wahrheit hinter den Dingen zu finden</b>. Sie lernt nicht durch "
            "Aktivität, sondern durch Rückzug, Beobachtung, Stille. Eine 7, die zu lange im Lärm bleibt, "
            "verliert ihre Klarheit — sie braucht Einsamkeit wie andere Sauerstoff."
        ),
        "stärken": [
            "<b>Tiefe</b> — sieht, was andere übersehen.",
            "<b>Intuition</b> — weiß Dinge, ohne sie hergeleitet zu haben.",
            "<b>Forschungsdrang</b> — gibt nicht auf, bis das Muster sichtbar ist.",
            "<b>Innere Ruhe</b> — kann in Stille existieren, ohne Reize zu brauchen.",
            "<b>Authentizität</b> — kann Lügen nicht lange aushalten, weder eigene noch fremde.",
            "<b>Lehrer:in-Qualität</b> — wenn sie spricht, hört man hin.",
        ],
        "schatten": [
            "<b>Isolation</b> — zieht sich zu weit zurück, verliert Anschluss.",
            "<b>Zynismus</b> — Tiefe ohne Mitgefühl wird kalt.",
            "<b>Überheblichkeit</b> — fühlt sich „über“ den anderen, weil sie mehr sieht.",
            "<b>Realitätsflucht</b> — verschwindet in Theorie, Studium, Meditation.",
            "<b>Misstrauen</b> — sieht hinter allem ein Motiv.",
            "<b>Depression</b> — wenn der Sinn fehlt, kollabiert das System.",
        ],
        "berufung": (
            "Die 7 lebt von Tiefe. Klassische Berufungen: Wissenschaft, Forschung, Therapie, Psychoanalyse, "
            "Philosophie, Religion, Spiritualität, ernsthafte Kunst (Literatur, klassische Musik, "
            "Bildhauerei), Investigationsjournalismus."
        ),
        "geld": (
            "Die 7 verdient Geld schwer — sie hat oft eine Hemmung, ihre Tiefe zu vermarkten. Heilung: "
            "erkennen, dass Wahrheit ein <i>Produkt</i> sein darf, das andere brauchen. Eine 7, die das "
            "begreift, wird gut bezahlt."
        ),
        "körper": (
            "Klassische 7er-Themen: <b>Nervensystem</b> (Reizüberflutung), <b>Kopfschmerzen</b> (zu viel "
            "denken), <b>Verdauung</b> (Sensibilität gegen Umweltgifte)."
        ),
        "beziehungen": (
            "Die 7 ist im Beziehungsleben schwer fassbar. Sie braucht Partner, die ihre Stille-Bedürfnisse "
            "nicht persönlich nehmen. Heilung: die 7 lernt, ihre Rückzüge zu benennen statt zu praktizieren."
        ),
        "falle": (
            "Zu glauben, dass Wahrheit ohne Liebe Tiefe ist. Eine 7 ohne Herz ist nur kalt. Eine 7 mit "
            "Herz ist Magie."
        ),
    },
    8: {
        "tagline": "Manifestation · Macht · materielle Vollendung",
        "intro": (
            "Die 8 ist im numerologischen System die <b>Zahl der Manifestation</b>. Ihr Symbol ist die "
            "liegende Acht — Unendlichkeit, Kreislauf, ewiges Geben und Empfangen. In Mankevichs Lesart "
            "ist sie die Zahl der Unternehmer:innen, Architekt:innen, Investor:innen, Imperien-Bauer:innen — "
            "von Elon Musk bis Coco Chanel."
        ),
        "kernthema": (
            "Die 8 ist hier, um <b>etwas Bleibendes zu errichten</b>. Sie lernt nicht durch Theorie, "
            "sondern durch das, was sie selbst aufbaut, verliert und wieder aufbaut. Eine 8, die nie "
            "gefallen ist, ist meistens nicht wirklich 8 geworden."
        ),
        "stärken": [
            "<b>Strategische Klarheit</b> — sieht Systeme und Hebel schneller als andere.",
            "<b>Resilienz</b> — Rückschläge werden zu Brennstoff.",
            "<b>Magnetismus für Ressourcen</b> — Geld und Menschen folgen einer klaren 8.",
            "<b>Verantwortung tragen</b> — die einzige Zahl, die mit Last gut umgehen kann.",
            "<b>Langer Atem</b> — wo andere bei Jahr 3 aufgeben, fängt sie an.",
            "<b>Doppelpolarität</b> — kann gleichzeitig Visionär:in und Buchhalter:in sein.",
        ],
        "schatten": [
            "<b>Kontrollzwang</b> — wer loslässt, verliert; wer hält, erstickt.",
            "<b>Workaholismus</b> — Identität verschmilzt mit Output.",
            "<b>Härte</b> — gegen sich selbst zuerst, gegen andere als logische Folge.",
            "<b>Geld als Maßstab</b> — Selbstwert hängt an Kontoständen.",
            "<b>Beziehungs-Verdünnung</b> — Menschen werden zu „Funktionen“.",
            "<b>Körper-Kollaps</b> — Schlaf, Verdauung, Rücken zahlen die Rechnung.",
        ],
        "berufung": (
            "Die 8 ist nicht hier, um angestellt zu sein. Sie ist hier, um etwas zu <b>führen</b> — eine "
            "Firma, ein Team, eine Bewegung, ein Werk. Klassische Berufungen: Unternehmer:in, Investor:in, "
            "CEO, Architekt:in, Bauträger:in, Verleger:in, Anwalt/Anwältin, Strategieberatung, Politik."
        ),
        "geld": (
            "Die 8 ist die einzige Zahl, die Geld nicht als Tabu, sondern als Energie versteht. Sie kann "
            "sehr reich werden — oft mehrfach, mit Verlusten dazwischen. <b>Geld ist Wirkung, nicht Wert.</b> "
            "Wer das kapiert, wird reich und frei. Wer es verwechselt, wird reich und leer."
        ),
        "körper": (
            "Klassische 8er-Themen: <b>Rücken</b> (Last), <b>Verdauung</b> (Kontrolle), <b>Schlaf</b> "
            "(Abschalten), <b>Nervensystem</b> (Dauerspannung). Krafttraining stabilisiert, Ausdauer leert "
            "den Druck-Tank, Atemarbeit öffnet das System."
        ),
        "beziehungen": (
            "Die 8 wirkt im Beruf oft härter als sie privat ist. Sie braucht jemanden, der sie nicht mehr "
            "„performen“ lässt, wenn die Tür zu ist. Heilung: in der Beziehung lernen, "
            "<b>nicht nützlich, sondern anwesend zu sein.</b>"
        ),
        "falle": (
            "Zu glauben, dass das Außen die Frage des Innen beantworten kann. Die 8 baut Imperien, um "
            "zu beweisen, dass sie sicher ist — aber Sicherheit kommt nicht von außen."
        ),
    },
    9: {
        "tagline": "Vollendung · Weisheit · alte Seele",
        "intro": (
            "Die 9 ist die <b>letzte einstellige Zahl</b> — sie hat alle anderen Zahlen (1-8) bereits in "
            "sich. Deshalb gilt sie als „alte Seele“. Menschen mit 9 wirken oft seltsam reif für ihr Alter, "
            "haben einen weiten Blick und ein natürliches Gespür für das große Ganze."
        ),
        "kernthema": (
            "Die 9 ist hier, um <b>etwas zu vollenden — nicht zu beginnen</b>. Sie schließt Kreise, "
            "übersetzt zwischen Welten (Generationen, Kulturen, Disziplinen) und hat ein humanitäres "
            "Grundinteresse: ihr Leben soll für etwas Größeres gewesen sein."
        ),
        "stärken": [
            "<b>Visionäres Sehen</b> — erkennt Muster, lange bevor andere sie verstehen.",
            "<b>Empathie ohne Übergriff</b> — kann halten, ohne zu retten.",
            "<b>Natürliche Autorität</b> — muss nicht laut sein, um gehört zu werden.",
            "<b>Lehrer:in-Energie</b> — andere kommen mit ihren Fragen wie von selbst.",
            "<b>Loslassen</b> — kann gehen, wenn etwas vorbei ist.",
            "<b>Großmut</b> — verzeiht überraschend schnell.",
        ],
        "schatten": [
            "<b>Selbst-Aufopferung</b> — gibt, bis nichts mehr da ist, und nennt das Berufung.",
            "<b>Schwere</b> — trägt das Leid der Welt unsichtbar mit.",
            "<b>Idealismus</b> — leidet daran, dass die Welt nicht ist, wie sie sollte.",
            "<b>Einsamkeit</b> — Menschen finden sie inspirierend, selten ebenbürtig.",
            "<b>Spirituelle Überheblichkeit</b> — Hochmut hinter Demut.",
            "<b>Vergangenheits-Verstrickung</b> — hängt an Themen fest, die zu Ende sind.",
        ],
        "berufung": (
            "Die 9 ist hier, um <b>Spuren zu hinterlassen</b>. Klassische Berufungen: Lehre, Therapie, "
            "Spiritualität, Humanitäre Arbeit, Diplomatie, Verlagswesen, Forschung, Mentorenschaft, "
            "Kunst mit Sinn (nicht nur mit Form)."
        ),
        "geld": (
            "Die 9 hat eine schwierige Beziehung zu Geld — sie traut sich oft nicht, „banale“ Wünsche "
            "zu haben. Heilung: erkennen, dass materielle Sicherheit nicht im Widerspruch zur Mission "
            "steht, sondern Voraussetzung dafür."
        ),
        "körper": (
            "Klassische 9er-Themen: <b>Immunsystem</b> (offene Antenne für die Welt), <b>Müdigkeit</b> "
            "(trägt zu viel), <b>Herz</b> (Mitgefühl ohne Grenze)."
        ),
        "beziehungen": (
            "Die 9 liebt tief und großzügig — und sucht oft Partner, die sie „bilden“ kann. Heilung: "
            "die 9 lernt, dass Augenhöhe nicht Pädagogik ist."
        ),
        "falle": (
            "Zu glauben, dass alle Wesen schon Bewusstsein wie sie haben sollten. Die 9 muss lernen, "
            "dass jeder seinen eigenen Weg geht — auch wenn er kürzer aussieht als ihrer."
        ),
    },
}


# =======================================================================
# SEELENZAHL — Tiefenporträt + Kombinations-Logik mit der Lebenszahl
# Die Seelenzahl-Beschreibung überschneidet sich inhaltlich mit der
# Lebenszahl-Beschreibung. Wir nehmen denselben Content-Block, aber
# beschreiben den "inneren Antrieb" statt der "Mission".
# =======================================================================

SEELENZAHL_KERN = {
    1: (
        "Innerlich willst du <b>eigenständig sein</b>, deinen Weg gehen, nicht in fremden Strukturen "
        "untergehen. Das ist nicht Stolz, das ist Code: deine Seele liest „lebendig“ als „autonom“."
    ),
    2: (
        "Innerlich willst du <b>verbunden sein</b>, in Augenhöhe, in Resonanz. Deine Seele lebt von "
        "Beziehung — nicht von Symbiose, sondern von echter, zweistimmiger Verbindung."
    ),
    3: (
        "Innerlich willst du <b>gesehen werden</b> — nicht als Show, sondern als du. Deine Seele "
        "spielt, gestaltet, erzählt; sie wird müde, wenn sie sich verstecken muss."
    ),
    4: (
        "Innerlich willst du <b>etwas Solides bauen</b>. Deine Seele liebt Beständigkeit, Handwerk, "
        "Routinen, die halten. Was du anpackst, soll Spuren hinterlassen."
    ),
    5: (
        "Innerlich willst du <b>frei sein</b>. Deine Seele atmet, wenn neue Welten aufmachen — neue "
        "Orte, neue Menschen, neue Möglichkeiten. Stillstand ist für dich kleines Sterben."
    ),
    6: (
        "Innerlich willst du <b>lieben und Schönheit erschaffen</b>. Deine Seele lebt von Beziehung, "
        "von Heim, von Verantwortung für Menschen, die du wirklich liebst."
    ),
    7: (
        "Innerlich willst du <b>die Wahrheit hinter den Dingen verstehen</b>. Deine Seele zieht sich "
        "regelmäßig zurück, um zu sehen, was unter der Oberfläche eigentlich passiert."
    ),
    8: (
        "Innerlich willst du <b>Wirkung haben</b>. Deine Seele liest „bedeutend“ als „lebendig“. "
        "Sie kann sich nicht mit einer Statisten-Rolle zufriedengeben."
    ),
    9: (
        "Innerlich willst du <b>Spuren hinterlassen</b>. Deine Seele trägt einen Auftrag — ein „warum“, "
        "das größer ist als dein eigenes Leben. Sie kann nicht „nur“ glücklich sein, sie will Sinn."
    ),
}


# Generische Variante A/B/C-Beschreibung für die Kombination zweier Zahlen
def kombi_variants(lz: int, sz: int) -> dict:
    """Liefert Variante A (Lebenszahl dominiert), B (Seele dominiert) und C (Integration)."""
    lz_label = LEBENSZAHL_LABEL.get(lz, "Lebenszahl")
    sz_label = SEELENZAHL_LABEL.get(sz, "Seele")
    if lz == sz:
        return {
            "intro": (
                f"Lebenszahl und Seelenzahl sind beide die <b>{lz}</b>. Das ist eine seltene Verdoppelung: "
                f"deine Mission und dein innerer Antrieb laufen in dieselbe Richtung. Vorteil: enorme "
                f"Klarheit. Nachteil: kein eingebauter Gegenpol — du musst dir Vielfalt aktiv ins Leben holen."
            ),
            "a": (
                f"<b>Variante A — Überdosis {lz_label}.</b> Du lebst die {lz} so kompromisslos, dass kein "
                f"Raum für andere Energien bleibt. Das wirkt nach außen extrem klar, fühlt sich innen aber "
                f"eng an."
            ),
            "b": (
                f"<b>Variante B — Verleugnung.</b> Du spürst die doppelte {lz}-Wucht und versuchst, sie "
                f"abzudämpfen, dich anzupassen. Das macht dich müde, weil du deine Hauptenergie "
                f"unterdrückst."
            ),
            "c": (
                f"<b>Variante C — Integration.</b> Du lebst die {lz} bewusst und holst dir gleichzeitig "
                f"komplementäre Energien (über Partner, Mentoren, Hobbies). Innen Linie, außen Bandbreite."
            ),
        }
    return {
        "intro": (
            f"Das ist die <b>entscheidende Spannung deines Codes</b>. Die {lz} ({lz_label}) zieht in eine "
            f"Richtung, die {sz} ({sz_label}) in eine andere. Beide sind echt, beide wollen gelebt werden."
        ),
        "a": (
            f"<b>Variante A — die {lz} dominiert.</b> Du folgst dem äußeren Auftrag ({lz_label}) so stark, "
            f"dass die innere Stimme ({sz_label}) verstummt. Funktioniert eine Weile, kollabiert irgendwann "
            f"über Sinnkrise, Gesundheit oder Beziehung."
        ),
        "b": (
            f"<b>Variante B — die {sz} dominiert.</b> Du gibst der inneren Stimme ({sz_label}) den Vortritt "
            f"und lebst nicht deine Mission ({lz_label}). Die {lz} rächt sich später über Frust, Ungeduld, "
            f"das Gefühl „etwas verpasst zu haben“."
        ),
        "c": (
            f"<b>Variante C — Integration.</b> Du baust dein Leben so, dass deine Mission ({lz_label}) "
            f"<i>durch</i> deine innere Wahrheit ({sz_label}) gelebt wird. Dann werden beide stärker, statt "
            f"sich gegenseitig zu kannibalisieren."
        ),
    }


LEBENSZAHL_LABEL = {
    1: "Pionierin",  2: "Vermittlerin", 3: "Künstlerin",  4: "Bauherrin",
    5: "Reisende",   6: "Liebende",     7: "Forscherin",  8: "Bauherrin der Imperien",
    9: "Lehrerin",
}

SEELENZAHL_LABEL = {
    1: "Autonomie-Seele", 2: "Beziehungs-Seele", 3: "Ausdrucks-Seele", 4: "Struktur-Seele",
    5: "Freiheits-Seele", 6: "Herz-Seele",       7: "Wahrheits-Seele", 8: "Wirkungs-Seele",
    9: "Sinn-Seele",
}


# =======================================================================
# PERSÖNLICHKEITSZAHL — wie du nach außen wirkst (Monat)
# =======================================================================

PERSOENLICHKEIT_CONTENT = {
    1: {
        "tagline": "Auftritt · Eigenständigkeit · der erste Eindruck",
        "intro": (
            "Die 1 in der Persönlichkeit macht dich sofort als jemanden lesbar, der seinen eigenen Weg "
            "geht. Andere lesen Bestimmtheit, Klarheit, Selbst-Standigkeit in deinem ersten Eindruck — "
            "und reagieren entsprechend (mit Respekt oder mit Konkurrenz)."
        ),
        "stärken": [
            "<b>Sofortige Sichtbarkeit</b> — du wirst im Raum wahrgenommen.",
            "<b>Glaubwürdigkeit</b> — wenn du sprichst, hören Leute hin.",
            "<b>Magnetismus für andere Pioniere</b> — du ziehst Macher:innen an.",
            "<b>Schnelle Eskalation</b> — du rutschst leicht in Führungsrollen.",
        ],
        "schatten": [
            "<b>Distanz</b> — wirkst kühler als du bist.",
            "<b>Erwartungslast</b> — Leute halten dich für reifer als du dich fühlst.",
            "<b>Übersehen werden in Teams</b> — als Solo gelesen, nicht eingeladen.",
            "<b>Schwer fassbar</b> — andere wissen nicht, wer du wirklich bist.",
        ],
    },
    2: {
        "tagline": "Sanftheit · Empathie · der ruhige Anker",
        "intro": (
            "Die 2 in der Persönlichkeit macht dich nach außen weich, offen, zugänglich. Du wirkst "
            "vertrauenswürdig auf den ersten Blick, Menschen öffnen sich schnell — was Vorteile (hohe "
            "soziale Resonanz) und Risiken (man unterschätzt deine Klarheit) hat."
        ),
        "stärken": [
            "<b>Vertrauensvorschuss</b> — Menschen erzählen dir Dinge.",
            "<b>Diplomatie</b> — du wirkst nicht angreifbar, aber präsent.",
            "<b>Empathie</b> — du spürst Stimmungen, bevor sie ausgesprochen sind.",
            "<b>Brückenfunktion</b> — du wirst zwischen Welten platziert.",
        ],
        "schatten": [
            "<b>Unterschätzt-Werden</b> — Leute halten dich für nett, nicht für stark.",
            "<b>Konfliktvermeidung</b> — wirkst weicher als du innerlich bist.",
            "<b>Ausgenutzt-Werden</b> — Vertrauen kann missbraucht werden.",
            "<b>Schwer „nein“ sagen</b> — dein Auftritt lädt zum Bitten ein.",
        ],
    },
    3: {
        "tagline": "Charme · Kreativität · Sichtbarkeit",
        "intro": (
            "Die 3 in der Persönlichkeit macht dich charmant, kreativ, sprachgewandt, kontaktfreudig. "
            "Du wirkst leichter und spielerischer als deine inneren Themen vermuten ließen — und das "
            "ist deine geheime Stärke."
        ),
        "stärken": [
            "<b>Soziale Brillanz</b> — du veränderst die Stimmung im Raum.",
            "<b>Humor</b> — du löst Spannung mit einem Satz auf.",
            "<b>Ästhetisches Gespür</b> — du weißt, was wirkt.",
            "<b>Charme</b> — Menschen vertrauen dir schnell.",
        ],
        "schatten": [
            "<b>Maskerade</b> — niemand merkt, wenn es dir schlecht geht.",
            "<b>Anerkennungs-Hunger</b> — du brauchst das „Gesehen-Werden“ mehr als zugegeben.",
            "<b>Oberflächlichkeit-Vorwurf</b> — andere unterschätzen dich.",
            "<b>Konfliktvermeidung</b> — du lachst Probleme weg, statt sie zu benennen.",
        ],
    },
    4: {
        "tagline": "Bodenständigkeit · Verlässlichkeit · klare Kante",
        "intro": (
            "Die 4 in der Persönlichkeit macht dich nüchtern, sachlich, geerdet. Du wirkst älter und "
            "reifer als dein Alter — Menschen vertrauen dir Geld, Geheimnisse, Projekte an, ohne dass "
            "du dafür groß werben musst."
        ),
        "stärken": [
            "<b>Verlässlichkeit</b> — was du sagst, gilt.",
            "<b>Glaubwürdigkeit</b> — Menschen geben dir Verantwortung.",
            "<b>Geerdetheit</b> — auch in Krisen wirkst du ruhig.",
            "<b>Diskretion</b> — du wirkst wie jemand, dem man etwas anvertrauen kann.",
        ],
        "schatten": [
            "<b>Verschlossen wirken</b> — Leute trauen sich nicht, dich zu fragen.",
            "<b>Steif</b> — wirkst manchmal älter/strenger als nötig.",
            "<b>Humorlos</b> — die 4er-Kanten wirken im Alltag oft trocken.",
            "<b>Unnahbar</b> — Menschen lesen dich als „abgeschlossen“.",
        ],
    },
    5: {
        "tagline": "Freiheit · Bewegung · Wandel",
        "intro": (
            "Die 5 in der Persönlichkeit macht dich beweglich, kontaktfreudig, neugierig, schwer "
            "einzufangen. Du wirkst jünger und freier als deine inneren Themen vermuten ließen."
        ),
        "stärken": [
            "<b>Schnelle Auffassung</b> — du verstehst Menschen in Sekunden.",
            "<b>Kommunikation</b> — du kannst in jeder Schicht andocken.",
            "<b>Mut</b> — du entscheidest schnell.",
            "<b>Anziehung</b> — Menschen wollen mit dir Zeit verbringen.",
        ],
        "schatten": [
            "<b>Sprunghaftigkeit</b> — Leute wissen nicht, ob sie auf dich zählen können.",
            "<b>Oberflächlichkeit</b> — wirkst manchmal flüchtiger als du bist.",
            "<b>Bindungsangst</b> — andere lesen Distanz, wo Schutz ist.",
            "<b>Unzuverlässigkeits-Vorwurf</b> — auch wenn du es ernst meinst.",
        ],
    },
    6: {
        "tagline": "Wärme · Fürsorge · der einladende Auftritt",
        "intro": (
            "Die 6 in der Persönlichkeit macht dich warm, einladend, fürsorglich. Menschen fühlen sich "
            "in deiner Nähe gehalten — das ist eine der angenehmsten ersten Eindrücke überhaupt."
        ),
        "stärken": [
            "<b>Wärme</b> — Menschen entspannen sich in deiner Nähe.",
            "<b>Vertrauen</b> — Leute öffnen sich dir.",
            "<b>Ästhetische Wirkung</b> — du wirkst gepflegt, harmonisch.",
            "<b>Glaubwürdigkeit als Fürsorgliche:r</b> — du wirst um Rat gefragt.",
        ],
        "schatten": [
            "<b>Übernahme von Verantwortung</b> — Leute laden dir ihre Themen ab.",
            "<b>Wirkst nett, nicht stark</b> — Konkurrenz unterschätzt dich.",
            "<b>Schwer Grenzen ziehen</b> — dein Auftritt lädt zum Bitten ein.",
            "<b>Idealisiert werden</b> — Erwartung der „guten Mutter“/„guten Beraters“.",
        ],
    },
    7: {
        "tagline": "Tiefe · Stille · der nachdenkliche Auftritt",
        "intro": (
            "Die 7 in der Persönlichkeit macht dich nach außen still, reflektiert, tiefgründig. Du "
            "wirkst älter und weiser als dein Alter — manche fühlen sich davon angezogen, andere "
            "fühlen sich davon eingeschüchtert."
        ),
        "stärken": [
            "<b>Glaubwürdige Tiefe</b> — du wirkst wie jemand, der weiß.",
            "<b>Beobachtungsgabe</b> — andere fühlen sich von dir gesehen.",
            "<b>Authentizität</b> — du wirkst nicht performt.",
            "<b>Wirkung in Eins-zu-Eins-Situationen</b> — Menschen öffnen sich dir.",
        ],
        "schatten": [
            "<b>Unnahbar wirken</b> — Leute trauen sich nicht.",
            "<b>Distanz lesen lassen</b> — auch wenn du nur nachdenkst.",
            "<b>Schwer in Gruppen</b> — Smalltalk fühlt sich falsch an.",
            "<b>Als arrogant gelesen werden</b> — weil du wenig sagst.",
        ],
    },
    8: {
        "tagline": "Autorität · Manifestation · der mächtige Auftritt",
        "intro": (
            "Die 8 in der Persönlichkeit macht dich nach außen autoritativ, zielgerichtet, ernsthaft. "
            "Menschen lesen sofort: hier ist jemand, der weiß, was er/sie will. Das öffnet Türen — "
            "und erzeugt manchmal auch Angst."
        ),
        "stärken": [
            "<b>Natürliche Autorität</b> — du wirst ernst genommen, sofort.",
            "<b>Glaubwürdigkeit in Geld-Themen</b> — du wirkst wie jemand, der manifestiert.",
            "<b>Klare Führung</b> — Teams wissen, wo sie mit dir dran sind.",
            "<b>Eindruck von Stabilität</b> — auch in Krisen.",
        ],
        "schatten": [
            "<b>Einschüchterung</b> — Menschen wagen nicht, dich anzusprechen.",
            "<b>Unzugänglich</b> — wirkst „über“ den anderen.",
            "<b>Härte</b> — wirkst kühler als du bist.",
            "<b>Erwartungslast</b> — Leute halten dich für reicher/mächtiger als du bist.",
        ],
    },
    9: {
        "tagline": "Weisheit · Mission · der missionarische Auftritt",
        "intro": (
            "Die 9 in der Persönlichkeit macht dich nach außen weise, getragen, mit einem leichten "
            "missionarischen Zug. Du wirkst älter als dein Alter und trägst eine sichtbare „Bedeutung“ "
            "mit dir — manche fühlen sich angezogen, andere meiden das."
        ),
        "stärken": [
            "<b>Glaubwürdigkeit als Lehrer:in</b> — auch wenn du nichts erklärst.",
            "<b>Anziehung für Sinn-Suchende</b> — Menschen fragen dich nach Rat.",
            "<b>Natürliche Autorität ohne Härte</b> — du musst nicht laut sein.",
            "<b>Großzügiger Eindruck</b> — du wirkst nicht kleinkariert.",
        ],
        "schatten": [
            "<b>Spirituelle Überhöhung</b> — wirkst manchmal „abgehoben“.",
            "<b>Schwere</b> — die Aura kann erdrückend sein.",
            "<b>Schwer fassbar im Alltag</b> — Leute wissen nicht, wie sie dich „behandeln“ sollen.",
            "<b>Erwartung der Weisheit</b> — auch wenn du gerade einfach müde bist.",
        ],
    },
}


# =======================================================================
# AUSDRUCKSZAHL — wie deine Wirkung in der Welt landet (Jahr)
# =======================================================================

AUSDRUCK_CONTENT = {
    1: {
        "tagline": "Pionier-Wirkung · Eigenständigkeit · „Ich war hier“",
        "intro": (
            "Die 1 in der Ausdruckszahl bedeutet: du hinterlässt einen pionierhaften Eindruck. Andere "
            "beschreiben dich als „selbstständig“, „die/der ihr/sein Ding macht“. Was du tust, hat eine "
            "Handschrift."
        ),
        "stärken": [
            "<b>Klare Linie</b> — was du tust, ist wiedererkennbar.",
            "<b>Autorität</b> — du wirst schnell zur Anlaufstelle.",
            "<b>Inspirationswirkung</b> — andere trauen sich, weil sie dich sehen.",
            "<b>Selbstmarke</b> — du bist eine Aussage, nicht nur ein Mensch.",
        ],
        "schatten": [
            "<b>Wirkst größer als du dich fühlst</b> — Erwartungslast, die du nicht erbeten hast.",
            "<b>Schwer zu folgen</b> — andere wissen nicht, ob sie mitkönnen.",
            "<b>Konkurrenz-Magnet</b> — du ziehst Menschen an, die sich messen wollen.",
            "<b>Einsamkeit auf dem eigenen Weg</b>.",
        ],
    },
    2: {
        "tagline": "Verbindende Wirkung · Resonanz · Brücke",
        "intro": (
            "Die 2 in der Ausdruckszahl bedeutet: deine Wirkung in der Welt ist verbindend, "
            "vermittelnd, sanft. Menschen erinnern dich als jemanden, durch den etwas zusammenkam — "
            "ein Projekt, eine Beziehung, eine Lösung."
        ),
        "stärken": [
            "<b>Brücken bauen</b> — du verbindest, was sonst getrennt bliebe.",
            "<b>Glaubwürdigkeit in heiklen Themen</b> — du wirkst neutral, ohne kalt zu sein.",
            "<b>Mehr Wirkung, als du selber siehst</b> — du beeinflusst leise.",
            "<b>Treuer Wert in Teams</b> — Gruppen funktionieren mit dir besser.",
        ],
        "schatten": [
            "<b>Wirst übersehen</b> — deine leise Wirkung wird nicht zugeschrieben.",
            "<b>Wenig sichtbare „Marke“</b> — schwerer im Selbstmarketing.",
            "<b>Empfindlich gegen Ungerechtigkeit</b> — du trägst die Ungleichgewichte mit.",
        ],
    },
    3: {
        "tagline": "Kreative Wirkung · Sichtbarkeit · Sprache",
        "intro": (
            "Die 3 in der Ausdruckszahl bedeutet: deine Wirkung landet kreativ, kommunikativ, "
            "charismatisch. Du kannst komplexe Dinge einfach machen — Gold wert in Vertrieb, Marketing, "
            "Führung, Bühne."
        ),
        "stärken": [
            "<b>Sprachgefühl</b> — du findest den Satz, der ankommt.",
            "<b>Charisma</b> — du ziehst Räume auf dich.",
            "<b>Humor als Werkzeug</b> — du entwaffnest Spannung mit Leichtigkeit.",
            "<b>Storytelling</b> — du erzählst Visionen so, dass Leute mitgehen.",
        ],
        "schatten": [
            "<b>Anerkennungs-Hunger</b> — die 3 will gesehen werden.",
            "<b>Selbstdarstellung</b> — Substanz wird zur Fassade.",
            "<b>Vermeidung von Tiefe</b> — über Schmerz Witze machen.",
            "<b>Zerstreuung</b> — viele Felder, wenig Tiefe.",
        ],
    },
    4: {
        "tagline": "Strukturelle Wirkung · Verlässlichkeit · Bau",
        "intro": (
            "Die 4 in der Ausdruckszahl bedeutet: deine Wirkung in der Welt ist strukturell. Du baust "
            "Dinge, die nach dir noch da sind — Systeme, Häuser, Firmen, Bücher, Methoden."
        ),
        "stärken": [
            "<b>Verlässlichkeit als Marke</b> — Menschen erinnern sich an dich als „die/der, der es macht“.",
            "<b>Architektur-Sinn</b> — du baust Strukturen, die halten.",
            "<b>Langfrist-Wirkung</b> — deine Spur ist nicht spektakulär, aber dauerhaft.",
            "<b>Glaubwürdigkeit in komplexen Themen</b> — du wirkst zuverlässig.",
        ],
        "schatten": [
            "<b>Schwer sichtbar</b> — deine Wirkung wird nicht zugeschrieben.",
            "<b>Nüchterner Eindruck</b> — wirkst sachlicher, als du bist.",
            "<b>Wenig „Glanz“</b> — bekommst nicht den Applaus, den deine Arbeit verdient.",
        ],
    },
    5: {
        "tagline": "Bewegliche Wirkung · Vielseitigkeit · Wandel",
        "intro": (
            "Die 5 in der Ausdruckszahl bedeutet: deine Wirkung in der Welt ist beweglich, vielfältig, "
            "wandelbar. Du fällst auf, weil du in vielen Welten zu Hause bist und überall andockst."
        ),
        "stärken": [
            "<b>Vielseitigkeit</b> — du wirkst kompetent in vielen Feldern.",
            "<b>Sprach- und Kulturbrücken</b> — du verbindest, was geographisch getrennt ist.",
            "<b>Vertrieblicher Eindruck</b> — Menschen kaufen von dir.",
            "<b>Frische</b> — du wirkst nie verstaubt.",
        ],
        "schatten": [
            "<b>Schwer einordbar</b> — Leute wissen nicht, wofür du stehst.",
            "<b>Unverbindlich-Vorwurf</b> — wirkst sprunghaft.",
            "<b>Keine klare Marke</b> — schwer für Karriere und Geld.",
        ],
    },
    6: {
        "tagline": "Verbindende Wirkung · Wärme · Heim",
        "intro": (
            "Die 6 in der Ausdruckszahl bedeutet: deine Wirkung in der Welt ist warm, fürsorglich, "
            "heimat-bildend. Menschen erinnern dich als jemanden, durch den sie sich gehalten gefühlt "
            "haben."
        ),
        "stärken": [
            "<b>Wärme als Eindruck</b> — du wirkst zugewandt.",
            "<b>Vertrauen schenken</b> — Menschen vertrauen dir sofort.",
            "<b>Ästhetik</b> — was du tust, ist auch schön.",
            "<b>Gemeinschaftsbildende Wirkung</b> — Gruppen finden bei dir Anker.",
        ],
        "schatten": [
            "<b>Wirkst wie eine „gute Mutter“/„guter Vater“</b> — auch wenn du jemand anderes sein willst.",
            "<b>Wirst um Hilfe gebeten</b> — auch wenn du selber Hilfe brauchst.",
            "<b>Idealisiert werden</b> — Erwartungen, denen du nicht entkommen kannst.",
        ],
    },
    7: {
        "tagline": "Tiefe Wirkung · Wahrheit · Stille",
        "intro": (
            "Die 7 in der Ausdruckszahl bedeutet: deine Wirkung in der Welt ist tief, ruhig, "
            "wahrheitsorientiert. Du hinterlässt einen Eindruck von Substanz — Menschen merken sich "
            "deine Sätze, weil sie nicht inflationär waren."
        ),
        "stärken": [
            "<b>Glaubwürdigkeit</b> — was du sagst, hat Gewicht.",
            "<b>Wirkung auf Einzelne, nicht auf Massen</b> — du verändert Menschen.",
            "<b>Lehrer:in-Energie</b> — Menschen suchen dich auf, um zu lernen.",
            "<b>Authentizität als Marke</b>.",
        ],
        "schatten": [
            "<b>Schwer skalierbar</b> — deine Wirkung passiert in der Tiefe, nicht in der Breite.",
            "<b>Wenig „Reach“</b> — Massen-Wirkung fühlt sich falsch an.",
            "<b>Als unzugänglich gelesen werden</b>.",
        ],
    },
    8: {
        "tagline": "Manifestations-Wirkung · Macht · Spur",
        "intro": (
            "Die 8 in der Ausdruckszahl bedeutet: deine Wirkung in der Welt ist materiell, sichtbar, "
            "messbar. Du hinterlasst Spuren — Firmen, Gebäude, Bücher, Vermögen, Strukturen, die nach "
            "dir noch da sind."
        ),
        "stärken": [
            "<b>Sichtbare Manifestation</b> — was du anfasst, wird real.",
            "<b>Magnetismus für Ressourcen</b> — Geld, Menschen, Aufträge.",
            "<b>Glaubwürdigkeit in Macht-Fragen</b>.",
            "<b>Skaleneffekte</b> — du wirkst auf Größe, nicht nur auf Einzelne.",
        ],
        "schatten": [
            "<b>Wirkst hart</b> — auch wenn du es nicht bist.",
            "<b>Erzeugst Konkurrenz</b> — andere wollen sich mit dir messen.",
            "<b>Identifizierung mit Output</b> — wer du bist = was du gebaut hast.",
        ],
    },
    9: {
        "tagline": "Vollendende Wirkung · Mission · Spuren",
        "intro": (
            "Die 9 in der Ausdruckszahl bedeutet: deine Wirkung in der Welt ist sinngebend, "
            "abschließend, weise. Du wirst erinnert als jemand, der etwas „rund gemacht“ hat — eine "
            "Generation, eine Geschichte, eine Bewegung."
        ),
        "stärken": [
            "<b>Lehrer:in/Mentor:in-Wirkung</b> — Menschen schauen zu dir auf.",
            "<b>Glaubwürdigkeit in Sinn-Themen</b>.",
            "<b>Langfrist-Wirkung</b> — du wirst nach deinem Tod noch zitiert.",
            "<b>Großzügige Spur</b> — du nimmst, aber gibst mehr zurück.",
        ],
        "schatten": [
            "<b>Schwere</b> — wirkst manchmal getragener als nötig.",
            "<b>Wenig „spielerisches Marketing“</b> — passt nicht zu dir.",
            "<b>Wirst auf den Sockel gestellt</b> — auch wenn du das nicht willst.",
        ],
    },
}


# =======================================================================
# KARMA-ZAHLEN — Erklärungen
# =======================================================================

KARMA_CONTENT = {
    10: {
        "title": "10 — der „Meister-Pionier“",
        "text": (
            "Die 10 verbindet die <b>1 (Ich, Anfang, Wille)</b> mit der <b>0 (göttlicher Aspekt, "
            "unendliches Potenzial)</b>. Sie ist keine „normale“ 1, sondern eine 1 mit Karma-Auftrag: "
            "hier ist jemand, die/der nicht einfach Anfänger:in ist, sondern „wiedergeboren“. Lernaufgabe: "
            "du sollst Neues beginnen, ohne zu glauben, dass es nur dein Verdienst ist. Heilmittel: "
            "Dankbarkeit. Die 10 öffnet sich, wenn du anerkennst, was dir zugekommen ist, nicht nur, "
            "was du geleistet hast."
        ),
    },
    11: {
        "title": "11 — Meisterzahl (Intuition · Antenne)",
        "text": (
            "Die 11 ist eine Meisterzahl: hohe Sensibilität, Intuition, die Fähigkeit, Dinge zu „sehen“, "
            "bevor andere sie verstehen. Wer die 11 im Code hat, trägt eine versteckte Antenne. Risiko: "
            "Reizüberflutung, Nervosität, das Gefühl, „nicht in diese Welt zu passen“."
        ),
    },
    13: {
        "title": "13 — Karma-Zahl der Transformation",
        "text": (
            "Die 13 verbindet die 1 (Ich) mit der 3 (Ausdruck) und reduziert auf 4 (Struktur). Ihre "
            "Lernaufgabe: <b>Wandlung durch Loslassen</b>. Wer die 13 trägt, muss mehrfach im Leben "
            "alte Identitäten sterben lassen, damit etwas Neues entstehen kann. Schatten: an Vergangenem "
            "festhalten, bis es einstürzt."
        ),
    },
    14: {
        "title": "14 — Karma-Zahl der Versuchung/Befreiung",
        "text": (
            "Die 14 verbindet die 1 (Ich) mit der 4 (Struktur) und reduziert auf 5 (Freiheit). Ihre "
            "Lernaufgabe: <b>Befreiung aus selbstgewählten Abhängigkeiten</b> — Sucht, ungesunde "
            "Beziehungen, Konsum. Wer die 14 trägt, muss aktiv lernen, dass Freiheit nicht von außen "
            "kommt."
        ),
    },
    16: {
        "title": "16 — Karma-Zahl der Demut („der Turm“)",
        "text": (
            "Die 16 verbindet die <b>1 (Ego, Wille)</b> mit der <b>6 (Liebe, Verantwortung)</b>. Sie ist "
            "eine der intensivsten Karma-Zahlen, symbolisch verglichen mit dem „Turm“, der einstürzt. "
            "Lernaufgabe: <b>Liebe darf nicht zum Werkzeug des Egos werden</b>. Bindungen, die nur "
            "deinem Bild von dir dienen, kollabieren. Wer die 16 trägt, erlebt mindestens einmal einen "
            "Crash-Moment — eine Beziehung, ein Projekt, eine Identität, die wegbricht. Heilmittel: "
            "ehrlich gegen sich selbst sein, keine Geheimnisse."
        ),
    },
    17: {
        "title": "17 — Karma-Zahl der Macht/Verantwortung",
        "text": (
            "Die 17 verbindet die <b>1 (Pionier)</b> mit der <b>7 (Wahrheit, Tiefe)</b>. Ihre "
            "Lernaufgabe: <b>Macht ohne Wahrheit kollabiert. Erfolg ohne Innerlichkeit isoliert.</b> "
            "Wer die 17 trägt, wird im Leben mehrfach in Positionen kommen, in denen er/sie "
            "Verantwortung über andere hat. Heilmittel: Rückzug-Disziplin, regelmäßig wirklich nichts tun."
        ),
    },
    19: {
        "title": "19 — Karma-Zahl der Ego-Reifung",
        "text": (
            "Die 19 verbindet die <b>1 (Ich, Wille)</b> mit der <b>9 (Vollendung, Sinn)</b>. Ihre "
            "Lernaufgabe: <b>„Ich“ ist nicht „allein“.</b> Erst wenn das Ich seine Verbindung zur "
            "größeren Geschichte versteht, wird es ganz. Die 19 ist die Karma-Zahl der Egozentriker:in-Falle: "
            "sie bekommt eine Lektion, sobald sie glaubt, das Leben drehe sich um sie."
        ),
    },
    22: {
        "title": "22 — Meisterzahl (Baumeister:in)",
        "text": (
            "Die 22 ist die Meisterzahl der großen Manifestation. Wer sie trägt, kann etwas Bleibendes "
            "errichten — eine Institution, eine Bewegung, ein Werk. Schatten: die Last wird zu schwer, "
            "die Person zerbricht an der eigenen Größe."
        ),
    },
    28: {
        "title": "28 — Partnerschaft als Manifestation",
        "text": (
            "Die 28 verbindet die <b>2 (Partnerschaft)</b> mit der <b>8 (Manifestation)</b> und "
            "reduziert auf 10 → 1 (Pionier). Ihre Energie: Solo-Wirkung, die durch Resonanz mit anderen "
            "entsteht. Wer die 28 im Code hat, manifestiert über echte Beziehungen — Co-Founder, "
            "Partnerschaft, Lebensgefährte:in."
        ),
    },
    33: {
        "title": "33 — Meisterzahl (Liebes-Meister:in)",
        "text": (
            "Die 33 ist die höchste Meisterzahl: bedingungslose Liebe, große Lehrenergie, "
            "Heilkraft. Wer sie trägt, ist hier auf einer „Mission“ — meistens spät erkannt."
        ),
    },
    37: {
        "title": "37 — die 3 + 7 als Schwelle",
        "text": (
            "Die 37 ist keine klassische Karma-Zahl, sondern eine eigenwillige Zwischenstufe. Sie "
            "verbindet die 3 (Ausdruck) mit der 7 (Innenwelt) — also Außen und Innen in einer "
            "Schwelle, die meistens zur 10 (Meister-Pionier) reduziert. Wer 37 im Code hat, lebt diese "
            "Schwelle: nach außen kreativ-sichtbar, nach innen tief-wahrheitssuchend."
        ),
    },
}


# =======================================================================
# PERSÖNLICHES JAHR — was bedeutet ein 1er/2er/.../9er Jahr
# =======================================================================

JAHR_CONTENT = {
    1: {
        "tagline": "Neuanfang · Saat · Pionier",
        "text": (
            "Ein 1er-Jahr ist das <b>Startjahr eines neuen 9-Jahres-Zyklus</b>. Klassische Themen: einen "
            "neuen Lebensabschnitt starten, ein neues Projekt anstoßen, eine alte Identität ablegen. "
            "Was in einem 1er-Jahr beginnt, prägt die nächsten 9 Jahre. Es ist <i>nicht</i> die Zeit, "
            "abzuwarten oder zu konsolidieren — dieses Jahr verlangt Initiative."
        ),
        "todo": [
            "<b>Eine neue Sache anstoßen, die in 9 Jahren noch da ist.</b>",
            "<b>Eine alte Identität ablegen.</b> Eine Rolle, die nicht mehr passt.",
            "<b>Mut zum ersten Schritt — auch ohne fertigen Plan.</b>",
        ],
    },
    2: {
        "tagline": "Geduld · Partnerschaft · Reifen",
        "text": (
            "Ein 2er-Jahr ist das <b>Jahr der Partnerschaft, der Sensibilität, der Geduld</b>. Was im "
            "1er-Jahr gesät wurde, will jetzt langsam wachsen. Klassische Themen: Beziehungen vertiefen, "
            "Verträge schließen, in Augenhöhe mit anderen arbeiten, Konflikte diplomatisch klären. "
            "Aggressives Pushen funktioniert nicht — Dinge brauchen Zeit."
        ),
        "todo": [
            "<b>Geduld kultivieren.</b>",
            "<b>Schlüsselbeziehungen vertiefen.</b>",
            "<b>Auf Resonanz statt Kraft setzen.</b>",
        ],
    },
    3: {
        "tagline": "Ausdruck · Kreativität · Freude",
        "text": (
            "Ein 3er-Jahr ist das <b>Jahr der Sichtbarkeit und Kreativität</b>. Klassische Themen: "
            "öffentliche Auftritte, Veröffentlichungen, soziale Sichtbarkeit, kreative Projekte, "
            "neue Freundschaften, viel Spaß. Vorsicht: das 3er-Jahr verleitet zu Oberflächlichkeit "
            "und Zerstreuung — Substanz darf nicht verloren gehen."
        ),
        "todo": [
            "<b>Ein kreatives Projekt nach außen tragen.</b>",
            "<b>Genießen, ohne zu zerstreuen.</b>",
            "<b>Sichtbar werden — nicht als Show, als du selbst.</b>",
        ],
    },
    4: {
        "tagline": "Arbeit · Struktur · Bau",
        "text": (
            "Ein 4er-Jahr ist das <b>Jahr der Arbeit und Struktur</b>. Klassische Themen: bauen, "
            "renovieren, Strukturen schaffen, hart arbeiten, Routinen einführen, Verantwortung "
            "übernehmen. Wenig Glanz, viel Substanz. Wer dieses Jahr ernst nimmt, legt das Fundament "
            "für die nächsten Jahre."
        ),
        "todo": [
            "<b>Einen Bau abschließen — physisch oder strukturell.</b>",
            "<b>Routinen etablieren, die halten.</b>",
            "<b>Geduld mit langsamem Fortschritt.</b>",
        ],
    },
    5: {
        "tagline": "Veränderung · Risiko · Wandel",
        "text": (
            "Ein 5er-Jahr ist das <b>Jahr der Veränderung</b>. Klassische Themen: Umzug, Jobwechsel, "
            "neue Beziehungen, Reisen, mutige Schritte. Was 4 stabilisiert hat, wird in 5 erschüttert. "
            "Das ist gut — Stagnation wird aufgelöst. Vorsicht: nicht alle Veränderungen sind "
            "Verbesserungen, prüfen statt nur springen."
        ),
        "todo": [
            "<b>Etwas Großes verändern, was nicht mehr passt.</b>",
            "<b>Mut zum Risiko — mit Augenmaß.</b>",
            "<b>Beweglich bleiben, auch wenn alles wackelt.</b>",
        ],
    },
    6: {
        "tagline": "Familie · Beziehung · Verantwortung",
        "text": (
            "Ein 6er-Jahr ist das <b>Jahr der Familie und Verantwortung</b>. Klassische Themen: Heirat, "
            "Geburt, Hauskauf, Familienverpflichtungen, Pflege von Beziehungen, ästhetische Projekte. "
            "Kein Jahr für aggressive Expansion — ein Jahr für Konsolidierung, „Haus in Ordnung bringen“, "
            "Beziehung auffüllen."
        ),
        "todo": [
            "<b>Beziehungen und Familie priorisieren.</b>",
            "<b>Das Heim schöner machen — physisch und emotional.</b>",
            "<b>Verantwortung übernehmen, ohne sich zu verlieren.</b>",
        ],
    },
    7: {
        "tagline": "Rückzug · Innenarbeit · Studium",
        "text": (
            "Ein 7er-Jahr ist das <b>Jahr der Innenarbeit</b>. Klassische Themen: Studium, Therapie, "
            "spirituelle Vertiefung, alleine sein, Bücher schreiben, Stille suchen. <i>Nicht</i> das "
            "Jahr für große externe Manifestation — das System sagt: jetzt wird gesammelt, nicht "
            "verschwendet."
        ),
        "todo": [
            "<b>Bewusst Rückzugszeiten einbauen.</b>",
            "<b>Tief in ein Thema einsteigen, das dich wirklich interessiert.</b>",
            "<b>Therapie, Mediation, Tagebuch — alles, was nach innen führt.</b>",
        ],
    },
    8: {
        "tagline": "Manifestation · Geld · Erfolg",
        "text": (
            "Ein 8er-Jahr ist das <b>Jahr der Manifestation und materiellen Sichtbarkeit</b>. Klassische "
            "Themen: Karriere-Sprünge, Geschäftsgründung, Geld-Themen, Investitionen, größere Verträge, "
            "eigener Marktauftritt. Wer in einem 8er-Jahr passiv bleibt, lässt eine seltene Welle "
            "ungenutzt."
        ),
        "todo": [
            "<b>Eine sichtbare Sache aufsetzen — mit deinem Namen drauf.</b>",
            "<b>Mit Geld in Beziehung gehen — Zahlen wirklich anschauen.</b>",
            "<b>Verantwortung übernehmen, die du sonst gescheut hast.</b>",
        ],
    },
    9: {
        "tagline": "Vollendung · Loslassen · Abschluss",
        "text": (
            "Ein 9er-Jahr ist das <b>Abschluss-Jahr eines 9-Jahres-Zyklus</b>. Klassische Themen: "
            "Beziehungen, Projekte, alte Identitäten beenden. Es ist <i>nicht</i> die Zeit, Neues zu "
            "starten — das ist das nächste 1er-Jahr. Hier wird aufgeräumt, geheilt, integriert, "
            "verabschiedet."
        ),
        "todo": [
            "<b>Beenden, was beendet werden will.</b>",
            "<b>Verzeihen — sich selbst und anderen.</b>",
            "<b>Den Zyklus reflektieren — was war, was bleibt, was geht.</b>",
        ],
    },
}


# =======================================================================
# KOMPATIBILITÄT — Tabellen-Texte, mit leichter Variation pro Lebenszahl
# =======================================================================

def kompatibilitaets_zeilen(lebenszahl: int) -> list[list[str]]:
    """Liefert die 9 Zeilen für die Kompatibilitätstabelle. Format: [zahl, label, text]."""
    rows = [
        ["1", "Spannung",     "Zwei Pioniere — aufregend am Anfang, schwer auf Dauer, weil keiner nachgibt."],
        ["2", "Heilend",      "Bringt der harten 1 die fehlende Sanftheit. Klassische Partnerzahl für 1er."],
        ["3", "Leicht",       "Spielerische, kreative Resonanz — gut für Freundschaften und Co-Founder."],
        ["4", "Stark",        "Die 4 baut, was du planst. Idealer Kompagnon, COO-Energie."],
        ["5", "Anregend",     "Hält dich beweglich. Reibung möglich, weil 5 frei und du strukturiert bist."],
        ["6", "Erdend",       "Die 6 schafft Heimat, du schaffst Außenwelt. Familien-Kompatibel."],
        ["7", "Tief",         "Bringt Innenschau, die du brauchst. Schwierig, wenn die 7 zu zurückgezogen wird."],
        ["8", "Spannungsreich","Zwei starke Macher:innen. Entweder Powerteam oder Krieg. Selten Mittelweg."],
        ["9", "Inspirierend", "Resonanz auf Seelenebene — Lehrer:in-Energie."],
    ]
    # Wenn die Lebenszahl im Code ist, eigene Zeile etwas neutraler beschreiben:
    rows[lebenszahl - 1][1] = "Doppel-" + str(lebenszahl)
    return rows


# =======================================================================
# Hilfsfunktionen
# =======================================================================

ZAHL_THEMA = {
    1: "Pionier-Energie", 2: "Partnerschaft, Sensibilität, Geduld", 3: "Kreativität, Sichtbarkeit",
    4: "Disziplin, Struktur, Boden", 5: "Bewegung, Erfahrung, Risiko",
    6: "Familie, Harmonie, Schönheit", 7: "Innenwelt, Stille, Wahrheit",
    8: "Macht, Geld, Manifestation", 9: "Vollendung, Weisheit, Mission",
}


def fehlende_zahlen(*present: int) -> list[int]:
    """Welche der Zahlen 1-9 tauchen NICHT in den übergebenen Zahlen auf."""
    s = set(present)
    return [n for n in range(1, 10) if n not in s]
