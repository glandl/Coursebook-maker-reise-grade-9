+++
title = "Woche 7 · Review und Retrospektive"
weight = 7
+++

**Heute:** Das große Finale von P1. Ihr präsentiert eure Gadgets, schaut in der **Retrospektive** darauf, wie ihr zusammengearbeitet habt, und schließt euer Lernjournal für dieses Projekt ab.

{{% notice style="info" title="Was du am Ende der Stunde hast" %}}
- Euer Team hat das Gadget präsentiert und Feedback bekommen.
- Du hast mindestens einem anderen Team schriftliches Feedback gegeben.
- Euer Team hat 1–2 konkrete Vorsätze für P2.
- Dein Journal für P1 ist vollständig, mit Projektrückblick und Selbsteinschätzung, und committet.
{{% /notice %}}

## 1. Aufbauen und Technik-Check (10 min)

- Gadget aufbauen, an Strom (Powerbank oder USB) anschließen, **einmal komplett durchspielen**.
- Zustandsdiagramm und Code-Ausschnitt für die Projektion bereit (Team-Repository im Browser geöffnet).
- Plan-B-Video griffbereit.
- Reihenfolge der Teams steht an der Tafel. Jede Person bekommt **ein Team zugelost**, dem sie schriftlich Feedback gibt.

## 2. Präsentationen (45 min)

Pro Team **3 Minuten Präsentation + 2 Minuten Fragen**, Ablauf wie in [Woche 6]({{% relref "projekte/p1-code-gadget/woche-06-testen-doku" %}}) geplant. Die Lehrkraft stoppt die Zeit.

**Feedback-Karte** (für das zugeloste Team, auf Papier oder als Issue im Team-Repository):

```markdown
Team: …

Mir gefällt: …
Ich frage mich: …
Wie wäre es, wenn: …

Die Demo hat gezeigt, dass … (welche User Story?)
```

Worauf die Lehrkraft achtet (Produkt, Prozess, Präsentation, Journal), steht in den [Rubrik-Vorlagen]({{% relref "lehrkraefte/rubriken" %}}).

## Pause (5 min)

## 3. Retrospektive (20 min)

Das Review schaut auf das **Produkt**. Die **Retrospektive** schaut auf die **Zusammenarbeit**: Wie haben wir gearbeitet, und was machen wir im nächsten Projekt anders? Es geht nicht um Schuld, sondern um Verbesserung.

Format **Start · Stop · Continue**, im Team:

| Schritt | Zeit | Was passiert |
|---------|------|--------------|
| Still schreiben | 5 min | Jede Person schreibt Haftnotizen in drei Spalten: **Start** (Was sollten wir anfangen?), **Stop** (Was sollten wir lassen?), **Continue** (Was hat gut funktioniert?). Eine Idee pro Zettel. |
| Vorstellen und ordnen | 8 min | Reihum vorlesen und aufkleben, Ähnliches zusammenschieben. |
| Entscheiden | 5 min | Jede Person hat 2 Punkte zum Vergeben. Die 1–2 Zettel mit den meisten Punkten werden **Vorsätze für P2**, formuliert als konkrete Handlung: „Wir machen jede Stunde ein Stand-up mit Board-Foto" statt „besser kommunizieren". |
| Festhalten | 2 min | Foto der Wand, Vorsätze in die `README.md` des Team-Repositorys unter **Retrospektive**. |

Denkanstöße, falls euch nichts einfällt: Kanban-Board aktuell gehalten? Aufgaben fair verteilt? Wann habt ihr am meisten geschafft, wann am wenigsten, und warum? Wie lief das Zusammenführen des Codes?

{{< youtube rWz9VsHSpAE >}}

## 4. Journal-Abgabe (15 min)

Abgabe heißt: **der letzte Commit ist drin**. Es wird nichts eingesammelt (siehe [Lernjournal]({{% relref "projekte/lernjournal" %}})).

{{% notice style="primary" title="Journalauftrag 7 · Projektrückblick P1" icon="book" %}}
Datei `p1/woche-07.md`:

```markdown
# P1 · Woche 7 · Projektrückblick · <Datum>

## Unser Gadget
Ein Satz, ein Foto, Link zum Team-Repository.

## Mein bester Code
Ein Code-Ausschnitt, den du selbst geschrieben hast, und was daran gut ist.

## Selbsteinschätzung
| Ich kann … | 1 | 2 | 3 | 4 | Beleg (Link) |
|------------|---|---|---|---|--------------|
| einfache Algorithmen in Python umsetzen (Verzweigung, Schleife, Funktion, Liste) | | | | | |
| ein Board mit Sensor und Aktor in Betrieb nehmen | | | | | |
| das Verhalten eines interaktiven Systems durch Variation von Eingaben und Rückmeldungen untersuchen und erklären | | | | | |
| ein Gerät mit einem Zustandsdiagramm und einem Ablaufplan modellieren | | | | | |

1 = noch nicht · 2 = mit Hilfe · 3 = selbstständig · 4 = kann es anderen erklären

## Retrospektive
Die Vorsätze eures Teams für P2, und ein persönlicher Vorsatz.

## Feedback
Das Feedback, das ihr bei der Präsentation bekommen habt, in einem Satz,
und was du davon hältst.
```
{{% /notice %}}

**Checkliste vor dem letzten Commit:**

- [ ] `p1/woche-01.md` bis `p1/woche-07.md` sind da.
- [ ] Journalaufträge 1–7 sind beantwortet (Überschriften aus den Vorlagen).
- [ ] Bilder liegen in `images/` und werden angezeigt (Vorschau prüfen).
- [ ] `README.md` verlinkt alle P1-Einträge.
- [ ] Keine Passwörter, keine Fotos von Personen ohne Zustimmung.

Commit-Nachricht: `P1 Woche 7: Projektrückblick, Abgabe P1`.

## 5. Abschlussquiz P1 (5 min)

{{< quiz title="Abschlussquiz · P1 Code & Gadget" >}}
{{< question correct="2" >}}
Was gibt dieses Programm aus?

```python
werte = [4, 8, 6]
summe = 0
for w in werte:
    if w > 5:
        summe = summe + w
print(summe)
```
---
18
14
8
3
---
Nur 8 und 6 sind größer als 5, also 8 + 6 = 14.
{{< /question >}}
{{< question correct="1" >}}
`zahl = input("Zahl: ")`. Wie rechnest du mit der Eingabe?
---
`zahl = int(input("Zahl: "))`
`zahl = input(int("Zahl: "))`
`zahl = number(input("Zahl: "))`
Gar nicht, `input` liefert schon eine Zahl.
---
`input` liefert Text, `int(...)` wandelt ihn in eine ganze Zahl um.
{{< /question >}}
{{< question correct="3" >}}
Ein Rollo hat die Zustände OBEN, UNTEN und FÄHRT. Welches ist ein **Ereignis**, das einen Übergang auslöst?
---
MOTOR
FÄHRT
Endschalter erreicht
Rollo
---
Zustände beschreiben Situationen, Ereignisse lösen die Wechsel aus. „Endschalter erreicht" beendet den Zustand FÄHRT.
{{< /question >}}
{{< question correct="4" >}}
Eine Taste an einem Pin mit Pull-up soll die LED **genau einmal pro Druck** umschalten. Was braucht man?
---
Ein längeres `time.sleep`.
Einen zweiten Pin.
`taste.value() == 1` statt `== 0`.
Flankenerkennung: nur den Wechsel von nicht gedrückt zu gedrückt auswerten.
---
Solange die Taste unten ist, meldet der Pin viele Durchläufe lang 0. Nur der Wechsel 1 → 0 ist der eigentliche Druck.
{{< /question >}}
{{< question correct="2" >}}
Welche Aufteilung des Codes haben wir in P1 verwendet?
---
Alles in `main.py`, damit man nichts suchen muss.
`hardware.py` (board-spezifisch), `logik.py` (testbar am PC), `main.py` (Hauptschleife)
Eine Datei pro Zustand.
`input.py`, `output.py`, `test.py`
---
Die Hardware-Schicht macht den Code boardunabhängig, die Logik-Datei macht ihn testbar.
{{< /question >}}
{{< question correct="1" >}}
Ihr ersetzt bei einem Wecker den Ton durch ein kurzes Aufleuchten der LED. Was untersucht ihr damit im Sinne der Mensch-Maschine-Interaktion?
---
Wie sich eine andere Rückmeldung auf das Verhalten der Nutzer:innen auswirkt (z. B. ob sie aufwachen).
Wie schnell der Prozessor ist.
Ob der Code kürzer wird.
Wie viel Strom die LED braucht.
---
Rückmeldungen variieren und beobachten, wie Menschen darauf reagieren, ist genau das Experiment aus Woche 5.
{{< /question >}}
{{< question correct="3" >}}
Was ist der Zweck einer **Retrospektive**?
---
Die Noten für das Projekt festlegen.
Das Produkt vorführen.
Die Zusammenarbeit im Team verbessern, mit konkreten Vorsätzen für das nächste Projekt.
Den Code auf Fehler prüfen.
---
Das Produkt wird im Review gezeigt, der Code im Code-Review geprüft. Die Retrospektive betrachtet, **wie** das Team gearbeitet hat.
{{< /question >}}
{{< question correct="4" >}}
Wo steht im Kanban-Board eine Karte, deren Akzeptanzkriterien erst zum Teil erfüllt sind?
---
Fertig
Backlog, sie wird gelöscht.
Irgendwo, Hauptsache sichtbar.
In Arbeit
---
„Fertig" heißt: alle Akzeptanzkriterien erfüllt. Bis dahin bleibt die Karte in Arbeit.
{{< /question >}}
{{< /quiz >}}

## Ausblick: P2 Wetterstation

Euer Board kann jetzt messen und reagieren. In [P2]({{% relref "projekte/p2-wetterstation" %}}) lernt es **funken**: Messwerte über WLAN verschicken, speichern und auswerten. Wer mit ESP32 oder Pico W gebaut hat, verwendet das Board weiter, und `hardware.py` wächst einfach um neue Funktionen. Die Vorsätze aus der heutigen Retrospektive nehmt ihr mit.
