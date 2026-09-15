+++
title = "Python & Thonny"
weight = 1
+++

**Thonny** is the Python development environment of this course. It ships with Python, has a built-in shell, a beginner-friendly debugger and can later talk directly to MicroPython boards. One tool for the whole year.

## Installation

{{< tabs groupid="os" >}}
{{% tab title="Windows" %}}
1. Download the installer from [thonny.org](https://thonny.org/) (button "Windows").
2. Run the installer, keep the default settings. Python is included, nothing else needs to be installed.
3. Start Thonny from the start menu.

On school PCs Thonny is already installed; if not, thonny.org also offers a **portable version** that runs from a folder or USB stick without install rights.
{{% /tab %}}
{{% tab title="macOS" %}}
1. On [thonny.org](https://thonny.org/) choose the Mac download (Apple Silicon or Intel, depending on your device).
2. Open the `.pkg` file and follow the instructions.
3. Start Thonny from the Applications folder. On first start you may need right-click → Open if macOS checks the origin.
{{% /tab %}}
{{% tab title="Linux" %}}
Easiest via the package manager:

```bash
sudo apt install thonny      # Debian / Ubuntu / Mint / Pop!_OS
```

Alternatively use the install script from [thonny.org](https://thonny.org/).
{{% /tab %}}
{{% tab title="Browser (fallback)" %}}
If nothing can be installed:

- [python.microbit.org](https://python.microbit.org/) — Python editor with micro:bit simulator, runs entirely in the browser.
- [Wokwi](https://wokwi.com/) — simulator for Pico, ESP32 and more, see [Wokwi & Browser Simulators]({{% relref "werkzeuge/wokwi-simulator" %}}).

For plain PC Python without a board, any online Python editor that supports `input()` works.
{{% /tab %}}
{{< /tabs >}}

## First start

1. On first start Thonny asks for a language: pick yours (changeable later under *Tools → Options → General*).
2. The top is the **editor** (where you write programs), the bottom is the **shell** (where you try single commands).
3. Type into the shell and press Enter:

```python
print("Hello Maker Journey!")
```

4. A program: **File → New**, type the code, **File → Save** as `test.py`, then the green **play button** (or **F5**).

## The most important buttons

| Button / key | Meaning |
|--------------|---------|
| ▶ Play (F5) | Run the current file |
| ■ Stop | Abort the running program (important with `while True`) |
| 🐞 Debug (Ctrl+F5) | Run the program step by step, watch variables |
| *View → Variables* | Shows all variables and their values while the program runs |
| *View → Assistant* | Explains error messages in plain language |

{{% notice style="tip" title="If a program stops responding" %}}
Press the stop button or click into the shell and press **Ctrl+C**. With an endless loop this is normal, not an error.
{{% /notice %}}

## Videos

Short introduction to the interface (German):

{{< youtube 93J6Sxk55mg >}}

First steps with Python in Thonny (German):

{{< youtube k7CLrRkzC5o >}}

## Later in the course

Thonny is the tool for **P1 and P2**. From **P3** the course switches to **Visual Studio Code**, which is the better home for notebooks, data analysis, SQL and later web development with Git. A separate setup guide follows at the start of P3.

From P1 week 3 you connect Thonny to your board: *Tools → Options → Interpreter* → select MicroPython. Guide under [MicroPython Boards]({{% relref "werkzeuge/micropython-boards" %}}).
