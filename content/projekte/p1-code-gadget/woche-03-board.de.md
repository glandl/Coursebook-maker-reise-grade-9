+++
title = "Woche 3 · Funktionen, Listen, erstes Board"
weight = 3
+++

**Heute:** Du verpackst Code in **Funktionen**, speicherst viele Werte in **Listen** und bringst euer Board zum Leben: LED blinkt, Taste schaltet.

{{% notice style="info" title="Was du am Ende der Stunde hast" %}}
- Du kannst eine Funktion mit Parametern und Rückgabewert schreiben und aufrufen.
- Du kannst eine Liste anlegen, erweitern, durchlaufen und mit dem Index auf Elemente zugreifen.
- Euer Board ist mit Thonny verbunden, eine LED blinkt und eine Taste schaltet sie um.
- Der Board-Code liegt im Team-Repository, das Kanban-Board ist aktuell.
{{% /notice %}}

## 1. Stand-up (5 min)

Vor dem Kanban-Board, jede Person höchstens eine Minute: **Was habe ich gemacht? Was mache ich heute? Wo hänge ich?** Karten verschieben, Namen draufschreiben.

## 2. Funktionen (15 min)

Eine **Funktion** ist ein benannter Codeblock. Du schreibst ihn einmal mit `def` und rufst ihn beliebig oft auf. Werte gibst du als **Parameter** hinein, mit `return` gibt die Funktion ein Ergebnis zurück.

### `schalter_funktionen.py`

Das ist `schalter.py` aus Woche 1, aufgeräumt: Die Logik („was kommt nach AUS?") und die Ausgabe sind jetzt getrennte Funktionen.

```python
def umschalten(zustand):
    """Liefert den neuen Zustand nach einem Tastendruck."""
    if zustand == "AUS":
        return "AN"
    return "AUS"


def anzeigen(zustand, druecke):
    symbol = "💡" if zustand == "AN" else "⚫"
    print(symbol, "Lampe ist", zustand, "| Tastendrücke:", druecke)


zustand = "AUS"
druecke = 0
anzeigen(zustand, druecke)

while True:
    taste = input("[Enter] drücken, 'q' zum Beenden: ")
    if taste == "q":
        break
    zustand = umschalten(zustand)
    druecke = druecke + 1
    anzeigen(zustand, druecke)
```

**Warum der Aufwand?** In ein paar Minuten ersetzt du `input` durch eine echte Taste und `print` durch eine echte LED. Die Funktion `umschalten` bleibt **unverändert**. Getrennte Logik kann man außerdem ohne Hardware testen (das machen wir in Woche 6).

**Ändere es:** Füge einen dritten Zustand `BLINKEN` hinzu: AUS → AN → BLINKEN → AUS. Du musst nur `umschalten` ändern (und das Symbol in `anzeigen`).

## 3. Listen (15 min)

Eine **Liste** speichert mehrere Werte in einer Variable, in fester Reihenfolge.

```python
zustaende = ["ROT", "ROT-GELB", "GRÜN", "GELB"]

print(zustaende[0])        # ROT      – Index beginnt bei 0
print(zustaende[-1])       # GELB     – von hinten
print(len(zustaende))      # 4

for z in zustaende:
    print("Ampel:", z)
```

### `ampel_liste.py` — Zustände im Kreis

```python
import time

ZUSTAENDE = ["ROT", "ROT-GELB", "GRÜN", "GELB"]
DAUER = [3, 1, 3, 1]              # Sekunden pro Zustand

i = 0
for schritt in range(8):
    print("Ampel:", ZUSTAENDE[i])
    time.sleep(DAUER[i])
    i = (i + 1) % len(ZUSTAENDE)   # nach dem letzten wieder zum ersten
```

`%` ist der **Rest** der Division: `4 % 4` ist 0, darum springt der Index vom letzten Element zurück auf 0. Namen in GROSSBUCHSTABEN bedeuten: Dieser Wert ändert sich im Programm nicht (Konstante).

### `messwerte.py` — Werte sammeln und auswerten

Sensoren liefern laufend Werte. Die sammelst du in einer Liste:

```python
messwerte = []                     # leere Liste

while True:
    eingabe = input("Messwert (leer = fertig): ")
    if eingabe == "":
        break
    messwerte.append(float(eingabe))

if len(messwerte) > 0:
    print("Anzahl:", len(messwerte))
    print("Kleinster:", min(messwerte), "Größter:", max(messwerte))
    print("Mittelwert:", round(sum(messwerte) / len(messwerte), 2))
```

**Ändere es:** Schreib eine Funktion `mittelwert(werte)`, die den Mittelwert zurückgibt, und verwende sie.

{{% expand title="Lösung" %}}
```python
def mittelwert(werte):
    return sum(werte) / len(werte)
```
{{% /expand %}}

{{< youtube B1mMAieycPY >}}

{{< youtube R7lZTvC9UUU >}}

## Pause (5 min)

## 4. Board in Betrieb nehmen (45 min)

### 4a · Verbinden (10 min)

1. Board per USB anschließen.
2. Thonny: **Werkzeuge → Optionen → Interpreter**, das passende MicroPython wählen (bei micro:bit: „MicroPython (BBC micro:bit)"). Ist noch kein MicroPython auf dem Board, bietet Thonny unten rechts **Install or update MicroPython** an.
3. In der Shell `print("Hallo Board")` eintippen. Die Antwort kommt jetzt **vom Board**, nicht vom PC.

Details, Treiber und Fehlerbehebung je Board: [MicroPython-Boards]({{% relref "werkzeuge/micropython-boards" %}}). **Kein Board zur Hand?** [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) (Pico, ESP32) oder [python.microbit.org](https://python.microbit.org/) (micro:bit mit Simulator) funktionieren mit demselben Code.

{{% notice style="warning" title="Strom aus beim Umstecken" %}}
Bauteile nur anschließen oder umstecken, wenn das USB-Kabel **abgezogen** ist. LEDs immer mit **Vorwiderstand** (220 Ω). Eine LED hat eine Richtung: das **lange Bein** (+) zeigt zum Pin, das kurze zu GND.
{{% /notice %}}

### 4b · Blinken (10 min)

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
Keine Verkabelung nötig. Die LED in der Mitte der 5×5-Anzeige hat die Koordinaten (2, 2).

```python
from microbit import *

for i in range(10):
    display.set_pixel(2, 2, 9)   # Helligkeit 0–9
    sleep(500)                   # Millisekunden
    display.set_pixel(2, 2, 0)
    sleep(500)
```
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
Zuerst die **Onboard-LED**, keine Verkabelung nötig:

```python
from machine import Pin
import time

led = Pin("LED", Pin.OUT)

for i in range(10):
    led.value(not led.value())   # umschalten
    time.sleep(0.5)
```

Danach eine **externe LED**: GP15 → 220 Ω → langes LED-Bein, kurzes Bein → GND. Im Code `Pin("LED", …)` durch `Pin(15, Pin.OUT)` ersetzen.
{{% /tab %}}
{{% tab title="ESP32" %}}
Zuerst die **Onboard-LED** (bei den meisten DevKit-Boards an GPIO 2):

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)

for i in range(10):
    led.value(not led.value())   # umschalten
    time.sleep(0.5)
```

Keine Onboard-LED oder sie bleibt dunkel? Externe LED: GPIO 18 → 220 Ω → langes LED-Bein, kurzes Bein → GND, im Code `Pin(18, Pin.OUT)`.
{{% /tab %}}
{{% tab title="Arduino" %}}
**UNO R4 / Nano ESP32 mit MicroPython:** Code wie im ESP32-Tab, Pinnummern laut Pinout deines Boards auf [MicroPython-Boards]({{% relref "werkzeuge/micropython-boards" %}}) anpassen.
**UNO R3:** in [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) ein ESP32-Projekt anlegen und den ESP32-Code verwenden.
{{% /tab %}}
{{< /tabs >}}

**Ändere es:** Lass die LED dreimal kurz und dreimal lang blinken.

### 4c · Taste schaltet LED (15 min)

Jetzt kommt `umschalten` aus Teil 2 auf das Board, **unverändert**.

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
```python
from microbit import *


def umschalten(zustand):
    if zustand == "AUS":
        return "AN"
    return "AUS"


def anzeigen(zustand):
    if zustand == "AN":
        display.show(Image.HEART)
    else:
        display.clear()


zustand = "AUS"
anzeigen(zustand)

while True:
    if button_a.was_pressed():   # True nur einmal pro Druck
        zustand = umschalten(zustand)
        anzeigen(zustand)
    sleep(20)
```
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
**Aufbau:** Taste zwischen **GP14** und **GND**. Externe LED an GP15 wie in 4b (oder Onboard-LED `Pin("LED", Pin.OUT)`).

```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
taste = Pin(14, Pin.IN, Pin.PULL_UP)   # nicht gedrückt = 1, gedrückt = 0
vorher = 1


def gedrueckt():
    """True nur in dem Moment, in dem die Taste hinuntergeht."""
    global vorher
    jetzt = taste.value()
    neu = vorher == 1 and jetzt == 0
    vorher = jetzt
    return neu


def umschalten(zustand):
    if zustand == "AUS":
        return "AN"
    return "AUS"


def anzeigen(zustand):
    led.value(1 if zustand == "AN" else 0)


zustand = "AUS"
anzeigen(zustand)

while True:
    if gedrueckt():
        zustand = umschalten(zustand)
        anzeigen(zustand)
    time.sleep_ms(20)                  # entprellt nebenbei
```
{{% /tab %}}
{{% tab title="ESP32" %}}
**Aufbau:** Taste zwischen **GPIO 4** und **GND**. LED: Onboard an GPIO 2 oder extern an GPIO 18.

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)
taste = Pin(4, Pin.IN, Pin.PULL_UP)    # nicht gedrückt = 1, gedrückt = 0
vorher = 1


def gedrueckt():
    """True nur in dem Moment, in dem die Taste hinuntergeht."""
    global vorher
    jetzt = taste.value()
    neu = vorher == 1 and jetzt == 0
    vorher = jetzt
    return neu


def umschalten(zustand):
    if zustand == "AUS":
        return "AN"
    return "AUS"


def anzeigen(zustand):
    led.value(1 if zustand == "AN" else 0)


zustand = "AUS"
anzeigen(zustand)

while True:
    if gedrueckt():
        zustand = umschalten(zustand)
        anzeigen(zustand)
    time.sleep_ms(20)                  # entprellt nebenbei
```
{{% /tab %}}
{{% tab title="Arduino" %}}
Code wie im ESP32-Tab, Pins anpassen (siehe [MicroPython-Boards]({{% relref "werkzeuge/micropython-boards" %}})). UNO R3: [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) mit ESP32.
{{% /tab %}}
{{< /tabs >}}

{{% expand title="Warum `gedrueckt()` und nicht einfach `taste.value() == 0`?" %}}
Die Schleife läuft 50-mal pro Sekunde. Ein Tastendruck dauert etwa 0,2 s, also würde `taste.value() == 0` zehnmal hintereinander zutreffen und die LED zehnmal umschalten. `gedrueckt()` merkt sich in `vorher` den letzten Wert und meldet nur den **Wechsel** von „oben" (1) auf „unten" (0). Das nennt man **Flankenerkennung**. `global vorher` erlaubt der Funktion, die Variable außerhalb zu verändern. Beim micro:bit erledigt das `was_pressed()` für dich.
{{% /expand %}}

**Ändere es:** Übernimm deinen dritten Zustand `BLINKEN` aus Teil 2. Tipp: Im Zustand BLINKEN schaltest du die LED in jedem Schleifendurchlauf um, wenn seit dem letzten Umschalten 300 ms vergangen sind (`time.ticks_ms()`, beim micro:bit `running_time()`).

### 4d · Ohne PC starten (5 min)

Ein Gadget soll auch ohne Laptop laufen. Speichere das Programm in Thonny mit **Datei → Speichern unter → MicroPython-Gerät** als **`main.py`**. Nach dem nächsten Einstecken (auch an einer Powerbank) startet es automatisch. Beim micro:bit: **Flash**/**Send to micro:bit** im Editor.

Videos zum Nachschauen (Pico: externe LED und Taste auslesen, ESP32: erster Einstieg mit Thonny):

{{< youtube DaZF-3jM69U >}}

{{< youtube HTlIg6IqNzA >}}

{{< youtube 59S53NSHR0M >}}

## 5. Ins Team-Repository (5 min)

Lade euren Board-Code ins Team-Repository hoch (**Add file → Upload files**), z. B. als `code/main.py`. Kanban-Board aktualisieren: Was ist **fertig**?

## 6. Journalauftrag 3 (10 min)

{{% notice style="primary" title="Journalauftrag 3 · Erstes Lebenszeichen" icon="book" %}}
```markdown
# P1 · Woche 3 · <Datum>

## Aufbau
Foto von eurem Board mit LED und Taste (oder Screenshot aus dem Simulator).
Welche Pins habt ihr verwendet?

## Funktion erklärt
Kopiere eine Funktion aus eurem Code hierher (als ```python-Block)
und erkläre in 2–3 Sätzen: Welche Parameter bekommt sie,
was gibt sie zurück, warum ist sie eine eigene Funktion?

## Problem und Lösung
Was hat nicht auf Anhieb funktioniert, und wie habt ihr es gelöst?
```
{{% /notice %}}

Commit-Nachricht: `P1 Woche 3: Board läuft`.

## Quiz

{{< quiz title="Quiz · Woche 3" >}}
{{< question correct="2" >}}
Was gibt dieses Programm aus?

```python
def doppelt(x):
    return 2 * x

print(doppelt(3) + 1)
```
---
`8`
`7`
`2 * 3 + 1`
Nichts, weil `doppelt` nichts ausgibt.
---
`doppelt(3)` liefert 6 zurück, plus 1 ergibt 7. `return` gibt einen Wert zurück, ausgegeben wird er erst durch `print`.
{{< /question >}}
{{< question correct="3" >}}
`farben = ["rot", "grün", "blau"]`. Was ist `farben[1]`?
---
`"rot"`
`"blau"`
`"grün"`
ein Fehler
---
Der Index beginnt bei 0: `farben[0]` ist `"rot"`, `farben[1]` ist `"grün"`.
{{< /question >}}
{{< question correct="1" >}}
`i = 3` und die Liste hat 4 Elemente. Was ergibt `(i + 1) % 4`?
---
0
4
1
3
---
4 geteilt durch 4 ist 1 Rest **0**. So springt der Index vom letzten Element zurück zum ersten.
{{< /question >}}
{{< question correct="4" >}}
Eine Taste hängt zwischen Pin und GND, der Pin ist mit `Pin.PULL_UP` konfiguriert. Welchen Wert liefert `taste.value()`, während die Taste gedrückt ist?
---
1
`True`
Das hängt von der Taste ab.
0
---
Der Pull-up-Widerstand zieht den Pin auf 1, solange nichts passiert. Die gedrückte Taste verbindet den Pin mit GND, also 0.
{{< /question >}}
{{< question correct="2" >}}
Warum trennen wir `umschalten(zustand)` von `anzeigen(zustand)`?
---
Weil Python das so verlangt.
Damit die Logik auf PC und Board gleich bleibt und ohne Hardware getestet werden kann.
Damit das Programm schneller läuft.
Weil eine Funktion höchstens drei Zeilen haben darf.
---
Nur `anzeigen` hängt von der Hardware ab. Die Logik lässt sich unverändert weiterverwenden und prüfen.
{{< /question >}}
{{< /quiz >}}

## Bis nächste Woche

- Journalauftrag 3 committen.
- Im Team: Welcher **Sensor** und welcher **Aktor** (Summer, Servo, Display, …) gehört zu eurem Gadget? Bauteil bei der Lehrkraft reservieren.
- Nächste Woche ist das **Sprint-Review 1**: Euer Board soll dann mindestens eine Muss-Story vorführen können.
