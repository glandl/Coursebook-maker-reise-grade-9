+++
title = "Week 1 · Kickoff"
weight = 1
+++

**Today:** you get to know the Maker Journey, write your first Python programs, create your learning journal on GitHub and write the first entry in Markdown.

{{% notice style="info" title="What you will have at the end of the lesson" %}}
- Thonny runs on your computer and you have run and modified two programs.
- You know what a **state** is and have simulated a gadget with states.
- You have a GitHub account and a learning journal repository with your first **commit**.
- Your first journal entry is written, in Markdown, with at least two gadget ideas.
{{% /notice %}}

## 1. The Maker Journey (10 min)

One school year, five projects, one learning journal. Have a look at the [start page]({{% relref "/" %}}): every project follows the same rhythm **kickoff → sprints → review → retro**. In P1 you build your first interactive device. What it should look like at the end is in the [project brief]({{% relref "projekte/p1-code-gadget" %}}). The boards it will run on are passed around the class today.

## 2. Tool check: Thonny (15 min)

Open Thonny. If it is missing on your device, follow the [setup guide]({{% relref "werkzeuge/python-thonny" %}}). In an emergency the browser works too: [python.microbit.org](https://python.microbit.org/) has a Python console and a simulator.

Type into the **Shell** at the bottom (the window with `>>>`) and press Enter:

```python
print("Hello Maker Journey!")
```

If the text appears, you are ready.

## 3. Two programs (30 min)

Create a new file for each program (**File → New**), save it under the given name and run it with the green play button (or **F5**).

### Program 1 · `hello.py` — input and output

```python
name = input("What is your name? ")
print("Hello", name, "– welcome to the Maker Journey!")
```

**Change it:** also ask for a favourite device and print both in one sentence.

### Program 2 · `switch.py` — a gadget with two states

Almost every device has **states**: a lamp is OFF or ON. A button press changes the state. That is exactly what we simulate in text here, before we build it with a real LED and button in a few weeks.

```python
# A gadget with two states: OFF and ON
state = "OFF"

while True:
    print("Lamp is", state)
    button = input("Press the button [Enter], 'q' to quit: ")
    if button == "q":
        break
    if state == "OFF":
        state = "ON"
    else:
        state = "OFF"

print("Gadget switched off.")
```

**Change it:**

1. Count how often the button was pressed and print the number at the end.
2. The lamp should switch itself off after the fifth press ("energy saving mode").

{{% expand title="Hint for 1." %}}
Create `presses = 0` before the loop and increase the variable inside the loop with `presses = presses + 1`.
{{% /expand %}}

**Take a screenshot** of the running program. You will need it for the journal in a moment.

### If you are fast (or at home) · `trafficlight.py` — three states in a circle

```python
state = "RED"
switches = 0

while switches < 6:
    print("Traffic light:", state)
    input("Continue with [Enter]")
    if state == "RED":
        state = "GREEN"
    elif state == "GREEN":
        state = "YELLOW"
    else:
        state = "RED"
    switches = switches + 1

print("Done after", switches, "switches.")
```

**Change it:** a real traffic light goes RED → RED-YELLOW → GREEN → YELLOW → RED. Add the fourth state. Then draw the states as circles and the transitions as arrows on paper. That is your first **state diagram**.

{{% notice style="tip" title="Preview: the same program on the board" %}}
From week 3 your switch runs on real hardware. The core stays the same, only `input` and `print` are replaced by button and LED. You do not have to understand this today, just see that it is the same idea.
{{% /notice %}}

{{< tabs groupid="board" >}}
{{% tab title="micro:bit" %}}
```python
from microbit import *

state = "OFF"
while True:
    if button_a.was_pressed():
        if state == "OFF":
            state = "ON"
            display.show(Image.HAPPY)
        else:
            state = "OFF"
            display.clear()
```
{{% /tab %}}
{{% tab title="Raspberry Pi Pico" %}}
```python
from machine import Pin
import time

led = Pin("LED", Pin.OUT)               # onboard LED
button = Pin(14, Pin.IN, Pin.PULL_UP)   # button between GP14 and GND

state = "OFF"
while True:
    if button.value() == 0:             # pressed
        state = "ON" if state == "OFF" else "OFF"
        led.value(1 if state == "ON" else 0)
        time.sleep(0.3)                 # debounce
```
{{% /tab %}}
{{% tab title="ESP32" %}}
```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)                   # onboard LED (usually GPIO 2)
button = Pin(4, Pin.IN, Pin.PULL_UP)    # button between GPIO 4 and GND

state = "OFF"
while True:
    if button.value() == 0:
        state = "ON" if state == "OFF" else "OFF"
        led.value(1 if state == "ON" else 0)
        time.sleep(0.3)
```
{{% /tab %}}
{{% tab title="Arduino" %}}
An **Arduino UNO R4** or **Nano ESP32** runs MicroPython, so the ESP32 code applies (adjust the LED pin). The classic **UNO R3** cannot run MicroPython: use the [Wokwi simulator]({{% relref "werkzeuge/wokwi-simulator" %}}) with a virtual ESP32 or the C++ appendix.
{{% /tab %}}
{{< /tabs >}}

## 4. Your learning journal on GitHub (25 min)

Your journal is a collection of **Markdown files in a GitHub repository**. You save every change as a **commit**. That way you and your teacher can see it grow week by week.

### 4a · Account and repository (15 min)

Follow part 1 and part 2 of the guide [Git & GitHub]({{% relref "werkzeuge/git-github" %}}). At the end you have a repository `lernjournal` with a `README.md`.

### 4b · Markdown in five minutes (5 min)

Open the [Markdown cheat sheet]({{% relref "werkzeuge/markdown" %}}). Today you only need: `#` for headings, `-` for lists, `**bold**`, and how to embed an image.

### 4c · First commit (5 min)

Edit the `README.md` in the browser (pencil icon) so that it looks like this, with your details:

```markdown
# Learning journal of <first name>

Class: <class> · School year 2026/27 · Maker Journey

## Entries
- [P1 week 1](p1/woche-01.md)
```

Check the **Preview** tab, then **Commit changes** with the message `README: name and class`. Your first commit.

## 5. Journal task 1 (15 min)

In the repository create the file `p1/woche-01.md` (**Add file → Create new file**, the slash creates the folder) and write your first entry:

{{% notice style="primary" title="Journal task 1 · Starting point" icon="book" %}}
```markdown
# P1 · Week 1 · <date>

## Expectations
What do you expect from the Maker Journey? What can you already do
(programming, electronics, tinkering)?

## Gadget ideas
At least two devices from your everyday life you would like to build.
For each idea: inputs (what is measured or pressed), outputs
(what lights up, beeps, moves), states.

## Worked / stuck on
What worked today, where did you get stuck?

## Evidence
Screenshot of switch.py: upload into the images/ folder and
embed it here: ![switch.py](../images/p1-w01-switch.png)
```
{{% /notice %}}

Commit message: `P1 week 1: first entry`. If the screenshot upload does not work out today, catch up on it by next week.

If you need inspiration for gadget ideas: this is what a micro:bit can do (German).

{{< youtube SF_Ym8fWTPU >}}

## Check yourself

{{% expand title="What is the difference between `print` and `input`?" %}}
`print` outputs text. `input` shows a text, waits for input and returns it as text that you can store in a variable.
{{% /expand %}}

{{% expand title="What happens in `switch.py` if you delete the line `if button == \"q\": break`?" %}}
The loop runs forever. You can only end the program with the stop button (or Ctrl+C in the shell).
{{% /expand %}}

{{% expand title="How many states does a bicycle light with the modes off, steady, flashing have?" %}}
Three. One button press goes around in a circle: off → steady → flashing → off. That is exactly the structure of `trafficlight.py`.
{{% /expand %}}

{{% expand title="What is a commit, and why does it need a message?" %}}
A commit is a saved state of your repository with time and author. The message says what changed, so that you (and your teacher) can read the history of the journal without opening every file.
{{% /expand %}}

## Until next week

- Finish journal task 1 and commit it (do not forget the screenshot).
- Try `trafficlight.py` if you did not get to it today.
- Install Thonny at home if you use your own device ([guide]({{% relref "werkzeuge/python-thonny" %}})).
- Video to rewatch if something went too fast today (German):

{{< youtube oxXAb8IikHM >}}
