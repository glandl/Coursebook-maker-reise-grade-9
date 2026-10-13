+++
title = "MicroPython-Boards (micro:bit, Pico, ESP32, Arduino)"
weight = 2
+++

**MicroPython** ist Python für kleine Computer ohne Bildschirm und Tastatur, sogenannte **Mikrocontroller**. Du schreibst denselben Python-Code wie am PC (`if`, `while`, Funktionen, Listen), dazu kommen Module wie `machine` oder `microbit`, mit denen du Pins, LEDs und Sensoren ansprichst. Programmiert wird in [Thonny]({{% relref "werkzeuge/python-thonny" %}}), das Board hängt per USB am PC.

Diese Seite brauchst du ab **P1 Woche 3**. Kein Board zur Hand? Derselbe Code läuft im [Wokwi-Simulator]({{% relref "werkzeuge/wokwi-simulator" %}}).

## Welches Board habe ich?

| Board | Woran du es erkennst | MicroPython? |
|-------|----------------------|--------------|
| **micro:bit** | Taschengroß, 5×5-LED-Anzeige, Tasten A und B. **V2** hat ein goldenes Logo zum Antippen und einen Lautsprecher auf der Rückseite. | ja |
| **Raspberry Pi Pico** | Grüne Leiste, Aufdruck „Raspberry Pi Pico“ (**Pico W** / **Pico 2 W** mit silbernem WLAN-Chip-Deckel), Taste **BOOTSEL**. | ja |
| **ESP32** | Meist schwarzes Board mit silbernem Metalldeckel „ESP32-WROOM“, zwei Tasten **EN** und **BOOT**. Viele Hersteller, Pins unterschiedlich beschriftet. | ja |
| **Arduino Nano ESP32** | Kleines Arduino-Board, Aufdruck „Nano ESP32“. | ja |
| **Arduino UNO R3 / UNO R4** | Großes Arduino-Board mit Buchsenleisten. | **nein**, siehe Tab „Arduino“ |

Welche Stärken die Boards haben, steht in [Woche 2]({{% relref "projekte/p1-code-gadget/woche-02-anforderungen" %}}).

## Was du brauchst

- Ein **USB-Datenkabel**. Viele Kabel aus Handy-Ladegeräten können nur laden, keine Daten übertragen. Wird das Board nicht erkannt, ist das die häufigste Ursache. Markiere funktionierende Kabel mit Klebeband.
- Für Pico, ESP32 und Nano ESP32: ein **Steckbrett** (Breadboard), **Steckkabel**, LEDs, **Widerstände** 220 Ω und 10 kΩ, eine **Taste**.
- Für micro:bit: nichts, alles Nötige ist eingebaut. Für eigene Bauteile **Krokodilklemmen** oder ein **Edge-Connector-Breakout**.

## Teil 1 · MicroPython aufspielen und mit Thonny verbinden

Das musst du **einmal pro Board** machen. Danach genügt: Board anstecken, Thonny starten.

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
**Mit Thonny:**

1. micro:bit per USB anschließen. Am PC erscheint ein Laufwerk **MICROBIT**.
2. Thonny: **Werkzeuge → Optionen → Interpreter** → **MicroPython (BBC micro:bit)**.
3. Unten rechts **Install or update MicroPython** klicken, das Laufwerk MICROBIT wählen, **Install**. Die gelbe LED auf der Rückseite blinkt, dann startet das Board neu.
4. **OK**. In der Shell erscheint `>>>`. Test:

```python
from microbit import *
display.scroll("Hallo")
```

**Ohne Installation (Browser):** [python.microbit.org](https://python.microbit.org/) öffnen, Code schreiben, mit **Send to micro:bit** übertragen (Chrome oder Edge, verbindet sich direkt über USB). In anderen Browsern **Save** klicken und die `.hex`-Datei auf das Laufwerk MICROBIT ziehen. Der Editor hat einen eingebauten Simulator, siehe [Wokwi & Browser-Simulatoren]({{% relref "werkzeuge/wokwi-simulator" %}}).

{{% notice style="info" title="Thonny oder Browser-Editor?" %}}
Beides funktioniert mit demselben Code. **Thonny** brauchst du für den **Plotter** (Woche 4) und um mehrere Dateien wie `hardware.py` aufs Board zu legen. Der **Browser-Editor** ist ideal für zu Hause und zum Ausprobieren im Simulator.
{{% /notice %}}
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
1. Taste **BOOTSEL** gedrückt halten, **dann** das USB-Kabel einstecken, dann loslassen. Am PC erscheint ein Laufwerk **RPI-RP2** (Pico 2: **RP2350**).
2. Thonny: **Werkzeuge → Optionen → Interpreter** → **MicroPython (Raspberry Pi Pico)**.
3. Unten rechts **Install or update MicroPython** klicken.
4. **Target volume:** das Laufwerk RPI-RP2. **Variant:** genau dein Modell wählen: *Pico / Pico H*, *Pico W / Pico WH*, *Pico 2* oder *Pico 2 W*. Die falsche Variante läuft, aber ohne WLAN oder gar nicht.
5. **Install**. Nach dem Kopieren verschwindet das Laufwerk, das Board startet neu.
6. Fenster schließen, **OK**. In der Shell erscheint `>>>`. Test:

```python
from machine import Pin
Pin("LED", Pin.OUT).value(1)    # Onboard-LED leuchtet
```

Treiber sind unter Windows 10/11, macOS und Linux **nicht** nötig.
{{% /tab %}}
{{% tab title="ESP32" %}}
1. ESP32 per USB anschließen.
2. **Treiber prüfen (nur Windows, nur beim ersten Mal):** Im Geräte-Manager unter *Anschlüsse (COM & LPT)* muss ein neuer **COM-Port** erscheinen. Fehlt er, auf den kleinen Chip neben der USB-Buchse schauen und den Treiber installieren:
   - Aufdruck **CP210x** (Silicon Labs) → [CP210x-Treiber](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers)
   - Aufdruck **CH340** / **CH9102** (WCH) → [CH340-Treiber](https://www.wch-ic.com/downloads/CH341SER_EXE.html)
3. Thonny: **Werkzeuge → Optionen → Interpreter** → **MicroPython (ESP32)**, bei *Port* den neuen Port wählen (`COM3`, `/dev/ttyUSB0`, `/dev/cu.usbserial-…`).
4. Unten rechts **Install or update MicroPython (esptool)** klicken.
5. **Target port:** dein Port. **MicroPython family:** *ESP32*. **Variant:** *Espressif • ESP32 / WROOM*. Hast du ein ESP32-**S3** oder **C3**, die passende Familie wählen.
6. **Install**. Bleibt es bei `Connecting...` hängen: Taste **BOOT** gedrückt halten, bis Prozentzahlen erscheinen.
7. Fenster schließen, **OK**. In der Shell erscheint `>>>`. Test:

```python
from machine import Pin
Pin(2, Pin.OUT).value(1)        # Onboard-LED (bei den meisten DevKits)
```

{{% notice style="warning" title="Linux: Zugriff verweigert" %}}
Meldet Thonny `Permission denied: '/dev/ttyUSB0'`, einmal `sudo usermod -a -G dialout $USER` ausführen und dich ab- und wieder anmelden. Verschwindet der Port unter Ubuntu sofort wieder, stört das Paket `brltty`: `sudo apt remove brltty`.
{{% /notice %}}
{{% /tab %}}
{{% tab title="Arduino" %}}
**Arduino UNO R3 und UNO R4:** Für diese Boards gibt es **kein offizielles MicroPython**. Der Kurs ist in Python, darum gibt es zwei Wege:

1. **Simulator:** In [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) ein **ESP32**-Projekt anlegen und den ESP32-Code des Kurses verwenden. Das ist gleichwertig: Ihr baut dieselbe Schaltung virtuell auf.
2. **Board tauschen:** ESP32, Pico oder **Arduino Nano ESP32** bei der Lehrkraft holen.

**Arduino Nano ESP32:**

1. [Arduino MicroPython Installer](https://labs.arduino.cc/en/labs/micropython-installer) laden und starten.
2. Nano ESP32 anschließen. Erkennt der Installer das Board nicht: **Reset**-Taste zweimal schnell hintereinander drücken.
3. Board auswählen, **Install MicroPython**.
4. Thonny: **Werkzeuge → Optionen → Interpreter** → **MicroPython (ESP32)**, Port wählen, **OK**. Test:

```python
from machine import Pin
Pin(48, Pin.OUT).value(1)       # Onboard-LED (D13)
```

Code wie im ESP32-Tab, aber mit **anderen Pinnummern**, siehe Teil 3.
{{% /tab %}}
{{< /tabs >}}

## Teil 2 · Arbeiten mit dem Board in Thonny

Sobald Thonny mit dem Board verbunden ist, gilt:

- Die **Shell** spricht mit dem **Board**. `print(1 + 1)` rechnet der Mikrocontroller.
- **▶ Play (F5)** schickt die Datei im Editor zum Board und führt sie dort aus. Sie wird dabei **nicht** gespeichert: Nach dem Abstecken ist sie weg.
- **■ Stopp** (oder **Strg+C** in der Shell) bricht das Programm ab. Ein zweiter Klick auf Stopp startet das Board neu (Soft-Reset).

### Dateien auf dem Board

**Ansicht → Dateien** zeigt oben die Dateien auf deinem PC, unten (Überschrift **MicroPython device**) die Dateien auf dem Board.

| Was | Wie |
|-----|-----|
| Datei aufs Board speichern | **Datei → Speichern unter → MicroPython device**, Namen eintippen |
| Datei vom PC hochladen | Oben im Dateien-Bereich (PC) Rechtsklick auf die Datei → **Upload nach /** |
| Datei vom Board holen | Rechtsklick auf die Datei auf dem Gerät → **Download nach …** |
| Datei löschen | Rechtsklick → **Löschen** |

Zwei Dateinamen haben eine besondere Bedeutung:

| Datei | Bedeutung |
|-------|-----------|
| **`main.py`** | Startet automatisch, sobald das Board Strom bekommt, auch an einer Powerbank. Das ist euer Gadget-Programm. |
| `boot.py` | Startet noch vor `main.py`. Im Kurs nicht verändern. |

Eigene Module wie **`hardware.py`** (ab Woche 4) müssen **auf dem Board** liegen, damit `import hardware` funktioniert.

{{% notice style="tip" title="Der Code gehört ins Repository, nicht nur aufs Board" %}}
Das Board ist kein Speicherort. Speichere jede Datei auch auf dem PC und lade sie ins Team-Repository hoch. Ein Board kann verloren gehen, getauscht oder neu bespielt werden.
{{% /notice %}}

## Teil 3 · Pinbelegung und Kurs-Verkabelung

Alle Programme im Kurs verwenden dieselbe Verkabelung pro Board. Halte dich daran, dann laufen die Beispiele ohne Änderung.

{{% notice style="warning" title="Strom aus beim Stecken" %}}
- Bauteile nur stecken oder umstecken, wenn das USB-Kabel **abgezogen** ist.
- Alle Boards arbeiten mit **3,3 V**. Niemals **5 V** an einen Eingangspin legen.
- LEDs immer mit **Vorwiderstand** (220 Ω). Das **lange Bein** der LED zeigt zum Pin, das kurze zu GND.
- **3V3** und **GND** nie direkt verbinden (Kurzschluss).
{{% /notice %}}

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
Für P1 ist **nichts zu verkabeln**: Tasten A/B, 5×5-Anzeige, Lichtsensor (die Anzeige selbst), Beschleunigungssensor, Temperatur, Mikrofon und Lautsprecher (V2) sind eingebaut.

| Kurs-Funktion | micro:bit |
|---------------|-----------|
| Taste | `button_a`, `button_b` |
| LED | Pixel auf `display` |
| Summer | eingebauter Lautsprecher, `music.pitch(...)` |
| Lichtsensor | `display.read_light_level()` (0–255) |
| Lage | `accelerometer.get_x()` |

**Eigene Bauteile** schließt du mit Krokodilklemmen an die großen Ringe **0**, **1**, **2**, **3V** und **GND** an:

```python
from microbit import *

pin0.write_digital(1)        # externe LED an Pin 0 (mit 220 Ω) ein
wert = pin1.read_analog()    # Analogwert an Pin 1, 0–1023
print(wert)
```

Die kleinen Pins am Rand erreichst du nur mit einem Breakout-Board. Viele davon gehören zur LED-Anzeige. Bleib bei 0, 1 und 2.
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
**Achtung:** Die Zahl im Code ist die **GP-Nummer**, nicht die Nummer des Beinchens. `Pin(15)` ist **GP15**, das ist Beinchen 20.

| Kurs-Funktion | GP-Pin | Beinchen | Anschluss |
|---------------|--------|----------|-----------|
| Taste | **GP14** | 19 | Taste zwischen GP14 und GND (Beinchen 18) |
| LED | **GP15** | 20 | GP15 → 220 Ω → LED langes Bein, kurzes Bein → GND |
| Onboard-LED | `"LED"` | – | eingebaut, keine Verkabelung |
| Summer (passiv) | **GP16** | 21 | GP16 → Summer → GND (Beinchen 23) |
| Lichtsensor / Poti | **GP26** (ADC0) | 31 | 3V3 → LDR → GP26 → 10 kΩ → GND |
| 3,3 V | 3V3(OUT) | 36 | Plus für Sensoren |
| GND | GND | 3, 8, 13, 18, 23, 28, 33, 38 | jeder GND ist gleich |

**Analoge Eingänge** gibt es nur an **GP26**, **GP27** und **GP28**. Offizielles Pinout zum Ausdrucken: [Pico](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf), [Pico W](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf).

Das Steckbrett: Die Pico sitzt über der Mittelrille, jede Fünferreihe neben einem Beinchen ist mit diesem verbunden. Die langen Leisten am Rand (rot/blau) eignen sich für 3V3 und GND.
{{% /tab %}}
{{% tab title="ESP32" %}}
Gilt für das verbreitete **ESP32-DevKit** (30 oder 38 Pins). Die Zahl im Code ist die **GPIO-Nummer**, auf dem Board meist als `D18`, `G18`, `IO18` oder nur `18` aufgedruckt.

| Kurs-Funktion | GPIO | Anschluss |
|---------------|------|-----------|
| Taste | **4** | Taste zwischen GPIO 4 und GND |
| LED | **18** | GPIO 18 → 220 Ω → LED langes Bein, kurzes Bein → GND |
| Onboard-LED | **2** | eingebaut bei den meisten DevKits (nicht bei allen) |
| Summer (passiv) | **19** | GPIO 19 → Summer → GND |
| Lichtsensor / Poti | **34** | 3V3 → LDR → GPIO 34 → 10 kΩ → GND |

**Pins mit Haken:**

| Pins | Hinweis |
|------|---------|
| 6–11 | **Nie verwenden**, gehören zum internen Speicher. |
| 0, 2, 12, 15 | Beeinflussen den Start. Nur verwenden, wenn nötig (GPIO 2 für die Onboard-LED ist in Ordnung). |
| 34, 35, 36 (VP), 39 (VN) | **Nur Eingang**, kein `Pin.PULL_UP`. Gut für Sensoren, schlecht für Tasten. |
| 32–39 | Analoge Eingänge, die auch mit **WLAN** funktionieren (wichtig für P2). Andere ADC-Pins (z. B. 25, 26, 27) gehen nicht, solange WLAN aktiv ist. |

Analog-Eingänge immer mit `adc.atten(ADC.ATTN_11DB)` einstellen, sonst endet der Messbereich bei ca. 1 V.
{{% /tab %}}
{{% tab title="Arduino" %}}
**Arduino Nano ESP32:** Auf dem Board stehen Arduino-Namen (`D2`, `A0`), MicroPython verwendet aber die **GPIO-Nummern** des ESP32-S3. Übersetzung:

| Arduino | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 |
|---------|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|
| **GPIO** | 44 | 43 | 5 | 6 | 7 | 8 | 9 | 10 | 17 | 18 | 21 | 38 | 47 | 48 |

| Arduino | A0 | A1 | A2 | A3 | A4 | A5 | A6 | A7 |
|---------|----|----|----|----|----|----|----|----|
| **GPIO** | 1 | 2 | 3 | 4 | 11 | 12 | 13 | 14 |

**Kurs-Verkabelung** (so ändert sich am ESP32-Code möglichst wenig):

| Kurs-Funktion | Anschluss am Nano | im Code | Unterschied zum ESP32-Code |
|---------------|-------------------|---------|----------------------------|
| Taste | **A3** ↔ GND | `Pin(4, …)` | keiner |
| LED | **D9** → 220 Ω → LED → GND | `Pin(18, …)` | keiner |
| Onboard-LED | D13 | `Pin(48, …)` | statt 2 |
| Summer | **D8** → Summer → GND | `PWM(Pin(17))` | statt 19 |
| Lichtsensor / Poti | 3V3 → LDR → **A0** → 10 kΩ → GND | `ADC(Pin(1))` | statt 34 |

In `hardware.py` (Woche 4) änderst du also nur die Zahlen 19 → 17 und 34 → 1. Das Board arbeitet mit **3,3 V**, nicht mit 5 V wie der UNO.

**UNO R3 / UNO R4:** kein MicroPython, siehe Teil 1.
{{% /tab %}}
{{< /tabs >}}

### Taste richtig stecken

Eine Taste mit vier Beinchen verbindet immer zwei Paare. Sicher funktioniert es, wenn du **zwei diagonal gegenüberliegende** Beinchen verwendest. Die Taste sitzt über der Mittelrille des Steckbretts.

## Teil 4 · Weitere Bauteile

Für euer Gadget braucht ihr vielleicht mehr als LED, Taste und Lichtsensor. Jedes Bauteil wird in `hardware.py` zu **einer kleinen Funktion**, der Rest des Codes bleibt gleich (siehe [Woche 4]({{% relref "projekte/p1-code-gadget/woche-04-sensoren-review" %}})).

Vorgeschlagene Pins, die sich mit der Kurs-Verkabelung nicht überschneiden:

| Bauteil | Pico | ESP32 | Nano ESP32 | Strom |
|---------|------|-------|------------|-------|
| Bewegungsmelder (PIR, HC-SR501) | GP17 | 27 | D4 → 7 | 5 V |
| Ultraschall-Abstand: Trig | GP18 | 25 | D5 → 8 | 5 V (HC-SR04) / 3,3 V (HC-SR04**P**) |
| Ultraschall-Abstand: Echo | GP19 | 26 | D6 → 9 | siehe Warnung |
| Servo (SG90) | GP20 | 13 | D7 → 10 | 5 V |
| Temperatur/Feuchte (DHT11/DHT22) | GP21 | 33 | D10 → 21 | 3,3 V |
| OLED-Display (I²C): SDA / SCL | GP4 / GP5 | 21 / 22 | A4 → 11 / A5 → 12 | 3,3 V |
| zweiter Analogwert | GP27 | 35 | A1 → 2 | 3,3 V |

**5 V** gibt es am Pin **VBUS** (Pico, Beinchen 40), **5V/VIN** (ESP32) bzw. **VBUS** (Nano ESP32), solange das Board per USB versorgt wird.

In den Beispielen unten stehen die **Pico**-Pins. Für andere Boards die Zahl aus der Tabelle einsetzen. Auf dem micro:bit sind die meisten dieser Bauteile umständlich (wenige Pins, keine 5 V). Dort besser die eingebauten Sensoren nutzen.

{{% expand title="Bewegungsmelder (PIR)" %}}
Der PIR liefert 1, solange er Bewegung erkennt. Mit den zwei Drehreglern stellst du Empfindlichkeit und Haltezeit ein. Nach dem Einschalten braucht er etwa eine Minute zum Kalibrieren.

```python
from machine import Pin

_pir = Pin(17, Pin.IN)


def bewegung():
    """True, solange Bewegung erkannt wird."""
    return _pir.value() == 1
```
{{% /expand %}}

{{% expand title="Ultraschall-Abstandssensor (HC-SR04)" %}}
{{% notice style="warning" title="5-V-Signal" %}}
Der klassische **HC-SR04** braucht 5 V und sendet auf **Echo** ein 5-V-Signal. Das kann den 3,3-V-Pin beschädigen. Entweder einen **Spannungsteiler** einbauen (Echo → 1 kΩ → Pin → 2 kΩ → GND) oder die Variante **HC-SR04P** bzw. **RCWL-1601** verwenden, die mit 3,3 V läuft.
{{% /notice %}}

```python
from machine import Pin, time_pulse_us
import time

_trig = Pin(18, Pin.OUT)
_echo = Pin(19, Pin.IN)


def abstand_cm():
    """Abstand in cm, oder -1 wenn nichts gemessen wurde."""
    _trig.value(0)
    time.sleep_us(2)
    _trig.value(1)
    time.sleep_us(10)
    _trig.value(0)
    dauer = time_pulse_us(_echo, 1, 30000)   # höchstens 30 ms warten
    if dauer < 0:
        return -1
    return dauer * 0.0343 / 2                 # Schall: 343 m/s, hin und zurück
```
{{% /expand %}}

{{% expand title="Servo (SG90)" %}}
Braun = GND, Rot = **5 V**, Orange = Signal. Ein Servo zieht viel Strom: Startet das Board neu, sobald sich der Servo bewegt, reicht die USB-Versorgung nicht. Dann den Servo über eine eigene Stromquelle versorgen (GND verbinden).

```python
from machine import Pin, PWM

_servo = PWM(Pin(20))
_servo.freq(50)


def servo(winkel):
    """Dreht den Servo auf 0–180 Grad."""
    # 0,5 ms (0°) bis 2,5 ms (180°) von 20 ms
    _servo.duty_u16(1638 + winkel * (8192 - 1638) // 180)
```
{{% /expand %}}

{{% expand title="Temperatur und Luftfeuchte (DHT11 / DHT22)" %}}
Das Modul `dht` ist bei Pico und ESP32 schon dabei. Der Sensor darf höchstens **einmal pro Sekunde** (DHT22: alle 2 s) abgefragt werden.

```python
from machine import Pin
import dht

_dht = dht.DHT11(Pin(21))      # beim DHT22: dht.DHT22(...)


def temperatur():
    _dht.measure()
    return _dht.temperature()   # °C


def feuchte():
    _dht.measure()
    return _dht.humidity()      # %
```
{{% /expand %}}

{{% expand title="OLED-Display (SSD1306, 128×64, I²C)" %}}
Den Treiber einmal aufs Board installieren: Thonny **Werkzeuge → Verwalte Pakete …**, nach `ssd1306` suchen, **Installieren**.

```python
from machine import Pin, I2C
import ssd1306

_i2c = I2C(0, sda=Pin(4), scl=Pin(5))     # ESP32: I2C(0, sda=Pin(21), scl=Pin(22))
_oled = ssd1306.SSD1306_I2C(128, 64, _i2c)


def anzeigen_text(zeile1, zeile2=""):
    _oled.fill(0)
    _oled.text(zeile1, 0, 0)
    _oled.text(zeile2, 0, 16)
    _oled.show()
```

Meldet `I2C(...)` einen Fehler oder bleibt das Display dunkel: `print(_i2c.scan())` muss `[60]` ausgeben. Eine leere Liste heißt: SDA/SCL vertauscht oder nicht verbunden.
{{% /expand %}}

## Fehlerbehebung

| Problem | Wahrscheinliche Ursache | Lösung |
|---------|-------------------------|--------|
| Thonny findet kein Gerät, kein Port in der Liste | Ladekabel statt Datenkabel, Treiber fehlt (ESP32) | anderes Kabel, anderer USB-Anschluss, Treiber aus Teil 1 |
| `Device is busy or does not respond` | `main.py` läuft in einer Endlosschleife | mehrmals **Stopp** drücken. Hilft das nicht: abstecken, einstecken, sofort Stopp |
| `ImportError: no module named 'hardware'` | `hardware.py` liegt nur am PC | Datei **auf das Board** speichern (Teil 2) |
| `ValueError: invalid pin` | Beinchen-Nummer statt GP-/GPIO-Nummer | Pinout prüfen (Teil 3) |
| LED bleibt dunkel | LED verkehrt herum, falscher Pin, GND fehlt | langes Bein zum Pin, Verkabelung mit Tabelle vergleichen |
| Taste liefert immer 0 oder immer 1 | `Pin.PULL_UP` fehlt, Taste falsch gedreht, Pin 34–39 am ESP32 | Pull-up setzen, diagonale Beinchen, anderen Pin |
| Analogwert immer 0 oder immer Maximum | falscher Pin, kein ADC-Pin, `atten` fehlt (ESP32) | Pico: GP26–28. ESP32: 32–39 mit `ATTN_11DB` |
| Board startet neu, wenn Summer/Servo/Motor anläuft | USB liefert zu wenig Strom | eigene Stromversorgung für den Verbraucher |
| Programm läuft nicht ohne PC | Datei heißt nicht `main.py` oder liegt nur am PC | als `main.py` aufs Board speichern |
| micro:bit: Laufwerk heißt **MAINTENANCE** | Reset beim Einstecken gedrückt | abstecken, ohne Taste wieder einstecken |

{{% notice style="tip" title="Wenn gar nichts mehr geht" %}}
MicroPython einfach **neu aufspielen** (Teil 1). Das löscht alle Dateien auf dem Board. Darum gehört der Code ins Repository.
{{% /notice %}}

## Weiterlesen

- [MicroPython-Dokumentation](https://docs.micropython.org/en/latest/) (englisch): *Quick reference* für [RP2/Pico](https://docs.micropython.org/en/latest/rp2/quickref.html) und [ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)
- [micro:bit-MicroPython-Dokumentation](https://microbit-micropython.readthedocs.io/)
- [Arduino Nano ESP32 und MicroPython](https://docs.arduino.cc/micropython/)
