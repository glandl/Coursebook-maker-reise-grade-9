+++
title = "Week 3 · Functions, Lists, First Board"
weight = 3
+++

**Today:** you package code into **functions**, store many values in **lists**, and bring your board to life: an LED blinks, a button switches it.

{{% notice style="info" title="What you will have at the end of the lesson" %}}
- You can write and call a function with parameters and a return value.
- You can create a list, extend it, loop over it and access elements by index.
- Your board is connected to Thonny, an LED blinks and a button toggles it.
- The board code is in the team repository, the Kanban board is up to date.
{{% /notice %}}

## 1. Stand-up (5 min)

In front of the Kanban board, each person one minute at most: **What did I do? What am I doing today? Where am I stuck?** Move cards, write names on them.

## 2. Functions (15 min)

A **function** is a named block of code. You write it once with `def` and call it as often as you like. You pass values in as **parameters**, and with `return` the function hands back a result.

### `switch_functions.py`

This is `switch.py` from week 1, tidied up: the logic ("what comes after OFF?") and the output are now separate functions.

```python
def toggle(state):
    """Returns the new state after a button press."""
    if state == "OFF":
        return "ON"
    return "OFF"


def show(state, presses):
    symbol = "💡" if state == "ON" else "⚫"
    print(symbol, "Lamp is", state, "| button presses:", presses)


state = "OFF"
presses = 0
show(state, presses)

while True:
    button = input("Press [Enter], 'q' to quit: ")
    if button == "q":
        break
    state = toggle(state)
    presses = presses + 1
    show(state, presses)
```

**Why the effort?** In a few minutes you replace `input` with a real button and `print` with a real LED. The function `toggle` stays **unchanged**. Separate logic can also be tested without hardware (we do that in week 6).

**Change it:** add a third state `BLINK`: OFF → ON → BLINK → OFF. You only need to change `toggle` (and the symbol in `show`).

## 3. Lists (15 min)

A **list** stores several values in one variable, in a fixed order.

```python
states = ["RED", "RED-YELLOW", "GREEN", "YELLOW"]

print(states[0])        # RED     – index starts at 0
print(states[-1])       # YELLOW  – from the end
print(len(states))      # 4

for s in states:
    print("Traffic light:", s)
```

### `traffic_list.py` — states in a circle

```python
import time

STATES = ["RED", "RED-YELLOW", "GREEN", "YELLOW"]
DURATION = [3, 1, 3, 1]          # seconds per state

i = 0
for step in range(8):
    print("Traffic light:", STATES[i])
    time.sleep(DURATION[i])
    i = (i + 1) % len(STATES)     # after the last one, back to the first
```

`%` is the **remainder** of a division: `4 % 4` is 0, so the index jumps from the last element back to 0. Names in CAPITALS mean: this value does not change in the program (constant).

### `readings.py` — collect and evaluate values

Sensors deliver values continuously. You collect them in a list:

```python
readings = []                      # empty list

while True:
    entry = input("Reading (empty = done): ")
    if entry == "":
        break
    readings.append(float(entry))

if len(readings) > 0:
    print("Count:", len(readings))
    print("Smallest:", min(readings), "Largest:", max(readings))
    print("Average:", round(sum(readings) / len(readings), 2))
```

**Change it:** write a function `average(values)` that returns the average, and use it.

{{% expand title="Solution" %}}
```python
def average(values):
    return sum(values) / len(values)
```
{{% /expand %}}

German videos on functions and lists:

{{< youtube B1mMAieycPY >}}

{{< youtube R7lZTvC9UUU >}}

## Break (5 min)

## 4. Bring the board to life (45 min)

### 4a · Connect (10 min)

1. Plug the board in via USB.
2. Thonny: **Tools → Options → Interpreter**, choose the matching MicroPython (for micro:bit: "MicroPython (BBC micro:bit)"). If there is no MicroPython on the board yet, Thonny offers **Install or update MicroPython** at the bottom right.
3. Type `print("Hello board")` into the shell. The answer now comes **from the board**, not from the PC.

Details, drivers and troubleshooting for each board: [MicroPython Boards]({{% relref "werkzeuge/micropython-boards" %}}). **No board at hand?** [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) (Pico, ESP32) or [python.microbit.org](https://python.microbit.org/) (micro:bit with simulator) work with the same code.

{{% notice style="warning" title="Power off while rewiring" %}}
Only connect or move components while the USB cable is **unplugged**. Always use LEDs with a **series resistor** (220 Ω). An LED has a direction: the **long leg** (+) goes towards the pin, the short one to GND.
{{% /notice %}}

### 4b · Blink (10 min)

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
No wiring needed. The LED in the middle of the 5×5 display has the coordinates (2, 2).

```python
from microbit import *

for i in range(10):
    display.set_pixel(2, 2, 9)   # brightness 0–9
    sleep(500)                   # milliseconds
    display.set_pixel(2, 2, 0)
    sleep(500)
```
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
First the **onboard LED**, no wiring needed:

```python
from machine import Pin
import time

led = Pin("LED", Pin.OUT)

for i in range(10):
    led.value(not led.value())   # toggle
    time.sleep(0.5)
```

Then an **external LED**: GP15 → 220 Ω → long LED leg, short leg → GND. In the code replace `Pin("LED", …)` with `Pin(15, Pin.OUT)`.
{{% /tab %}}
{{% tab title="ESP32" %}}
First the **onboard LED** (GPIO 2 on most DevKit boards):

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)

for i in range(10):
    led.value(not led.value())   # toggle
    time.sleep(0.5)
```

No onboard LED, or it stays dark? External LED: GPIO 18 → 220 Ω → long LED leg, short leg → GND, in the code `Pin(18, Pin.OUT)`.
{{% /tab %}}
{{% tab title="Arduino" %}}
**UNO R4 / Nano ESP32 with MicroPython:** code as in the ESP32 tab, adjust pin numbers according to your board's pinout on [MicroPython Boards]({{% relref "werkzeuge/micropython-boards" %}}).
**UNO R3:** create an ESP32 project in [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) and use the ESP32 code.
{{% /tab %}}
{{< /tabs >}}

**Change it:** make the LED blink three times short and three times long.

### 4c · Button toggles LED (15 min)

Now `toggle` from part 2 moves onto the board, **unchanged**.

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
```python
from microbit import *


def toggle(state):
    if state == "OFF":
        return "ON"
    return "OFF"


def show(state):
    if state == "ON":
        display.show(Image.HEART)
    else:
        display.clear()


state = "OFF"
show(state)

while True:
    if button_a.was_pressed():   # True only once per press
        state = toggle(state)
        show(state)
    sleep(20)
```
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
**Wiring:** button between **GP14** and **GND**. External LED on GP15 as in 4b (or onboard LED `Pin("LED", Pin.OUT)`).

```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)   # not pressed = 1, pressed = 0
before = 1


def pressed():
    """True only at the moment the button goes down."""
    global before
    now = button.value()
    new = before == 1 and now == 0
    before = now
    return new


def toggle(state):
    if state == "OFF":
        return "ON"
    return "OFF"


def show(state):
    led.value(1 if state == "ON" else 0)


state = "OFF"
show(state)

while True:
    if pressed():
        state = toggle(state)
        show(state)
    time.sleep_ms(20)                   # also debounces
```
{{% /tab %}}
{{% tab title="ESP32" %}}
**Wiring:** button between **GPIO 4** and **GND**. LED: onboard on GPIO 2 or external on GPIO 18.

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_UP)    # not pressed = 1, pressed = 0
before = 1


def pressed():
    """True only at the moment the button goes down."""
    global before
    now = button.value()
    new = before == 1 and now == 0
    before = now
    return new


def toggle(state):
    if state == "OFF":
        return "ON"
    return "OFF"


def show(state):
    led.value(1 if state == "ON" else 0)


state = "OFF"
show(state)

while True:
    if pressed():
        state = toggle(state)
        show(state)
    time.sleep_ms(20)                   # also debounces
```
{{% /tab %}}
{{% tab title="Arduino" %}}
Code as in the ESP32 tab, adjust the pins (see [MicroPython Boards]({{% relref "werkzeuge/micropython-boards" %}})). UNO R3: [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) with ESP32.
{{% /tab %}}
{{< /tabs >}}

{{% expand title="Why `pressed()` and not simply `button.value() == 0`?" %}}
The loop runs 50 times per second. A button press lasts about 0.2 s, so `button.value() == 0` would be true ten times in a row and toggle the LED ten times. `pressed()` remembers the last value in `before` and only reports the **change** from "up" (1) to "down" (0). This is called **edge detection**. `global before` allows the function to change the variable outside of it. On the micro:bit, `was_pressed()` does this for you.
{{% /expand %}}

**Change it:** bring over your third state `BLINK` from part 2. Hint: in the BLINK state, toggle the LED in every loop pass if 300 ms have passed since the last toggle (`time.ticks_ms()`, on the micro:bit `running_time()`).

### 4d · Start without a PC (5 min)

A gadget should also run without a laptop. In Thonny save the program via **File → Save as → MicroPython device** as **`main.py`**. The next time you plug it in (even into a power bank) it starts automatically. On the micro:bit: **Flash**/**Send to micro:bit** in the editor.

Videos to rewatch, in German (Pico: external LED and reading a button, ESP32: first steps with Thonny):

{{< youtube DaZF-3jM69U >}}

{{< youtube HTlIg6IqNzA >}}

{{< youtube 59S53NSHR0M >}}

## 5. Into the team repository (5 min)

Upload your board code to the team repository (**Add file → Upload files**), for example as `code/main.py`. Update the Kanban board: what is **done**?

## 6. Journal task 3 (10 min)

{{% notice style="primary" title="Journal task 3 · First sign of life" icon="book" %}}
```markdown
# P1 · Week 3 · <date>

## Setup
Photo of your board with LED and button (or a screenshot from the simulator).
Which pins did you use?

## A function explained
Copy a function from your code here (as a ```python block)
and explain in 2–3 sentences: which parameters does it take,
what does it return, why is it a function of its own?

## Problem and solution
What did not work straight away, and how did you solve it?
```
{{% /notice %}}

Commit message: `P1 week 3: board is running`.

## Quiz

{{< quiz title="Quiz · Week 3" >}}
{{< question correct="2" >}}
What does this program print?

```python
def double(x):
    return 2 * x

print(double(3) + 1)
```
---
`8`
`7`
`2 * 3 + 1`
Nothing, because `double` does not print anything.
---
`double(3)` returns 6, plus 1 gives 7. `return` hands back a value; it is only printed by `print`.
{{< /question >}}
{{< question correct="3" >}}
`colours = ["red", "green", "blue"]`. What is `colours[1]`?
---
`"red"`
`"blue"`
`"green"`
an error
---
The index starts at 0: `colours[0]` is `"red"`, `colours[1]` is `"green"`.
{{< /question >}}
{{< question correct="1" >}}
`i = 3` and the list has 4 elements. What is `(i + 1) % 4`?
---
0
4
1
3
---
4 divided by 4 is 1 remainder **0**. That is how the index jumps from the last element back to the first.
{{< /question >}}
{{< question correct="4" >}}
A button is connected between a pin and GND, and the pin is configured with `Pin.PULL_UP`. What does `button.value()` return while the button is pressed?
---
1
`True`
It depends on the button.
0
---
The pull-up resistor pulls the pin to 1 as long as nothing happens. The pressed button connects the pin to GND, so 0.
{{< /question >}}
{{< question correct="2" >}}
Why do we keep `toggle(state)` separate from `show(state)`?
---
Because Python requires it.
So that the logic stays the same on PC and board and can be tested without hardware.
So that the program runs faster.
Because a function may have at most three lines.
---
Only `show` depends on the hardware. The logic can be reused and checked unchanged.
{{< /question >}}
{{< /quiz >}}

## Until next week

- Commit journal task 3.
- As a team: which **sensor** and which **actuator** (buzzer, servo, display, …) belong to your gadget? Reserve the part with your teacher.
- Next week is **sprint review 1**: your board should be able to demonstrate at least one must story by then.
