+++
title = "Wokwi & Browser Simulators"
weight = 3
+++

A **simulator** shows a virtual board with LEDs, buttons and sensors in the browser. Your MicroPython code runs in it **just like on the real board**. You don't need to install anything, only a browser.

| Simulator | Boards | Used for |
|-----------|--------|----------|
| [**Wokwi**](https://wokwi.com/) | Raspberry Pi Pico, ESP32 | your own circuits with breadboard components, `hardware.py`, later Wi-Fi (P2) |
| [**python.microbit.org**](https://python.microbit.org/) | micro:bit | editor and simulator in one, sensors via sliders |

## When to simulate?

The simulator is **not a stopgap** but an equivalent tool:

- **No board available:** at home, when ill, when the team board is with someone else.
- **Arduino UNO R3 / R4:** these boards cannot run MicroPython. Your team builds the circuit in Wokwi with an **ESP32** (see [MicroPython Boards]({{% relref "werkzeuge/micropython-boards" %}})).
- **Before wiring:** build and test the circuit virtually first. What does not work in the simulator will not work on the breadboard either.
- **For sharing:** a Wokwi link shows code **and** circuit. Ideal for the team repository and for questions to your teacher.

## Part 1 · Wokwi: start a project

1. Open an empty MicroPython project:
   - [New Pico project (MicroPython)](https://wokwi.com/projects/new/micropython-pi-pico)
   - [New ESP32 project (MicroPython)](https://wokwi.com/projects/new/micropython-esp32)
2. On the **left** is the code (`main.py`) and the circuit description (`diagram.json`), on the **right** the simulation.
3. Press the green **▶ button** above the simulation. The program starts, `print` output appears in the console at the bottom right.
4. **■** ends the simulation. If you change the code, ▶ restarts it.

Try it without wiring anything (Pico, onboard LED):

```python
from machine import Pin
import time

led = Pin("LED", Pin.OUT)       # if "LED" does not work: Pin(25, Pin.OUT)

for i in range(10):
    led.value(not led.value())
    time.sleep(0.5)
print("Done")
```

The ESP32 board in Wokwi (DevKitC) has **no onboard LED**. Connect an external LED to GPIO 18 right away, see part 3.

{{% notice style="tip" title="REPL in Wokwi" %}}
When `main.py` has finished, the console shows `>>>`. There you can try single commands like in the Thonny shell. If an endless loop is running, click into the console and press **Ctrl+C**.
{{% /notice %}}

## Part 2 · Adding and wiring components

| What | How |
|------|-----|
| Add a component | blue **+** button above the simulation, search for the component (e.g. *LED*, *Resistor*, *Pushbutton*, *Buzzer*, *Potentiometer*, *Photoresistor*) |
| Move a component | drag it |
| Rotate a component | click it, press **R** |
| Properties (colour, resistance) | click the component, change them in the pop-up |
| Draw a wire | click a pin, then the target pin. Clicks in between set bend points. |
| Wire colour | click the wire, choose a colour. Convention: **black = GND**, **red = 3V3** |
| Delete | click it, press **Delete** |

Hover over a pin and Wokwi shows its name (`GP15`, `GND.3`, `A`, `C`). On the LED, **A** (anode) is the long leg (+), **C** (cathode) the short one.

Wokwi only draws what is in `diagram.json`. So the mouse editor and the text in `diagram.json` change the same thing.

## Part 3 · The course wiring in Wokwi

Rebuild the circuit from [weeks 3 and 4]({{% relref "projekte/p1-code-gadget/woche-04-sensoren-review" %}}). Then the course's `hardware.py` runs **without changes**.

{{< tabs groupid="board" >}}
{{% tab title="Raspberry Pi Pico" %}}
| Component | Connection |
|-----------|------------|
| Button | GP14 ↔ GND |
| LED + resistor 220 Ω | GP15 → resistor → LED **A**, LED **C** → GND |
| Buzzer | GP16 → buzzer **2** (+), buzzer **1** (−) → GND |
| Potentiometer (instead of light sensor) | **VCC** → 3V3, **SIG** → GP26, **GND** → GND |

**Shortcut via `diagram.json`:** open the `diagram.json` tab. Insert the following lines **right after** `"parts": [` (before the board's entry):

```json
    { "type": "wokwi-pushbutton", "id": "btn1", "top": 0, "left": 150, "attrs": { "color": "green" } },
    { "type": "wokwi-resistor", "id": "r1", "top": 80, "left": 150, "attrs": { "value": "220" } },
    { "type": "wokwi-led", "id": "led1", "top": 50, "left": 250, "attrs": { "color": "red" } },
    { "type": "wokwi-buzzer", "id": "bz1", "top": 140, "left": 150, "attrs": {} },
    { "type": "wokwi-potentiometer", "id": "pot1", "top": 240, "left": 150, "attrs": {} },
```

And these lines **right after** `"connections": [`:

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

Then go back to the simulation and drag the components into a tidy layout.
{{% /tab %}}
{{% tab title="ESP32" %}}
| Component | Connection |
|-----------|------------|
| Button | GPIO 4 ↔ GND |
| LED + resistor 220 Ω | GPIO 18 → resistor → LED **A**, LED **C** → GND |
| Buzzer | GPIO 19 → buzzer **2** (+), buzzer **1** (−) → GND |
| Potentiometer (instead of light sensor) | **VCC** → 3V3, **SIG** → GPIO 34, **GND** → GND |

**Shortcut via `diagram.json`:** open the `diagram.json` tab. Insert the following lines **right after** `"parts": [` (before the board's entry):

```json
    { "type": "wokwi-pushbutton", "id": "btn1", "top": 0, "left": 200, "attrs": { "color": "green" } },
    { "type": "wokwi-resistor", "id": "r1", "top": 80, "left": 200, "attrs": { "value": "220" } },
    { "type": "wokwi-led", "id": "led1", "top": 50, "left": 300, "attrs": { "color": "red" } },
    { "type": "wokwi-buzzer", "id": "bz1", "top": 140, "left": 200, "attrs": {} },
    { "type": "wokwi-potentiometer", "id": "pot1", "top": 240, "left": 200, "attrs": {} },
```

And these lines **right after** `"connections": [`:

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

Then go back to the simulation and drag the components into a tidy layout.

**Arduino teams (UNO R3 / R4)** use exactly this ESP32 circuit.
{{% /tab %}}
{{< /tabs >}}

{{% notice style="warning" title="Errors in diagram.json" %}}
Every entry ends with a comma, **except the last one** in the list. If the list was empty before (`[]`), delete the comma after the last inserted line. Wokwi underlines errors in red. If the board in your file is not called `pico` or `esp` (see `"id"` in the board's entry), replace the name in the connections.
{{% /notice %}}

### Light sensor instead of potentiometer

Wokwi has a light sensor module (*Photoresistor sensor*, pins **VCC** → 3V3, **GND** → GND, **AO** → GP26 or GPIO 34). Careful: with this module the value **drops** when it gets brighter, exactly the opposite of the course circuit. Then calculate `100 - …` in `hardware.py`:

```python
def brightness():
    return 100 - _sensor.read_u16() * 100 // 65535
```

For the course the **potentiometer** is simpler: turn it = brighter/darker.

## Part 4 · Several files: `hardware.py` and `main.py`

From [week 4]({{% relref "projekte/p1-code-gadget/woche-04-sensoren-review" %}}) your program consists of several files. Wokwi copies **all files** of the project onto the virtual board, `main.py` starts automatically.

1. Next to the file tabs click the small **arrow ▾** → **New file…**
2. Type the name, e.g. `hardware.py`, paste the code.
3. In `main.py`, `import hardware` as usual.

The same menu lets you **upload** files (*Upload file(s)…*) and **download** the whole project as a ZIP.

## Part 5 · During the simulation

| Component | How to operate it |
|-----------|-------------------|
| Button | click and hold. **Ctrl**/**Cmd**+click keeps it pressed. |
| Potentiometer | drag the knob, or click it and press **← →** |
| Light sensor | click it, move the *lux* slider |
| Buzzer | sound comes from your computer's speaker (check the volume) |

You see readings with `print()` in the console. Wokwi has no plotter like Thonny. For the threshold in week 4 the numbers in the console are enough.

## Part 6 · Save, share, hand in

1. **Save** (or **Ctrl+S**). The first time, Wokwi asks you to sign in. Easiest: **sign in with GitHub**, you already have that account.
2. After saving, the project has its own address, e.g. `https://wokwi.com/projects/123456789`. This address is your **link for sharing**.
3. For the team repository:
   - put the **Wokwi link** into `README.md`,
   - still **upload** the files (`main.py`, `hardware.py`, …), because the repository is the source, not Wokwi,
   - take a **screenshot** of the circuit for the journal.

{{% notice style="info" title="Who can see my project?" %}}
Anyone who knows the link can see a saved Wokwi project. Do not put personal data in the code or project name. A good project name: `p1-gadget-<teamname>`.
{{% /notice %}}

If two of you work on the same project: Wokwi cannot be edited simultaneously. One person saves, the other opens the link and clicks **Save a copy**. Code is merged in the team repository.

## micro:bit: python.microbit.org

The [micro:bit Python Editor](https://python.microbit.org/) has the simulator built in.

1. Open [python.microbit.org](https://python.microbit.org/). Write code on the left.
2. On the right, press the **▶ button** above the virtual micro:bit.
3. Click buttons **A** and **B** and the logo in the picture.
4. Below the simulator you set the **sensors**: light level, temperature, sound level, acceleration and gestures (*shake*, *tilt*, …).
5. `print` output appears below the simulator (*Serial*).

Code for the simulator is **the same** as for the real micro:bit. **Send to micro:bit** (Chrome/Edge) puts it directly onto the board.

**Saving:** the editor remembers your project in the browser, but only on this device. **Save** downloads a `.hex` file (for sharing or flashing). The menu next to **Save** also has *Save Python script* for the `.py` file. That one belongs in the team repository.

**Several files:** use **Open…** to open another `.py` file such as `hardware.py` and **add it to the project as a new file**. It then appears in the *Project* area.

## Limits of the simulator

A simulator is a **model** of reality. Some things it does not reproduce:

| In the simulator | On the real board |
|------------------|-------------------|
| sensors deliver exact, steady values | values fluctuate, check thresholds again on the board |
| a reversed LED simply does not light | same, but a short circuit can **destroy** components |
| power is unlimited | servos and motors can make the board restart |
| timing roughly realistic | reaction games and tone lengths may feel slightly different |
| Wi-Fi via the network `Wokwi-GUEST` (no password, ESP32 and Pico W only) | real school Wi-Fi, see P2 |

So the rule is: **develop in the simulator, final check on the board.** Arduino teams demo their gadget in Wokwi at the review.

## Other simulators

- [**Wokwi** with Arduino UNO](https://wokwi.com/projects/new/arduino-uno): here you program in **C++** instead of Python. Not part of P1, just for the curious.
- [**MakeCode**](https://makecode.microbit.org/): micro:bit with blocks. You may know it from lower secondary. In this course we write Python.
