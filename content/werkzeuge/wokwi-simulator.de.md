+++
title = "Wokwi & Browser-Simulatoren"
weight = 3
+++

Ein **Simulator** zeigt im Browser ein virtuelles Board mit LEDs, Tasten und Sensoren. Dein MicroPython-Code läuft darin **genauso wie auf dem echten Board**. Du brauchst nichts zu installieren, nur einen Browser.

| Simulator | Boards | Wofür |
|-----------|--------|-------|
| [**Wokwi**](https://wokwi.com/) | Raspberry Pi Pico, ESP32 | eigene Schaltungen mit Steckbrett-Bauteilen, `hardware.py`, später WLAN (P2) |
| [**python.microbit.org**](https://python.microbit.org/) | micro:bit | Editor und Simulator in einem, Sensoren per Schieberegler |

## Wann simulieren?

Der Simulator ist **kein Notbehelf**, sondern ein gleichwertiges Werkzeug:

- **Kein Board da:** zu Hause, bei Krankheit, wenn das Team-Board gerade bei jemand anderem liegt.
- **Arduino UNO R3 / R4:** Diese Boards können kein MicroPython. Euer Team baut die Schaltung in Wokwi mit einem **ESP32** auf (siehe [MicroPython-Boards]({{% relref "werkzeuge/micropython-boards" %}})).
- **Vor dem Verkabeln:** Schaltung erst virtuell aufbauen und testen. Was im Simulator nicht geht, geht auf dem Steckbrett auch nicht.
- **Zum Teilen:** Ein Wokwi-Link zeigt Code **und** Schaltung. Ideal fürs Team-Repository und für Fragen an die Lehrkraft.

## Teil 1 · Wokwi: Projekt starten

1. Leeres MicroPython-Projekt öffnen:
   - [Neues Pico-Projekt (MicroPython)](https://wokwi.com/projects/new/micropython-pi-pico)
   - [Neues ESP32-Projekt (MicroPython)](https://wokwi.com/projects/new/micropython-esp32)
2. **Links** ist der Code (`main.py`) und die Schaltungsbeschreibung (`diagram.json`), **rechts** die Simulation.
3. Den grünen **▶-Knopf** über der Simulation drücken. Das Programm startet, Ausgaben von `print` erscheinen in der Konsole unten rechts.
4. **■** beendet die Simulation. Änderst du den Code, startet ▶ ihn neu.

Probier es aus, ohne etwas zu verkabeln (Pico, Onboard-LED):

```python
from machine import Pin
import time

led = Pin("LED", Pin.OUT)       # funktioniert "LED" nicht: Pin(25, Pin.OUT)

for i in range(10):
    led.value(not led.value())
    time.sleep(0.5)
print("Fertig")
```

Das ESP32-Board in Wokwi (DevKitC) hat **keine Onboard-LED**. Dort gleich eine externe LED an GPIO 18 anschließen, siehe Teil 3.

{{% notice style="tip" title="REPL in Wokwi" %}}
Ist `main.py` fertig, erscheint in der Konsole `>>>`. Dort kannst du wie in der Thonny-Shell einzelne Befehle ausprobieren. Läuft eine Endlosschleife, klick in die Konsole und drück **Strg+C**.
{{% /notice %}}

## Teil 2 · Bauteile hinzufügen und verdrahten

| Was | Wie |
|-----|-----|
| Bauteil hinzufügen | Blauer **+**-Knopf über der Simulation, Bauteil suchen (z. B. *LED*, *Resistor*, *Pushbutton*, *Buzzer*, *Potentiometer*, *Photoresistor*) |
| Bauteil verschieben | ziehen |
| Bauteil drehen | anklicken, **R** drücken |
| Eigenschaften (Farbe, Widerstandswert) | Bauteil anklicken, im Fenster ändern |
| Kabel ziehen | auf ein Beinchen klicken, dann auf das Ziel-Beinchen. Zwischenklicks setzen Knickpunkte. |
| Kabelfarbe | Kabel anklicken, Farbe wählen. Abmachung: **Schwarz = GND**, **Rot = 3V3** |
| Löschen | anklicken, **Entf** |

Fährst du mit der Maus über ein Beinchen, zeigt Wokwi seinen Namen (`GP15`, `GND.3`, `A`, `C`). Bei der LED ist **A** (Anode) das lange Bein (+), **C** (Kathode) das kurze.

Wokwi zeichnet nur, was in `diagram.json` steht. Mit dem Maus-Editor und mit dem Text in `diagram.json` änderst du also dasselbe.

## Teil 3 · Die Kurs-Verkabelung in Wokwi

Baue die Schaltung aus [Woche 3 und 4]({{% relref "projekte/p1-code-gadget/woche-04-sensoren-review" %}}) nach. Dann läuft `hardware.py` aus dem Kurs **ohne Änderung**.

{{< tabs groupid="board" >}}
{{% tab title="Raspberry Pi Pico" %}}
| Bauteil | Verbindung |
|---------|------------|
| Taste | GP14 ↔ GND |
| LED + Widerstand 220 Ω | GP15 → Widerstand → LED **A**, LED **C** → GND |
| Summer (Buzzer) | GP16 → Buzzer **2** (+), Buzzer **1** (−) → GND |
| Potentiometer (statt Lichtsensor) | **VCC** → 3V3, **SIG** → GP26, **GND** → GND |

**Abkürzung über `diagram.json`:** Öffne den Reiter `diagram.json`. Füge die folgenden Zeilen **direkt nach** `"parts": [` ein (vor dem Eintrag des Boards):

```json
    { "type": "wokwi-pushbutton", "id": "btn1", "top": 0, "left": 150, "attrs": { "color": "green" } },
    { "type": "wokwi-resistor", "id": "r1", "top": 80, "left": 150, "attrs": { "value": "220" } },
    { "type": "wokwi-led", "id": "led1", "top": 50, "left": 250, "attrs": { "color": "red" } },
    { "type": "wokwi-buzzer", "id": "bz1", "top": 140, "left": 150, "attrs": {} },
    { "type": "wokwi-potentiometer", "id": "pot1", "top": 240, "left": 150, "attrs": {} },
```

Und diese Zeilen **direkt nach** `"connections": [`:

```json
    [ "pico:GP14", "btn1:1.l", "green", [] ],
    [ "btn1:2.l", "pico:GND.4", "black", [] ],
    [ "pico:GP15", "r1:1", "orange", [] ],
    [ "r1:2", "led1:A", "orange", [] ],
    [ "led1:C", "pico:GND.5", "black", [] ],
    [ "pico:GP16", "bz1:2", "purple", [] ],
    [ "bz1:1", "pico:GND.6", "black", [] ],
    [ "pot1:VCC", "pico:3V3", "red", [] ],
    [ "pot1:SIG", "pico:GP26", "blue", [] ],
    [ "pot1:GND", "pico:GND.8", "black", [] ],
```

Danach zurück zur Simulation und die Bauteile mit der Maus ordentlich hinschieben.
{{% /tab %}}
{{% tab title="ESP32" %}}
| Bauteil | Verbindung |
|---------|------------|
| Taste | GPIO 4 ↔ GND |
| LED + Widerstand 220 Ω | GPIO 18 → Widerstand → LED **A**, LED **C** → GND |
| Summer (Buzzer) | GPIO 19 → Buzzer **2** (+), Buzzer **1** (−) → GND |
| Potentiometer (statt Lichtsensor) | **VCC** → 3V3, **SIG** → GPIO 34, **GND** → GND |

**Abkürzung über `diagram.json`:** Öffne den Reiter `diagram.json`. Füge die folgenden Zeilen **direkt nach** `"parts": [` ein (vor dem Eintrag des Boards):

```json
    { "type": "wokwi-pushbutton", "id": "btn1", "top": 0, "left": 200, "attrs": { "color": "green" } },
    { "type": "wokwi-resistor", "id": "r1", "top": 80, "left": 200, "attrs": { "value": "220" } },
    { "type": "wokwi-led", "id": "led1", "top": 50, "left": 300, "attrs": { "color": "red" } },
    { "type": "wokwi-buzzer", "id": "bz1", "top": 140, "left": 200, "attrs": {} },
    { "type": "wokwi-potentiometer", "id": "pot1", "top": 240, "left": 200, "attrs": {} },
```

Und diese Zeilen **direkt nach** `"connections": [`:

```json
    [ "esp:4", "btn1:1.l", "green", [] ],
    [ "btn1:2.l", "esp:GND.2", "black", [] ],
    [ "esp:18", "r1:1", "orange", [] ],
    [ "r1:2", "led1:A", "orange", [] ],
    [ "led1:C", "esp:GND.2", "black", [] ],
    [ "esp:19", "bz1:2", "purple", [] ],
    [ "bz1:1", "esp:GND.3", "black", [] ],
    [ "pot1:VCC", "esp:3V3", "red", [] ],
    [ "pot1:SIG", "esp:34", "blue", [] ],
    [ "pot1:GND", "esp:GND.1", "black", [] ],
```

Danach zurück zur Simulation und die Bauteile mit der Maus ordentlich hinschieben.

**Arduino-Teams (UNO R3 / R4)** verwenden genau diese ESP32-Schaltung.
{{% /tab %}}
{{< /tabs >}}

{{% notice style="warning" title="Fehler in diagram.json" %}}
Jeder Eintrag endet mit einem Komma, **außer dem letzten** in der Liste. War die Liste vorher leer (`[]`), lösch das Komma nach der letzten eingefügten Zeile. Wokwi unterstreicht Fehler rot. Heißt das Board in deiner Datei nicht `pico` bzw. `esp` (siehe `"id"` beim Board-Eintrag), ersetze den Namen in den Verbindungen.
{{% /notice %}}

### Lichtsensor statt Potentiometer

Wokwi hat ein Lichtsensor-Modul (*Photoresistor sensor*, Anschlüsse **VCC** → 3V3, **GND** → GND, **AO** → GP26 bzw. GPIO 34). Achtung: Bei diesem Modul **sinkt** der Wert, wenn es heller wird, also genau umgekehrt wie bei der Kurs-Schaltung. In `hardware.py` dann `100 - …` rechnen:

```python
def helligkeit():
    return 100 - _sensor.read_u16() * 100 // 65535
```

Für den Kurs ist das **Potentiometer** einfacher: drehen = heller/dunkler.

## Teil 4 · Mehrere Dateien: `hardware.py` und `main.py`

Ab [Woche 4]({{% relref "projekte/p1-code-gadget/woche-04-sensoren-review" %}}) besteht euer Programm aus mehreren Dateien. Wokwi legt **alle Dateien** des Projekts auf das virtuelle Board, `main.py` startet automatisch.

1. Neben den Datei-Reitern auf den kleinen **Pfeil ▾** klicken → **New file…**
2. Namen eintippen, z. B. `hardware.py`, Code einfügen.
3. In `main.py` wie gewohnt `import hardware`.

Mit demselben Menü kannst du Dateien **hochladen** (*Upload file(s)…*) und das ganze Projekt als ZIP **herunterladen**.

## Teil 5 · Während der Simulation

| Bauteil | So bedienst du es |
|---------|-------------------|
| Taste | anklicken und gedrückt halten. **Strg**/**Cmd**+Klick hält sie dauerhaft gedrückt. |
| Potentiometer | am Drehknopf ziehen, oder anklicken und **← →** drücken |
| Lichtsensor | anklicken, Schieberegler *lux* verschieben |
| Summer | Ton kommt aus dem Lautsprecher deines Computers (Lautstärke prüfen) |

Messwerte siehst du mit `print()` in der Konsole. Einen Plotter wie in Thonny gibt es in Wokwi nicht. Für den Schwellwert in Woche 4 genügen die Zahlen in der Konsole.

## Teil 6 · Speichern, teilen, abgeben

1. **Save** (oder **Strg+S**). Beim ersten Mal fragt Wokwi nach einer Anmeldung. Am einfachsten **mit GitHub anmelden**, das Konto hast du schon.
2. Nach dem Speichern hat das Projekt eine eigene Adresse, z. B. `https://wokwi.com/projects/123456789`. Diese Adresse ist dein **Link zum Teilen**.
3. Für das Team-Repository:
   - den **Wokwi-Link** in die `README.md` schreiben,
   - die Dateien (`main.py`, `hardware.py`, …) trotzdem **hochladen**, denn das Repository ist die Quelle, nicht Wokwi,
   - für das Journal einen **Screenshot** der Schaltung machen.

{{% notice style="info" title="Wer sieht mein Projekt?" %}}
Gespeicherte Wokwi-Projekte kann jede Person sehen, die den Link kennt. Schreib keine persönlichen Daten in Code oder Projektnamen. Ein guter Projektname: `p1-gadget-<teamname>`.
{{% /notice %}}

Arbeitet ihr zu zweit am selben Projekt: Wokwi kann nicht gleichzeitig bearbeitet werden. Eine Person speichert, die andere öffnet den Link und klickt **Save a copy**. Zusammengeführt wird der Code im Team-Repository.

## micro:bit: python.microbit.org

Der [micro:bit-Python-Editor](https://python.microbit.org/) hat den Simulator gleich eingebaut.

1. [python.microbit.org](https://python.microbit.org/) öffnen. Links Code schreiben.
2. Rechts den **▶-Knopf** über dem virtuellen micro:bit drücken.
3. Tasten **A** und **B** und das Logo im Bild anklicken.
4. Unter dem Simulator stellst du die **Sensoren** ein: Helligkeit, Temperatur, Lautstärke, Beschleunigung und Gesten (*shake*, *tilt*, …).
5. `print`-Ausgaben erscheinen unter dem Simulator (*Serial*).

Code für den Simulator ist **derselbe** wie für den echten micro:bit. Mit **Send to micro:bit** (Chrome/Edge) landet er direkt auf dem Board.

**Speichern:** Der Editor merkt sich dein Projekt im Browser, aber nur auf diesem Gerät. **Save** lädt eine `.hex`-Datei herunter (zum Weitergeben oder Flashen). Im Menü bei **Save** gibt es auch *Save Python script* für die `.py`-Datei. Die gehört ins Team-Repository.

**Mehrere Dateien:** Mit **Open…** eine weitere `.py`-Datei wie `hardware.py` öffnen und sie als **neue Datei zum Projekt hinzufügen**. Sie erscheint dann im Bereich *Project*.

## Grenzen des Simulators

Ein Simulator ist ein **Modell** der Wirklichkeit. Einiges bildet er nicht ab:

| Im Simulator | Auf dem echten Board |
|--------------|----------------------|
| Sensoren liefern exakte, ruhige Werte | Werte schwanken, Schwellwerte müsst ihr am Board noch einmal prüfen |
| Verkehrt gesteckte LED geht einfach nicht | dasselbe, aber ein Kurzschluss kann Bauteile **zerstören** |
| Strom ist unbegrenzt | Servos und Motoren können das Board neu starten lassen |
| Zeitverhalten ungefähr echt | Reaktionsspiele und Tonlängen können sich leicht anders anfühlen |
| WLAN über das Netz `Wokwi-GUEST` (ohne Passwort, nur ESP32 und Pico W) | echtes Schul-WLAN, siehe P2 |

Darum gilt: **Entwickeln im Simulator, Endabnahme am Board.** Arduino-Teams führen ihr Gadget beim Review in Wokwi vor.

## Andere Simulatoren

- [**Wokwi** mit Arduino UNO](https://wokwi.com/projects/new/arduino-uno): Hier programmierst du in **C++** statt Python. Nicht Teil von P1, nur für Neugierige.
- [**MakeCode**](https://makecode.microbit.org/): micro:bit mit Blöcken. Kennst du vielleicht aus der Unterstufe. Im Kurs schreiben wir Python.
