+++
title = "Woche 2 · Team, Anforderungen, Kanban"
weight = 2
+++

**Schüler:innen-Seite:** [P1 Woche 2 · Team, Anforderungen, Kanban]({{% relref "projekte/p1-code-gadget/woche-02-anforderungen" %}}) · **Dauer:** Doppelstunde · 95 min verplant, die restliche Zeit bleibt frei

Diese Stunde hat zwei Hälften: **Python-Werkstatt** (Variablen, Verzweigungen, Schleifen) und **Projektstart** (Team, Board, Anforderungen, Kanban). Mit dieser Stunde beginnt **Sprint 1** (Woche 2–4), der mit dem Sprint-Review in Woche 4 endet.

## Ziele der Stunde

- Alle können Eingaben mit `int()`/`float()` umwandeln, mit `if`/`elif`/`else` verzweigen und mit `while` und `for` wiederholen (TB 02, 9. Schulstufe).
- Jede:r ist in einem Team aus 2–3 Personen, jedes Team hat ein Board gewählt und ein privates Team-Repository angelegt.
- Jedes Team hat `ANFORDERUNGEN.md` mit 3–5 **User Stories** samt Akzeptanzkriterien und einer Eingaben-→-Gadget-→-Ausgaben-Skizze (Vorgriff auf TB 07, 10. Schulstufe: Anforderungen in natürlicher Sprache und einfachen grafischen Notationen).
- Jedes Team hat ein Kanban-Board mit gefüllter Spalte „Sprint 1" und kennt das WIP-Limit und das Stand-up (Vorgriff auf die agilen Methoden in TB 08).
- Journalauftrag 2 ist begonnen und committet.

## Vor der Stunde: Commit-Check

Das ist ab jetzt Routine (siehe [Woche 1]({{% relref "lehrkraefte/verlaufsplaene/woche-01" %}})): Submissions-Seite des Assignments in Classroom 50 öffnen (Seite neu laden!) und durchsehen, wer `p1/woche-01.md` gepusht hat.

- [ ] Liste der Personen **ohne Commit** notieren. Diese Woche ist der häufigste Grund kein Unwille, sondern ein **nicht fertiges Konto** (Bestätigungsmail, Benutzername, Roster-Eintrag).
- [ ] Für diese Personen Nacharbeit einplanen: Roster ergänzen und erneut hochladen, Assignment-Link nochmals schicken. In der Stunde selbst kann das eine fortgeschrittene Person in der Python-Phase übernehmen (siehe Differenzierung).
- [ ] Gadget-Ideen aus den Journaleinträgen überfliegen. Zwei bis drei tragfähige Ideen notieren — die brauchst du in Phase 3, wenn ein Team keine eigene Idee hat.

## Vorbereitung

### Technik

- [ ] Buch-Seite Woche 2 am Beamer geöffnet, dazu ein leerer Thonny mit sichtbarem Shell-Bereich.
- [ ] `thermostat.py` und `countdown.py` selbst einmal durchlaufen lassen, inklusive der provozierten Fehlermeldung (Eingabe `warm` → `ValueError`). Du willst die Fehlermeldung vorlesen können.
- [ ] GitHub aus dem Schulnetz erreichbar (wie Woche 1). Für die Team-Repositories reicht der Browser, **kein lokales Git**.
- [ ] Optional: ein fertiges Beispiel-`ANFORDERUNGEN.md` (Nachtlicht, wie auf der Schüler:innen-Seite) in einem eigenen Repo, um Mermaid-Rendering live auf GitHub zu zeigen.

### Hardware-Bestand

- [ ] **Vorher zählen** und an die Tafel schreiben: wie viele micro:bit, Pico/Pico W, ESP32, Arduino tatsächlich verfügbar sind, inklusive Kabel und Steckbretter. Ohne diese Zahl wählen alle Teams das Board mit dem coolsten Namen.
- [ ] Verteilungsregel vorab festlegen und ansagen, z. B. „pro Team ein Board, Reihenfolge der Anmeldung entscheidet, ESP32 nur für Teams, deren Gadget später vernetzt werden soll".
- [ ] Ohne ausreichend Hardware: Teams auf [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) bzw. den micro:bit-Simulator verweisen. Das ist kein Notbehelf zweiter Klasse — ab Woche 3 funktioniert damit der komplette Sprint.

### Material für Kanban

- [ ] Haftnotizen (zwei Farben: Story und Aufgabe), dicke Stifte, pro Team ein Plakat oder ein Tafelabschnitt mit vier Spalten.
- [ ] Aufbewahrung klären: Plakate bleiben im Raum (Schrank, Rückwand). Sonst ist das Board nächste Woche weg.
- [ ] Ansagen: **Foto des Boards am Stundenende ins Team-Repository.** Das ist der Nachweis, unabhängig davon, ob das Board aus Papier oder ein GitHub Project ist.

### Organisatorisches

- [ ] **Team-Liste** vorbereiten (Tabelle am Beamer oder auf Papier), die du in der Stunde ausfüllst:

  | Team | Mitglieder | Gadget (ein Satz) | Board | Repo-URL |
  | ------ | ----------- | ------------------- | ------- | ---------- |

  Die Repo-URLs brauchst du für den wöchentlichen Check und für das Review in Woche 4.
- [ ] Entscheiden, ob du als **Collaborator** in jedes Team-Repository willst. Empfehlung: ja, sonst siehst du die Arbeit der Teams bis Woche 4 nicht.
- [ ] Sprint-1-Termin ansagen können: **Review in Woche 4**. Alles, was in der Spalte „Sprint 1" landet, muss dort vorführbar sein.

## Verlauf

| Zeit | Phase | Lehrkraft | Schüler:innen | Material |
| ------ | ------- | ----------- | --------------- | ---------- |
| 0–5 | **Rückblick** | Sprint-Logik in zwei Sätzen: ab heute Sprint 1, Review in Woche 4. Partnerarbeit anmoderieren: Gadget-Ideen zeigen, Frage „welche Idee hat die klarsten Eingaben, Ausgaben, Zustände?" | Zu zweit Journaleinträge aus Woche 1 zeigen | Beamer, Buchseite |
| 5–20 | **Python A: Variablen & Verzweigungen** | `thermostat.py` am Beamer eintippen, nicht kopieren. `float(input(...))` erklären. Dann bewusst `warm` eingeben, Traceback gemeinsam lesen: **letzte Zeile zuerst**, dann Zeilennummer. Danach Einzel-/Paararbeit an den beiden Änderungsaufgaben. | Programm abtippen, ausprobieren, Aufgaben 1 und 2 | PCs, Thonny |
| 20–35 | **Python B: Schleifen** | Kurzer Stopp: `while` (Bedingung) vs. `for` (Anzahl) an der Tafel gegenüberstellen, `range(3)` → 0, 1, 2 explizit betonen. `countdown.py` laufen lassen, Stopp-Button wiederholen. Zirkulieren, Schnelle auf `wuerfel.py` schicken. | `countdown.py`, Änderungsaufgaben; Schnelle: `wuerfel.py` | PCs, Buchseite Abschnitt 2 |
| 35–50 | **Team & Board** | Hardware-Bestand an der Tafel zeigen, Boardtabelle in 3 min durchgehen (Stärken, nicht Pinouts), Hinweis auf P2/WLAN geben. Teams bilden lassen, **Timer auf 8 min**. Danach Team-Liste am Beamer ausfüllen. Übrig gebliebene Personen selbst zuordnen, nicht ausdiskutieren lassen. Eine Person pro Team legt das private Repo `p1-gadget-<teamname>` an und lädt Team plus Lehrkraft als Collaborator ein. | Team bilden, Board wählen, Repo anlegen, Einladungen annehmen | Tafel (Bestand), Git-Anleitung Teil 2, Team-Liste |
| 50–75 | **Anforderungen** | User-Story-Schema an die Tafel: **Als … möchte ich … damit …**. Gemeinsam **eine** Story für ein Beispiel-Gadget formulieren und zwei Akzeptanzkriterien dazu, „schnell" durch „innerhalb von 1 s" ersetzen. Muss/Soll/Kann erklären. Mermaid-Block einmal live auf GitHub zeigen. Dann Teamarbeit, zirkulieren und **jedes Team einmal anschauen**: prüfen, ob die Stories Verhalten beschreiben und nicht Bauteile. | `ANFORDERUNGEN.md` im Team-Repo: Gadget-Satz, Skizze, 3–5 Stories mit Priorität und Kriterien | Buchseite Abschnitt 4, Beispiel-Repo |
| 75–85 | **Kanban** | Vier Spalten an der Tafel, eine Muss-Story eines Teams gemeinsam in drei Karten zerlegen („LED anschließen", „Sensorwert ausgeben", „Schwellwert finden"). WIP-Limit und Stand-up ansagen — das Stand-up beginnt ab Woche 3 jede Stunde. Karten schreiben lassen, Sprint-1-Spalte füllen. Am Ende: Foto ins Repo. | Board aufbauen, Karten schreiben, Sprint 1 auswählen, Foto hochladen | Haftnotizen, Stifte, Plakate |
| 85–95 | **Journalauftrag 2 & Ausblick** | Vorlage am Beamer zeigen, `p1/woche-02.md` anlegen lassen, Commit-Nachricht vorgeben. Letzte 2 min: Ausblick Woche 3 (Funktionen, Listen, Board in Betrieb nehmen), Hausaufgabe nennen. | Eintrag schreiben, committen | Journalauftrag 2 |

## Differenzierung

- **Schnelle:** `wuerfel.py` mit Zählung der Sechser; Kanban digital als GitHub Project statt Papier; Akzeptanzkriterien mit messbaren Zahlen nachschärfen; als Helfer:innen für Nachzügler aus Woche 1 einsetzen (Konto, Roster, erster Commit).
- **Langsame:** Bei `countdown.py` genügt Änderungsaufgabe 1. In der Anforderungsphase reichen **zwei** Muss-Stories mit je einem Kriterium; die Skizze darf mit der Hand gezeichnet und fotografiert werden statt als Mermaid.
- **Team ohne eigene Idee:** Deine zwei bis drei vorbereiteten Ideen anbieten (Reaktionsspiel, Würfel, Nachtlicht). Diese Teams starten mit einer fertigen Story aus dem Buchbeispiel und schreiben nur die restlichen selbst.
- **Vorwissen:** Diese Teams bekommen die Auflage, ihre Stories so zu schneiden, dass jede in einer Stunde erledigbar ist — das ist die eigentlich schwierige Übung und kostet sie mehr Denkarbeit als der Python-Teil.

## Typische Stolpersteine

- **Teambildung frisst die Stunde.** Harte Grenze: 8 min mit sichtbarem Timer. Wer nach Ablauf kein Team hat, wird zugeteilt. Ankündigen, dass zugeteilt wird, bevor der Timer läuft.
- **Alle wollen den ESP32.** Bestandszahlen und Verteilungsregel stehen vor der Wahl an der Tafel, nicht danach.
- **Team-Repo versehentlich öffentlich.** Beim Anlegen explizit auf **Private** zeigen. Nachträglich änderbar unter *Settings → General → Danger Zone*.
- **Collaborator-Einladung nicht angenommen.** Die Eingeladenen müssen den Link in der Mail oder die Benachrichtigung auf GitHub bestätigen, sonst können sie nicht schreiben. In der Stunde einmal nachfragen: „Kann jede:r in eurem Repo eine Datei anlegen?"
- **Stories sind in Wirklichkeit Aufgaben** („Summer an Pin 15 anschließen"). Gegenfrage: *Wer* will das, und *wofür*? Wenn es darauf keine Antwort gibt, ist es eine Kanban-Karte, keine Story.
- **Akzeptanzkriterien ohne Messbarkeit** („reagiert schnell", „funktioniert gut"). Regel an der Tafel lassen: Eine fremde Person muss das Kriterium ohne Rückfrage prüfen können.
- **Mermaid rendert nicht:** Der Block braucht die Zeile ```` ```mermaid ````, und er wird nur auf GitHub gerendert, nicht in Thonny oder im lokalen Editor.
- `input()` liefert Text — `TypeError` beim Rechnen. Kommt garantiert; nutze ihn als Anlass, das Traceback-Lesen zu üben (steht auch als Quizfrage auf der Schüler:innen-Seite).
- **`=` statt `==`** in der Bedingung. Erzeugt einen `SyntaxError`; gleich beim ersten Auftreten für alle an der Tafel klären.
- **`range`-Abzählfehler:** `range(3)` endet **vor** 3, `range(start, 0, -1)` endet bei 1. Einmal explizit an der Tafel abzählen.
- **`while`-Schleife ohne Abbruch** blockiert Thonny. Stopp-Button nochmals zeigen, wie in Woche 1.

## Hausaufgabe

- `ANFORDERUNGEN.md` im Team fertigstellen, Kanban-Board mit Karten für Sprint 1 füllen.
- Journalauftrag 2 committen (`p1/woche-02.md`), falls in der Stunde nicht fertig geworden.
- Wer Hardware zu Hause hat: [MicroPython-Boards]({{% relref "werkzeuge/micropython-boards" %}}) lesen und das Board mit Thonny verbinden. Ohne Hardware: [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) oder [python.microbit.org](https://python.microbit.org/) öffnen.

## Nachweis und Fortschrittskontrolle

Diese Woche gibt es **zwei** Nachweise:

1. **Persönlich:** der Commit an `p1/woche-02.md` im Lernjournal — wie gewohnt über die Submissions-Seite prüfbar.
2. **Im Team:** `ANFORDERUNGEN.md` und das Board-Foto im Team-Repository. Trage die Repo-URLs in deine Team-Liste ein und sieh vor Woche 3 einmal in jedes Repo.

Fehlt bei einem Team `ANFORDERUNGEN.md`, fängt dieses Team Woche 3 damit an, statt mit dem Board. Ohne Anforderungen gibt es in Woche 4 nichts, woran das Review messen könnte, ob etwas fertig ist.
