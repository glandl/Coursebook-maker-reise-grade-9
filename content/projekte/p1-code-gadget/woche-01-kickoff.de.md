+++
title = "Woche 1 · Kickoff"
weight = 1
+++

**Heute:** Du lernst die Maker-Reise kennen, schreibst deine ersten Python-Programme, legst dein Lernjournal auf GitHub an und schreibst den ersten Eintrag in Markdown.

{{% notice style="info" title="Was du am Ende der Stunde hast" %}}
- Thonny läuft auf deinem Rechner und du hast zwei Programme ausgeführt und verändert.
- Du weißt, was ein **Zustand** ist und hast ein Gadget mit Zuständen simuliert.
- Du hast ein GitHub-Konto und ein Lernjournal-Repository mit deinem ersten **Commit**.
- Dein erster Journal-Eintrag steht, in Markdown, mit mindestens zwei Gadget-Ideen.
{{% /notice %}}

## 1. Die Maker-Reise (10 min)

Ein Schuljahr, fünf Projekte, ein Lernjournal. Schau dir die [Startseite]({{% relref "/" %}}) an: Jedes Projekt läuft nach demselben Rhythmus **Kickoff → Sprints → Review → Retro**. In P1 baust du dein erstes interaktives Gerät. Was am Ende herauskommen soll, steht im [Projektbrief]({{% relref "projekte/p1-code-gadget" %}}). Die Boards, auf denen das laufen wird, gehen heute durch die Klasse.

## 2. Werkzeug-Check: Thonny (15 min)

Öffne Thonny. Wenn es auf deinem Gerät noch fehlt, folge der [Setup-Anleitung]({{% relref "werkzeuge/python-thonny" %}}). Notfalls geht auch der Browser: [python.microbit.org](https://python.microbit.org/) hat eine Python-Konsole und einen Simulator.

Tippe unten in der **Shell** (das Fenster mit `>>>`) und drücke Enter:

```python
print("Hallo Maker-Reise!")
```

Wenn der Text erscheint, bist du startklar.

## 3. Zwei Programme (30 min)

Lege für jedes Programm eine neue Datei an (**Datei → Neu**), speichere sie unter dem angegebenen Namen und starte sie mit dem grünen Play-Button (oder **F5**).

### Programm 1 · `hallo.py` — Eingabe und Ausgabe

```python
name = input("Wie heißt du? ")
print("Hallo", name, "– willkommen zur Maker-Reise!")
```

**Ändere es:** Frag zusätzlich nach dem Lieblingsgerät und gib beides in einem Satz aus.

### Programm 2 · `schalter.py` — ein Gadget mit zwei Zuständen

Fast jedes Gerät hat **Zustände**: Eine Lampe ist AUS oder AN. Ein Tastendruck wechselt den Zustand. Genau das simulieren wir hier in Text, bevor wir es in ein paar Wochen mit echter LED und Taste bauen.

```python
# Ein Gadget mit zwei Zuständen: AUS und AN
zustand = "AUS"

while True:
    print("Lampe ist", zustand)
    taste = input("Taste drücken [Enter], 'q' zum Beenden: ")
    if taste == "q":
        break
    if zustand == "AUS":
        zustand = "AN"
    else:
        zustand = "AUS"

print("Gadget ausgeschaltet.")
```

**Ändere es:**

1. Zähle mit, wie oft die Taste gedrückt wurde, und gib die Zahl am Ende aus.
2. Die Lampe soll nach dem fünften Tastendruck von selbst ausgehen („Energiesparmodus").

{{% expand title="Tipp zu 1." %}}
Lege vor der Schleife `druecke = 0` an und erhöhe die Variable in der Schleife mit `druecke = druecke + 1`.
{{% /expand %}}

**Mach einen Screenshot** vom laufenden Programm. Den brauchst du gleich für das Journal.

### Wenn du schnell bist (oder zu Hause) · `ampel.py` — drei Zustände im Kreis

```python
zustand = "ROT"
schaltvorgaenge = 0

while schaltvorgaenge < 6:
    print("Ampel:", zustand)
    input("Weiter mit [Enter]")
    if zustand == "ROT":
        zustand = "GRÜN"
    elif zustand == "GRÜN":
        zustand = "GELB"
    else:
        zustand = "ROT"
    schaltvorgaenge = schaltvorgaenge + 1

print("Fertig nach", schaltvorgaenge, "Schaltvorgängen.")
```

**Ändere es:** Eine echte Ampel geht ROT → ROT-GELB → GRÜN → GELB → ROT. Baue den vierten Zustand ein. Zeichne danach die Zustände als Kreise und die Übergänge als Pfeile auf Papier. Das ist dein erstes **Zustandsdiagramm**.

{{% notice style="tip" title="Ausblick: dasselbe Programm auf dem Board" %}}
Ab Woche 3 läuft dein Schalter auf echter Hardware. Der Kern bleibt gleich, nur `input` und `print` werden durch Taste und LED ersetzt. Du musst das heute nicht verstehen, nur sehen, dass es dieselbe Idee ist.
{{% /notice %}}

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
```python
from microbit import *

zustand = "AUS"
while True:
    if button_a.was_pressed():
        if zustand == "AUS":
            zustand = "AN"
            display.show(Image.HAPPY)
        else:
            zustand = "AUS"
            display.clear()
```
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
```python
from machine import Pin
import time

led = Pin("LED", Pin.OUT)              # Onboard-LED
taste = Pin(14, Pin.IN, Pin.PULL_UP)   # Taste zwischen GP14 und GND

zustand = "AUS"
while True:
    if taste.value() == 0:             # gedrückt
        zustand = "AN" if zustand == "AUS" else "AUS"
        led.value(1 if zustand == "AN" else 0)
        time.sleep(0.3)                # Entprellen
```
{{% /tab %}}
{{% tab title="ESP32" %}}
```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)                  # Onboard-LED (meist GPIO 2)
taste = Pin(4, Pin.IN, Pin.PULL_UP)    # Taste zwischen GPIO 4 und GND

zustand = "AUS"
while True:
    if taste.value() == 0:
        zustand = "AN" if zustand == "AUS" else "AUS"
        led.value(1 if zustand == "AN" else 0)
        time.sleep(0.3)
```
{{% /tab %}}
{{% tab title="Arduino" %}}
Ein **Arduino UNO R4** oder **Nano ESP32** läuft mit MicroPython, dann gilt der ESP32-Code (LED-Pin anpassen). Der klassische **UNO R3** kann kein MicroPython: nimm dafür den [Wokwi-Simulator]({{% relref "werkzeuge/wokwi-simulator" %}}) mit einem virtuellen ESP32 oder den C++-Anhang.
{{% /tab %}}
{{< /tabs >}}

## 4. Dein Lernjournal auf GitHub (25 min)

Dein Journal ist eine Sammlung von **Markdown-Dateien in einem GitHub-Repository**. Jede Änderung speicherst du als **Commit**. So siehst du selbst und deine Lehrkraft, wie es Woche für Woche wächst.

### 4a · Konto und Repository (15 min)

Folge Teil 1 und Teil 2 der Anleitung [Git & GitHub]({{% relref "werkzeuge/git-github" %}}). Am Ende hast du ein Repository `lernjournal` mit einer `README.md`.

### 4b · Markdown in fünf Minuten (5 min)

Öffne den [Markdown-Spickzettel]({{% relref "werkzeuge/markdown" %}}). Du brauchst heute nur: `#` für Überschriften, `-` für Listen, `**fett**`, und wie man ein Bild einbindet.

### 4c · Erster Commit (5 min)

Bearbeite die `README.md` im Browser (Stift-Symbol), so dass sie so aussieht, mit deinen Angaben:

```markdown
# Lernjournal von <Vorname>

Klasse: <Klasse> · Schuljahr 2026/27 · Maker-Reise

## Einträge
- [P1 Woche 1](p1/woche-01.md)
```

Reiter **Preview** anschauen, dann **Commit changes** mit der Nachricht `README: Name und Klasse`. Dein erster Commit.

## 5. Journalauftrag 1 (15 min)

Lege im Repository die Datei `p1/woche-01.md` an (**Add file → Create new file**, der Schrägstrich erzeugt den Ordner) und schreib deinen ersten Eintrag:

{{% notice style="primary" title="Journalauftrag 1 · Startpunkt" icon="book" %}}
```markdown
# P1 · Woche 1 · <Datum>

## Erwartungen
Was erwartest du dir von der Maker-Reise? Was kannst du schon
(Programmieren, Elektronik, Basteln)?

## Gadget-Ideen
Mindestens zwei Geräte aus deinem Alltag, die du gern bauen würdest.
Zu jeder Idee: Eingaben (was misst oder drückt man), Ausgaben
(was leuchtet, piept, bewegt sich), Zustände.

## Geklappt / hängen geblieben
Was hat heute funktioniert, wo bist du stecken geblieben?

## Beleg
Screenshot von schalter.py: in den Ordner images/ hochladen und
hier einbinden: ![schalter.py](../images/p1-w01-schalter.png)
```
{{% /notice %}}

Commit-Nachricht: `P1 Woche 1: erster Eintrag`. Wenn der Screenshot-Upload heute nicht mehr klappt, holst du ihn bis nächste Woche nach.

Falls du Inspiration für die Gadget-Ideen brauchst: Das kann ein micro:bit.

{{< youtube SF_Ym8fWTPU >}}

## Check dich selbst

{{% expand title="Was ist der Unterschied zwischen `print` und `input`?" %}}
`print` gibt Text aus. `input` zeigt einen Text an, wartet auf eine Eingabe und liefert sie als Text zurück, den du in einer Variable speichern kannst.
{{% /expand %}}

{{% expand title="Was passiert in `schalter.py`, wenn du die Zeile `if taste == \"q\": break` löschst?" %}}
Die Schleife läuft endlos. Du kannst das Programm nur noch mit dem Stopp-Button (oder Strg+C in der Shell) beenden.
{{% /expand %}}

{{% expand title="Wie viele Zustände hat ein Fahrradlicht mit den Modi Aus, Dauerlicht, Blinken?" %}}
Drei. Ein Tastendruck geht im Kreis: Aus → Dauerlicht → Blinken → Aus. Das ist genau die Struktur von `ampel.py`.
{{% /expand %}}

{{% expand title="Was ist ein Commit, und warum braucht er eine Nachricht?" %}}
Ein Commit ist ein gespeicherter Stand deines Repositorys mit Zeitpunkt und Autor:in. Die Nachricht sagt, was sich geändert hat, damit du (und deine Lehrkraft) die Geschichte des Journals lesen können, ohne jede Datei zu öffnen.
{{% /expand %}}

## Bis nächste Woche

- Journalauftrag 1 fertigstellen und committen (Screenshot nicht vergessen).
- `ampel.py` ausprobieren, falls du heute nicht dazu gekommen bist.
- Thonny zu Hause installieren, falls du ein eigenes Gerät nutzt ([Anleitung]({{% relref "werkzeuge/python-thonny" %}})).
- Video zum Nachschauen, wenn heute etwas zu schnell ging:

{{< youtube oxXAb8IikHM >}}
