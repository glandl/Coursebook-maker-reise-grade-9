+++
title = "P1 · Code & Gadget"
weight = 10
+++

**Dauer:** ~7 Wochen (Woche 1–7) · **Team:** 2–3 Personen · **Sprache:** Python (PC) und MicroPython (Board)

## Worum geht es?

Du lernst Python von Grund auf und baust am Ende ein **interaktives Gadget** auf einem Einplatinenrechner: ein Gerät, das auf Eingaben (Tasten, Sensoren) reagiert, sich in verschiedenen **Zuständen** befindet und über Ausgaben (LEDs, Display, Ton, Motor) antwortet.

Beispiele für Gadgets, die Teams gebaut haben oder bauen könnten:

- Reaktionsspiel mit zwei Tasten und Highscore
- Schrittzähler oder Würfel mit Beschleunigungssensor
- Nachtlicht, das auf Helligkeit und Bewegung reagiert
- Timer/Pomodoro-Uhr mit Display und Summer
- Alarmanlage mit Abstandssensor und Codeeingabe

## Das Endprodukt

1. Ein **funktionierendes Gadget** auf micro:bit, Raspberry Pi Pico, ESP32 oder Arduino (deine Wahl, siehe [MicroPython-Boards]({{% relref "werkzeuge/micropython-boards" %}})).
2. Ein **Zustandsdiagramm** deines Gadgets (welche Zustände gibt es, was löst Übergänge aus).
3. Der **Quellcode** mit Kommentaren, im Team-Repository.
4. Eine **3-Minuten-Präsentation** beim Review in Woche 7.
5. Deine **Lernjournal-Einträge** (mindestens einer pro Woche).

## Lernziele (Lehrplan)

Am Ende von P1 kannst du …

| TB | Kompetenz (Lehrplan-Wortlaut) | Schulstufe |
|----|-------------------------------|-----------|
| 02 Algorithmen & Programmierung | Algorithmen in einer textbasierten Programmiersprache anhand einfacher Anwendungen umsetzen. | 9 |
| 04 Systeme | Rechnersysteme mit Peripherie, Sensoren oder Aktoren sowie grundlegender Netzwerkfunktionalität konfigurieren und für lebensweltliche Aufgaben einsetzen. *(Netzwerk-Teil folgt in P2)* | 10 |
| 06 Mensch-Maschine-Interaktion | Einfache interaktive Systeme bauen sowie deren Systemverhalten durch Variation von Eingaben und Rückmeldungen untersuchen und erklären. | 10 |
| 09 Modellierung & Simulation | Reale Objekte oder Situationen zustandsbasiert und ablauforientiert abstrahieren und modellieren. | 9 |

## Ablauf

| Woche | Phase | Inhalt |
|-------|-------|--------|
| 1 | **Kickoff** | Maker-Reise, erste Python-Programme, Lernjournal auf GitHub anlegen (Markdown, erster Commit), Gadget-Ideen |
| 2 | Kickoff → Sprint 1 | Python: Variablen, Verzweigungen, Schleifen · Team & Board wählen · Anforderungen an das Gadget · Kanban-Board anlegen |
| 3 | Sprint 1 | Funktionen und Listen · Board in Betrieb nehmen: LED, Taste |
| 4 | Sprint 1 → Review | Sensoren/Aktoren anschließen · Zustandsdiagramm zeichnen · **Sprint-Review 1** |
| 5 | Sprint 2 | Zustandsautomat in Code umsetzen · Verhalten durch Eingaben variieren |
| 6 | Sprint 2 | Feinschliff, Testen, Doku · Präsentation vorbereiten |
| 7 | **Review & Retro** | Präsentationen · Retrospektive · Journal-Abgabe |

## Werkzeuge

- [Python & Thonny]({{% relref "werkzeuge/python-thonny" %}}) — ab Woche 1
- [MicroPython-Boards]({{% relref "werkzeuge/micropython-boards" %}}) — ab Woche 3
- [Wokwi & Browser-Simulatoren]({{% relref "werkzeuge/wokwi-simulator" %}}) — Fallback ohne Hardware
- [Git & GitHub]({{% relref "werkzeuge/git-github" %}}) und [Markdown]({{% relref "werkzeuge/markdown" %}}) — ab Woche 1 für das Lernjournal
- [Lernjournal]({{% relref "projekte/lernjournal" %}}) — von Anfang an

## Wochen

{{% children sort="weight" %}}
