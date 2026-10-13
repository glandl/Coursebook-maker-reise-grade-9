+++
title = "MicroPython Boards (micro:bit, Pico, ESP32, Arduino)"
weight = 2
+++

**MicroPython** is Python for small computers without screen or keyboard, so-called **microcontrollers**. You write the same Python code as on the PC (`if`, `while`, functions, lists), plus modules such as `machine` or `microbit` that control pins, LEDs and sensors. You program in [Thonny]({{% relref "werkzeuge/python-thonny" %}}), the board is connected to the PC via USB.

You need this page from **P1 week 3**. No board at hand? The same code runs in the [Wokwi simulator]({{% relref "werkzeuge/wokwi-simulator" %}}).

## Which board do I have?

| Board | How to recognise it | MicroPython? |
|-------|---------------------|--------------|
| **micro:bit** | Pocket-sized, 5×5 LED display, buttons A and B. **V2** has a golden touch logo and a speaker on the back. | yes |
| **Raspberry Pi Pico** | Green strip, printed "Raspberry Pi Pico" (**Pico W** / **Pico 2 W** with a silver Wi-Fi chip cover), button **BOOTSEL**. | yes |
| **ESP32** | Usually a black board with a silver metal cover "ESP32-WROOM", two buttons **EN** and **BOOT**. Many manufacturers, pins labelled differently. | yes |
| **Arduino Nano ESP32** | Small Arduino board, printed "Nano ESP32". | yes |
| **Arduino UNO R3 / UNO R4** | Large Arduino board with header sockets. | **no**, see tab "Arduino" |

The strengths of each board are listed in [week 2]({{% relref "projekte/p1-code-gadget/woche-02-anforderungen" %}}).

## What you need

- A **USB data cable**. Many cables from phone chargers can only charge, not transfer data. If the board is not detected, this is the most common cause. Mark working cables with tape.
- For Pico, ESP32 and Nano ESP32: a **breadboard**, **jumper wires**, LEDs, **resistors** 220 Ω and 10 kΩ, a **push button**.
- For micro:bit: nothing, everything you need is built in. For your own components: **crocodile clips** or an **edge connector breakout**.

## Part 1 · Install MicroPython and connect Thonny

You do this **once per board**. Afterwards: plug in the board, start Thonny.

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
**With Thonny:**

1. Connect the micro:bit via USB. A drive **MICROBIT** appears on the PC.
2. Thonny: **Tools → Options → Interpreter** → **MicroPython (BBC micro:bit)**.
3. Click **Install or update MicroPython** at the bottom right, choose the MICROBIT drive, **Install**. The yellow LED on the back flashes, then the board restarts.
4. **OK**. The shell shows `>>>`. Test:

```python
from microbit import *
display.scroll("Hello")
```

**Without installing anything (browser):** open [python.microbit.org](https://python.microbit.org/), write code, transfer it with **Send to micro:bit** (Chrome or Edge, connects directly via USB). In other browsers click **Save** and drag the `.hex` file onto the MICROBIT drive. The editor has a built-in simulator, see [Wokwi & Browser Simulators]({{% relref "werkzeuge/wokwi-simulator" %}}).

{{% notice style="info" title="Thonny or browser editor?" %}}
Both work with the same code. You need **Thonny** for the **plotter** (week 4) and to put several files such as `hardware.py` onto the board. The **browser editor** is ideal at home and for trying things in the simulator.
{{% /notice %}}
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
1. Hold the **BOOTSEL** button, **then** plug in the USB cable, then release. A drive **RPI-RP2** (Pico 2: **RP2350**) appears on the PC.
2. Thonny: **Tools → Options → Interpreter** → **MicroPython (Raspberry Pi Pico)**.
3. Click **Install or update MicroPython** at the bottom right.
4. **Target volume:** the RPI-RP2 drive. **Variant:** pick exactly your model: *Pico / Pico H*, *Pico W / Pico WH*, *Pico 2* or *Pico 2 W*. The wrong variant runs without Wi-Fi or not at all.
5. **Install**. After copying, the drive disappears and the board restarts.
6. Close the window, **OK**. The shell shows `>>>`. Test:

```python
from machine import Pin
Pin("LED", Pin.OUT).value(1)    # onboard LED lights up
```

No drivers are needed on Windows 10/11, macOS and Linux.
{{% /tab %}}
{{% tab title="ESP32" %}}
1. Connect the ESP32 via USB.
2. **Check the driver (Windows only, first time only):** In Device Manager under *Ports (COM & LPT)* a new **COM port** must appear. If it is missing, look at the small chip next to the USB socket and install the driver:
   - printed **CP210x** (Silicon Labs) → [CP210x driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers)
   - printed **CH340** / **CH9102** (WCH) → [CH340 driver](https://www.wch-ic.com/downloads/CH341SER_EXE.html)
3. Thonny: **Tools → Options → Interpreter** → **MicroPython (ESP32)**, under *Port* choose the new port (`COM3`, `/dev/ttyUSB0`, `/dev/cu.usbserial-…`).
4. Click **Install or update MicroPython (esptool)** at the bottom right.
5. **Target port:** your port. **MicroPython family:** *ESP32*. **Variant:** *Espressif • ESP32 / WROOM*. If you have an ESP32-**S3** or **C3**, choose the matching family.
6. **Install**. If it hangs at `Connecting...`: hold the **BOOT** button until percentages appear.
7. Close the window, **OK**. The shell shows `>>>`. Test:

```python
from machine import Pin
Pin(2, Pin.OUT).value(1)        # onboard LED (on most DevKits)
```

{{% notice style="warning" title="Linux: permission denied" %}}
If Thonny reports `Permission denied: '/dev/ttyUSB0'`, run `sudo usermod -a -G dialout $USER` once and log out and back in. If the port disappears right away on Ubuntu, the package `brltty` interferes: `sudo apt remove brltty`.
{{% /notice %}}
{{% /tab %}}
{{% tab title="Arduino" %}}
**Arduino UNO R3 and UNO R4:** There is **no official MicroPython** for these boards. The course is in Python, so there are two ways:

1. **Simulator:** create an **ESP32** project in [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) and use the course's ESP32 code. This is equivalent: you build the same circuit virtually.
2. **Swap the board:** get an ESP32, Pico or **Arduino Nano ESP32** from your teacher.

**Arduino Nano ESP32:**

1. Download and start the [Arduino MicroPython Installer](https://labs.arduino.cc/en/labs/micropython-installer).
2. Connect the Nano ESP32. If the installer does not detect the board: press the **reset** button twice quickly.
3. Select the board, **Install MicroPython**.
4. Thonny: **Tools → Options → Interpreter** → **MicroPython (ESP32)**, choose the port, **OK**. Test:

```python
from machine import Pin
Pin(48, Pin.OUT).value(1)       # onboard LED (D13)
```

Code as in the ESP32 tab, but with **different pin numbers**, see part 3.
{{% /tab %}}
{{< /tabs >}}

## Part 2 · Working with the board in Thonny

As soon as Thonny is connected to the board:

- The **shell** talks to the **board**. `print(1 + 1)` is computed by the microcontroller.
- **▶ Play (F5)** sends the file in the editor to the board and runs it there. It is **not** saved: after unplugging it is gone.
- **■ Stop** (or **Ctrl+C** in the shell) aborts the program. A second click on Stop restarts the board (soft reset).

### Files on the board

**View → Files** shows the files on your PC at the top and the files on the **MicroPython device** at the bottom.

| What | How |
|------|-----|
| Save a file to the board | **File → Save as → MicroPython device**, type the name |
| Upload a file from the PC | In the upper (PC) part of the files pane right-click the file → **Upload to /** |
| Get a file from the board | Right-click the file on the device → **Download to …** |
| Delete a file | Right-click → **Delete** |

Two file names have a special meaning:

| File | Meaning |
|------|---------|
| **`main.py`** | Starts automatically as soon as the board gets power, also from a power bank. This is your gadget program. |
| `boot.py` | Starts even before `main.py`. Do not change it in this course. |

Your own modules such as **`hardware.py`** (from week 4) must be **on the board** so that `import hardware` works.

{{% notice style="tip" title="Code belongs in the repository, not only on the board" %}}
The board is not a storage place. Save every file on the PC too and upload it to the team repository. A board can get lost, swapped or re-flashed.
{{% /notice %}}

## Part 3 · Pinout and course wiring

All programs in the course use the same wiring per board. Stick to it and the examples run without changes.

{{% notice style="warning" title="Power off while wiring" %}}
- Only plug in or move components when the USB cable is **unplugged**.
- All boards work with **3.3 V**. Never connect **5 V** to an input pin.
- Always use a **series resistor** (220 Ω) with LEDs. The **long leg** of the LED goes towards the pin, the short one to GND.
- Never connect **3V3** and **GND** directly (short circuit).
{{% /notice %}}

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
For P1 there is **nothing to wire**: buttons A/B, 5×5 display, light sensor (the display itself), accelerometer, temperature, microphone and speaker (V2) are built in.

| Course function | micro:bit |
|-----------------|-----------|
| Button | `button_a`, `button_b` |
| LED | pixel on `display` |
| Buzzer | built-in speaker, `music.pitch(...)` |
| Light sensor | `display.read_light_level()` (0–255) |
| Tilt | `accelerometer.get_x()` |

**Your own components** connect with crocodile clips to the large rings **0**, **1**, **2**, **3V** and **GND**:

```python
from microbit import *

pin0.write_digital(1)        # external LED on pin 0 (with 220 Ω) on
value = pin1.read_analog()   # analog value on pin 1, 0–1023
print(value)
```

The small pins along the edge are only reachable with a breakout board. Many of them belong to the LED display. Stick to 0, 1 and 2.
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
**Careful:** the number in the code is the **GP number**, not the number of the physical pin. `Pin(15)` is **GP15**, which is physical pin 20.

| Course function | GP pin | Physical pin | Connection |
|-----------------|--------|--------------|------------|
| Button | **GP14** | 19 | button between GP14 and GND (pin 18) |
| LED | **GP15** | 20 | GP15 → 220 Ω → LED long leg, short leg → GND |
| Onboard LED | `"LED"` | – | built in, no wiring |
| Buzzer (passive) | **GP16** | 21 | GP16 → buzzer → GND (pin 23) |
| Light sensor / pot | **GP26** (ADC0) | 31 | 3V3 → LDR → GP26 → 10 kΩ → GND |
| 3.3 V | 3V3(OUT) | 36 | plus for sensors |
| GND | GND | 3, 8, 13, 18, 23, 28, 33, 38 | all GNDs are the same |

**Analog inputs** exist only on **GP26**, **GP27** and **GP28**. Official pinout to print: [Pico](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf), [Pico W](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf).

The breadboard: the Pico sits across the centre groove, each row of five next to a pin is connected to it. The long rails along the edge (red/blue) are handy for 3V3 and GND.
{{% /tab %}}
{{% tab title="ESP32" %}}
Applies to the common **ESP32 DevKit** (30 or 38 pins). The number in the code is the **GPIO number**, usually printed on the board as `D18`, `G18`, `IO18` or just `18`.

| Course function | GPIO | Connection |
|-----------------|------|------------|
| Button | **4** | button between GPIO 4 and GND |
| LED | **18** | GPIO 18 → 220 Ω → LED long leg, short leg → GND |
| Onboard LED | **2** | built in on most DevKits (not all) |
| Buzzer (passive) | **19** | GPIO 19 → buzzer → GND |
| Light sensor / pot | **34** | 3V3 → LDR → GPIO 34 → 10 kΩ → GND |

**Pins with a catch:**

| Pins | Note |
|------|------|
| 6–11 | **Never use**, they belong to the internal flash memory. |
| 0, 2, 12, 15 | Affect booting. Only use if needed (GPIO 2 for the onboard LED is fine). |
| 34, 35, 36 (VP), 39 (VN) | **Input only**, no `Pin.PULL_UP`. Good for sensors, bad for buttons. |
| 32–39 | Analog inputs that also work with **Wi-Fi** on (important for P2). Other ADC pins (e.g. 25, 26, 27) do not work while Wi-Fi is active. |

Always configure analog inputs with `adc.atten(ADC.ATTN_11DB)`, otherwise the range ends at about 1 V.
{{% /tab %}}
{{% tab title="Arduino" %}}
**Arduino Nano ESP32:** the board shows Arduino names (`D2`, `A0`), but MicroPython uses the **GPIO numbers** of the ESP32-S3. Translation:

| Arduino | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 |
|---------|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|
| **GPIO** | 44 | 43 | 5 | 6 | 7 | 8 | 9 | 10 | 17 | 18 | 21 | 38 | 47 | 48 |

| Arduino | A0 | A1 | A2 | A3 | A4 | A5 | A6 | A7 |
|---------|----|----|----|----|----|----|----|----|
| **GPIO** | 1 | 2 | 3 | 4 | 11 | 12 | 13 | 14 |

**Course wiring** (chosen so that the ESP32 code changes as little as possible):

| Course function | Connection on the Nano | In code | Difference to ESP32 code |
|-----------------|------------------------|---------|--------------------------|
| Button | **A3** ↔ GND | `Pin(4, …)` | none |
| LED | **D9** → 220 Ω → LED → GND | `Pin(18, …)` | none |
| Onboard LED | D13 | `Pin(48, …)` | instead of 2 |
| Buzzer | **D8** → buzzer → GND | `PWM(Pin(17))` | instead of 19 |
| Light sensor / pot | 3V3 → LDR → **A0** → 10 kΩ → GND | `ADC(Pin(1))` | instead of 34 |

So in `hardware.py` (week 4) you only change the numbers 19 → 17 and 34 → 1. The board works with **3.3 V**, not 5 V like the UNO.

**UNO R3 / UNO R4:** no MicroPython, see part 1.
{{% /tab %}}
{{< /tabs >}}

### Placing the button correctly

A four-legged push button always connects two pairs. It works reliably if you use **two diagonally opposite** legs. The button sits across the centre groove of the breadboard.

## Part 4 · More components

Your gadget may need more than LED, button and light sensor. Each component becomes **one small function** in `hardware.py`, the rest of the code stays the same (see [week 4]({{% relref "projekte/p1-code-gadget/woche-04-sensoren-review" %}})).

Suggested pins that do not clash with the course wiring:

| Component | Pico | ESP32 | Nano ESP32 | Power |
|-----------|------|-------|------------|-------|
| Motion sensor (PIR, HC-SR501) | GP17 | 27 | D4 → 7 | 5 V |
| Ultrasonic distance: Trig | GP18 | 25 | D5 → 8 | 5 V (HC-SR04) / 3.3 V (HC-SR04**P**) |
| Ultrasonic distance: Echo | GP19 | 26 | D6 → 9 | see warning |
| Servo (SG90) | GP20 | 13 | D7 → 10 | 5 V |
| Temperature/humidity (DHT11/DHT22) | GP21 | 33 | D10 → 21 | 3.3 V |
| OLED display (I²C): SDA / SCL | GP4 / GP5 | 21 / 22 | A4 → 11 / A5 → 12 | 3.3 V |
| second analog value | GP27 | 35 | A1 → 2 | 3.3 V |

**5 V** is available on pin **VBUS** (Pico, pin 40), **5V/VIN** (ESP32) or **VBUS** (Nano ESP32) while the board is powered via USB.

The examples below use the **Pico** pins. For other boards insert the number from the table. On the micro:bit most of these components are awkward (few pins, no 5 V). Use the built-in sensors there instead.

{{% expand title="Motion sensor (PIR)" %}}
The PIR returns 1 as long as it detects motion. The two knobs set sensitivity and hold time. After power-on it needs about a minute to calibrate.

```python
from machine import Pin

_pir = Pin(17, Pin.IN)


def motion():
    """True as long as motion is detected."""
    return _pir.value() == 1
```
{{% /expand %}}

{{% expand title="Ultrasonic distance sensor (HC-SR04)" %}}
{{% notice style="warning" title="5 V signal" %}}
The classic **HC-SR04** needs 5 V and sends a 5 V signal on **Echo**. This can damage the 3.3 V pin. Either add a **voltage divider** (Echo → 1 kΩ → pin → 2 kΩ → GND) or use the **HC-SR04P** or **RCWL-1601** variant, which runs on 3.3 V.
{{% /notice %}}

```python
from machine import Pin, time_pulse_us
import time

_trig = Pin(18, Pin.OUT)
_echo = Pin(19, Pin.IN)


def distance_cm():
    """Distance in cm, or -1 if nothing was measured."""
    _trig.value(0)
    time.sleep_us(2)
    _trig.value(1)
    time.sleep_us(10)
    _trig.value(0)
    duration = time_pulse_us(_echo, 1, 30000)   # wait at most 30 ms
    if duration < 0:
        return -1
    return duration * 0.0343 / 2                 # sound: 343 m/s, there and back
```
{{% /expand %}}

{{% expand title="Servo (SG90)" %}}
Brown = GND, red = **5 V**, orange = signal. A servo draws a lot of current: if the board restarts as soon as the servo moves, USB power is not enough. Then power the servo from a separate source (connect the GNDs).

```python
from machine import Pin, PWM

_servo = PWM(Pin(20))
_servo.freq(50)


def servo(angle):
    """Turns the servo to 0–180 degrees."""
    # 0.5 ms (0°) to 2.5 ms (180°) out of 20 ms
    _servo.duty_u16(1638 + angle * (8192 - 1638) // 180)
```
{{% /expand %}}

{{% expand title="Temperature and humidity (DHT11 / DHT22)" %}}
The `dht` module is already included on Pico and ESP32. The sensor may be read at most **once per second** (DHT22: every 2 s).

```python
from machine import Pin
import dht

_dht = dht.DHT11(Pin(21))      # for DHT22: dht.DHT22(...)


def temperature():
    _dht.measure()
    return _dht.temperature()   # °C


def humidity():
    _dht.measure()
    return _dht.humidity()      # %
```
{{% /expand %}}

{{% expand title="OLED display (SSD1306, 128×64, I²C)" %}}
Install the driver on the board once: Thonny **Tools → Manage packages**, search for `ssd1306`, **Install**.

```python
from machine import Pin, I2C
import ssd1306

_i2c = I2C(0, sda=Pin(4), scl=Pin(5))     # ESP32: I2C(0, sda=Pin(21), scl=Pin(22))
_oled = ssd1306.SSD1306_I2C(128, 64, _i2c)


def show_text(line1, line2=""):
    _oled.fill(0)
    _oled.text(line1, 0, 0)
    _oled.text(line2, 0, 16)
    _oled.show()
```

If `I2C(...)` reports an error or the display stays dark: `print(_i2c.scan())` must print `[60]`. An empty list means SDA/SCL are swapped or not connected.
{{% /expand %}}

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Thonny finds no device, no port in the list | charge-only cable, missing driver (ESP32) | other cable, other USB port, driver from part 1 |
| `Device is busy or does not respond` | `main.py` runs an endless loop | press **Stop** several times. If that does not help: unplug, plug in, press Stop immediately |
| `ImportError: no module named 'hardware'` | `hardware.py` is only on the PC | save the file **to the board** (part 2) |
| `ValueError: invalid pin` | physical pin number instead of GP/GPIO number | check the pinout (part 3) |
| LED stays dark | LED reversed, wrong pin, GND missing | long leg to the pin, compare wiring with the table |
| Button always returns 0 or always 1 | `Pin.PULL_UP` missing, button rotated, pin 34–39 on ESP32 | set pull-up, diagonal legs, different pin |
| Analog value always 0 or always maximum | wrong pin, not an ADC pin, `atten` missing (ESP32) | Pico: GP26–28. ESP32: 32–39 with `ATTN_11DB` |
| Board restarts when buzzer/servo/motor starts | USB supplies too little current | separate power supply for the load |
| Program does not run without PC | file is not called `main.py` or only on the PC | save as `main.py` to the board |
| micro:bit: drive is called **MAINTENANCE** | reset was pressed while plugging in | unplug, plug in again without pressing a button |

{{% notice style="tip" title="If nothing works any more" %}}
Simply **re-install** MicroPython (part 1). This deletes all files on the board. That is why code belongs in the repository.
{{% /notice %}}

## Further reading

- [MicroPython documentation](https://docs.micropython.org/en/latest/): *quick reference* for [RP2/Pico](https://docs.micropython.org/en/latest/rp2/quickref.html) and [ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)
- [micro:bit MicroPython documentation](https://microbit-micropython.readthedocs.io/)
- [Arduino Nano ESP32 and MicroPython](https://docs.arduino.cc/micropython/)
