"""Zeichnet die Schaltungsbilder der Baupläne (schaltung.svg pro Team).

Aufruf:  python3 planning/bauplaene/schaltplan.py
Keine Abhängigkeiten. Die Pins müssen zu den Tabellen in K1/K2 des
jeweiligen BAUPLAN.md passen (Kurs-Verkabelung, Pico 2 W).
"""
from pathlib import Path

HIER = Path(__file__).parent

P = 32                      # Abstand der Beinchen in px
BOARD_W = 190
TOP = 120                   # y von Beinchen 1 / 40
LEFT_SPACE = 330            # Platz links vom Board
FONT = "font-family='Helvetica, Arial, sans-serif'"

GND_C = "#222"
V33_C = "#d62828"
V5_C = "#8a1c7c"
SIG_C = "#1f6fd1"
LED_COLORS = {"rot": "#e63946", "gelb": "#f4b400", "grün": "#2a9d4b", "warmweiß": "#f6e7b0", "blau": "#3a6ff7"}

LEFT_PINS = {1: "GP0", 2: "GP1", 3: "GND", 4: "GP2", 5: "GP3", 6: "GP4", 7: "GP5", 8: "GND",
             9: "GP6", 10: "GP7", 11: "GP8", 12: "GP9", 13: "GND", 14: "GP10", 15: "GP11",
             16: "GP12", 17: "GP13", 18: "GND", 19: "GP14", 20: "GP15"}
RIGHT_PINS = {21: "GP16", 22: "GP17", 23: "GND", 24: "GP18", 25: "GP19", 26: "GP20", 27: "GP21",
              28: "GND", 29: "GP22", 30: "RUN", 31: "GP26", 32: "GP27", 33: "GND", 34: "GP28",
              35: "VREF", 36: "3V3", 37: "3V3_EN", 38: "GND", 39: "VSYS", 40: "VBUS"}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Bild:
    def __init__(self):
        self.teile = []
        self.bx = LEFT_SPACE                    # linker Rand des Boards
        self.rx = LEFT_SPACE + BOARD_W          # rechter Rand des Boards
        self.max_x = self.rx + 60
        self.used = {}
        self.extra_unten = 0                    # Platz unter dem Board (Summer)

    # --- Grundformen -------------------------------------------------------
    def add(self, s):
        self.teile.append(s)

    def text(self, x, y, t, size=12, anchor="start", color="#222", bold=False, italic=False):
        w = " font-weight='bold'" if bold else ""
        i = " font-style='italic'" if italic else ""
        self.add(f"<text x='{x}' y='{y}' font-size='{size}' text-anchor='{anchor}' fill='{color}' {FONT}{w}{i}>{esc(t)}</text>")

    def line(self, pts, color, width=2.5):
        p = " ".join(f"{x},{y}" for x, y in pts)
        self.add(f"<polyline points='{p}' fill='none' stroke='{color}' stroke-width='{width}' stroke-linejoin='round' stroke-linecap='round'/>")
        self.max_x = max(self.max_x, max(x for x, _ in pts) + 20)

    def dot(self, x, y, color):
        self.add(f"<circle cx='{x}' cy='{y}' r='4' fill='{color}'/>")

    # --- Pico --------------------------------------------------------------
    @staticmethod
    def y_links(pin):
        return TOP + (pin - 1) * P

    @staticmethod
    def y_rechts(pin):
        return TOP + (40 - pin) * P

    def pin(self, nr):
        """Koordinate des Beinchens am Board-Rand."""
        if nr <= 20:
            return self.bx, self.y_links(nr)
        return self.rx, self.y_rechts(nr)

    def benutze(self, nr, color):
        self.used[nr] = color
        return self.pin(nr)

    def board(self):
        h = 19 * P + 40
        y0 = TOP - 20
        self.add(f"<rect x='{self.bx + BOARD_W / 2 - 22}' y='{y0 - 22}' width='44' height='28' rx='4' fill='#b8b8b8' stroke='#777'/>")
        self.text(self.bx + BOARD_W / 2, y0 - 28, "USB", 11, "middle", "#555")
        self.add(f"<rect x='{self.bx}' y='{y0}' width='{BOARD_W}' height='{h}' rx='8' fill='#1f7a3d' stroke='#145228' stroke-width='2'/>")
        self.add(f"<text x='{self.bx + BOARD_W / 2}' y='{y0 + h / 2}' font-size='20' text-anchor='middle' fill='#ffffff' fill-opacity='0.25' {FONT} font-weight='bold' transform='rotate(-90 {self.bx + BOARD_W / 2} {y0 + h / 2})'>Raspberry Pi Pico 2 W</text>")
        for nr, name in list(LEFT_PINS.items()) + list(RIGHT_PINS.items()):
            x, y = self.pin(nr)
            benutzt = nr in self.used
            fill = "#f2c14e" if benutzt else "#c9a64a"
            self.add(f"<circle cx='{x}' cy='{y}' r='{6 if benutzt else 4}' fill='{fill}' stroke='#7a5b10'/>")
            farbe = "#ffffff" if benutzt else "#9fd3ae"
            size = 12 if benutzt else 10
            if nr <= 20:
                self.text(x + 12, y + 4, f"{nr}", size - 1, "start", farbe, benutzt)
                self.text(x + 34, y + 4, name, size, "start", farbe, benutzt)
            else:
                self.text(x - 12, y + 4, f"{nr}", size - 1, "end", farbe, benutzt)
                self.text(x - 34, y + 4, name, size, "end", farbe, benutzt)

    # --- Bauteile, waagrecht (links vom Board) ------------------------------
    def widerstand_h(self, x1, x2, y, wert):
        w = x1 - x2
        self.add(f"<rect x='{x2}' y='{y - 8}' width='{w}' height='16' rx='2' fill='#fff' stroke='#333' stroke-width='2'/>")
        self.text((x1 + x2) / 2, y + 4, wert, 10, "middle", "#222", True)

    def led_h(self, x1, x2, y, farbe):
        """LED zwischen x1 (rechts, Anode +) und x2 (links, Kathode −)."""
        c = LED_COLORS[farbe]
        self.add(f"<polygon points='{x1},{y - 10} {x1},{y + 10} {x2 + 4},{y}' fill='{c}' stroke='#333' stroke-width='2'/>")
        self.add(f"<line x1='{x2 + 4}' y1='{y - 10}' x2='{x2 + 4}' y2='{y + 10}' stroke='#333' stroke-width='3'/>")
        self.text(x1 + 4, y - 9, "+", 11, "start", "#333", True)
        self.text(x2 - 2, y - 9, "−", 11, "end", "#333", True)

    def taste_h(self, x1, x2, y):
        self.line([(x1, y), (x1 - 8, y)], "#333", 2.5)
        self.line([(x2, y), (x2 + 8, y)], "#333", 2.5)
        self.dot(x1 - 8, y, "#333")
        self.dot(x2 + 8, y, "#333")
        self.line([(x1 - 6, y - 9), (x2 + 6, y - 9)], "#333", 2.5)
        m = (x1 + x2) / 2
        self.line([(m, y - 9), (m, y - 15)], "#333", 2.5)

    # --- Bauteile, senkrecht (rechts vom Board) -----------------------------
    def widerstand_v(self, x, y1, y2, wert, label=None):
        self.add(f"<rect x='{x - 8}' y='{y1}' width='16' height='{y2 - y1}' rx='2' fill='#fff' stroke='#333' stroke-width='2'/>")
        self.text(x + 16, (y1 + y2) / 2 + 4, wert, 12, "start", "#222", True)
        if label:
            self.text(x + 16, (y1 + y2) / 2 + 20, label, 11, "start", "#555")

    def ldr_v(self, x, y1, y2):
        self.widerstand_v(x, y1, y2, "LDR", "Lichtsensor")
        m = (y1 + y2) / 2
        for dy in (-10, 4):
            self.line([(x - 30, m + dy - 10), (x - 13, m + dy)], "#e0a800", 2)
            self.add(f"<polygon points='{x - 13},{m + dy} {x - 21},{m + dy - 1} {x - 17},{m + dy - 6}' fill='#e0a800'/>")

    def piezo_v(self, x, y1, y2):
        self.add(f"<line x1='{x - 14}' y1='{y1}' x2='{x + 14}' y2='{y1}' stroke='#333' stroke-width='3'/>")
        self.add(f"<line x1='{x - 14}' y1='{y2}' x2='{x + 14}' y2='{y2}' stroke='#333' stroke-width='3'/>")
        self.add(f"<rect x='{x - 10}' y='{y1 + 5}' width='20' height='{y2 - y1 - 10}' fill='#ddd' stroke='#333' stroke-width='2'/>")
        self.text(x - 18, y1 + 4, "+", 13, "end", "#333", True)
        self.text(x - 18, y2 + 4, "−", 13, "end", "#333", True)

    # --- fertige Reihen -----------------------------------------------------
    def reihe_led(self, pin, farbe, ohm, label, gnd_x):
        x, y = self.benutze(pin, LED_COLORS[farbe])
        sig = LED_COLORS[farbe] if farbe != "warmweiß" else "#c9a227"
        self.line([(x, y), (x - 50, y)], sig)
        self.widerstand_h(x - 50, x - 110, y, ohm)
        self.line([(x - 110, y), (x - 135, y)], "#333")
        self.led_h(x - 135, x - 170, y, farbe)
        self.line([(x - 166, y), (gnd_x, y)], GND_C)
        self.dot(gnd_x, y, GND_C)
        self.text(gnd_x - 14, y + 4, label, 12, "end", "#222", True)

    def reihe_taste(self, pin, label, gnd_x):
        x, y = self.benutze(pin, SIG_C)
        self.line([(x, y), (x - 112, y)], SIG_C)
        self.taste_h(x - 112, x - 160, y)
        self.line([(x - 160, y), (gnd_x, y)], GND_C)
        self.dot(gnd_x, y, GND_C)
        self.text(gnd_x - 14, y + 4, label, 12, "end", "#222", True)

    def gnd_links(self, pins, alle_reihen, gnd_x, extra_ys=()):
        for p in pins:
            x, y = self.benutze(p, GND_C)
            self.line([(x, y), (gnd_x, y)], GND_C)
            self.dot(gnd_x, y, GND_C)
        ys = [self.y_links(p) for p in alle_reihen + pins] + list(extra_ys)
        self.line([(gnd_x, min(ys)), (gnd_x, max(ys))], GND_C, 4)
        self.text(gnd_x, max(ys) + 32, "GND", 11, "middle", GND_C, True)

    def spannungsteiler(self, oben, oben_label, unten, unten_label):
        """3V3 → oben → GP26 → unten → GND (Beinchen 36, 31, 28)."""
        xs = self.rx + 110
        x36, y36 = self.benutze(36, V33_C)
        x31, y31 = self.benutze(31, SIG_C)
        x28, y28 = self.benutze(28, GND_C)
        self.line([(x36, y36), (xs, y36), (xs, y36 + 30)], V33_C)
        oben(xs, y36 + 30, y31 - 30)
        self.line([(xs, y31 - 30), (xs, y31)], "#333")
        self.line([(x31, y31), (xs, y31)], SIG_C)
        self.dot(xs, y31, SIG_C)
        self.line([(xs, y31), (xs, y31 + 14)], "#333")
        unten(xs, y31 + 14, y28 - 14)
        self.line([(xs, y28 - 14), (xs, y28), (x28, y28)], GND_C)
        self.max_x = max(self.max_x, xs + 130)

    def pir(self):
        xv = self.rx + 260
        xb = xv + 40
        x40, y40 = self.benutze(40, V5_C)
        x23, y23 = self.benutze(23, GND_C)
        x22, y22 = self.benutze(22, SIG_C)
        y_vcc = y23 - P
        self.line([(x40, y40), (xv, y40), (xv, y_vcc), (xb, y_vcc)], V5_C)
        self.text(x40 + 14, y40 - 8, "5 V", 11, "start", V5_C, True)
        self.line([(x23, y23), (xb, y23)], GND_C)
        self.line([(x22, y22), (xb, y22)], SIG_C)
        top, bot = y_vcc - 26, y22 + 26
        self.add(f"<rect x='{xb}' y='{top}' width='130' height='{bot - top}' rx='6' fill='#2f6f3f' stroke='#1d4527' stroke-width='2'/>")
        self.add(f"<circle cx='{xb + 92}' cy='{(top + bot) / 2}' r='26' fill='#f4f4f4' stroke='#bbb' stroke-width='2'/>")
        for y, t in ((y_vcc, "VCC"), (y23, "GND"), (y22, "OUT")):
            self.add(f"<circle cx='{xb}' cy='{y}' r='4' fill='#f2c14e' stroke='#7a5b10'/>")
            self.text(xb + 10, y + 4, t, 11, "start", "#fff", True)
        self.text(xb + 65, top - 8, "Bewegungsmelder HC-SR501", 12, "middle", "#222", True)
        self.max_x = max(self.max_x, xb + 150)

    def tmp36(self):
        xb = self.rx + 120
        reihen = ((36, "+Vs", V33_C), (31, "Vout", SIG_C), (28, "GND", GND_C))
        for pin, t, c in reihen:
            x, y = self.benutze(pin, c)
            self.line([(x, y), (xb, y)], c)
        top, bot = self.y_rechts(36) - 30, self.y_rechts(28) + 30
        self.add(f"<rect x='{xb}' y='{top}' width='90' height='{bot - top}' rx='6' fill='#222' stroke='#000'/>")
        for pin, t, c in reihen:
            y = self.y_rechts(pin)
            self.add(f"<circle cx='{xb}' cy='{y}' r='4' fill='#c0c0c0'/>")
            self.text(xb + 10, y + 4, t, 12, "start", "#fff", True)
        self.text(xb + 45, top - 8, "TMP36", 13, "middle", "#222", True)
        # Ansicht von vorne
        ox, oy = xb + 140, top + 10
        self.text(ox + 60, oy, "von vorne (flache Seite):", 11, "middle", "#555")
        self.add(f"<path d='M {ox + 15} {oy + 56} L {ox + 15} {oy + 28} A 45 24 0 0 1 {ox + 105} {oy + 28} L {ox + 105} {oy + 56} Z' fill='#222'/>")
        self.text(ox + 60, oy + 46, "TMP36", 10, "middle", "#ddd")
        for i, (t, c) in enumerate((("+Vs", V33_C), ("Vout", SIG_C), ("GND", GND_C))):
            lx = ox + 25 + i * 35
            self.line([(lx, oy + 56), (lx, oy + 86)], "#999", 3)
            self.text(lx, oy + 102, t, 11, "middle", c, True)
            self.text(lx, oy + 116, ("links", "Mitte", "rechts")[i], 10, "middle", "#555")
        self.max_x = max(self.max_x, ox + 140)


    def summer_unten(self, gnd_x):
        """Passiver Summer: GP16 (Beinchen 21) → unter dem Board → GND-Schiene links. Liefert die y-Lage."""
        x, y = self.benutze(21, SIG_C)
        yb = y + 60
        self.line([(x, y), (x + 40, y), (x + 40, yb), (self.bx + BOARD_W / 2 + 34, yb)], SIG_C)
        m = self.bx + BOARD_W / 2
        x1, x2 = m + 34, m - 34                 # rechts +, links −
        self.add(f"<line x1='{x1}' y1='{yb - 14}' x2='{x1}' y2='{yb + 14}' stroke='#333' stroke-width='3'/>")
        self.add(f"<line x1='{x2}' y1='{yb - 14}' x2='{x2}' y2='{yb + 14}' stroke='#333' stroke-width='3'/>")
        self.add(f"<rect x='{x2 + 5}' y='{yb - 10}' width='{x1 - x2 - 10}' height='20' fill='#ddd' stroke='#333' stroke-width='2'/>")
        self.text(x1 + 6, yb - 16, "+", 13, "start", "#333", True)
        self.text(x2 - 6, yb - 16, "−", 13, "end", "#333", True)
        self.text(m, yb + 32, "Summer (passiv)", 12, "middle", "#222", True)
        self.line([(x2, yb), (gnd_x, yb)], GND_C)
        self.dot(gnd_x, yb, GND_C)
        self.extra_unten = 70
        return yb

    def servo(self):
        """SG90: rot an VBUS (40), braun an GND (38), orange an GP20 (Beinchen 26)."""
        xb = self.rx + 150
        x40, y40 = self.benutze(40, V5_C)
        x38, y38 = self.benutze(38, GND_C)
        x26, y26 = self.benutze(26, SIG_C)
        y_sig = self.y_rechts(37)
        self.line([(x40, y40), (xb, y40)], V5_C)
        self.text(x40 + 14, y40 - 8, "5 V", 11, "start", V5_C, True)
        self.line([(x38, y38), (xb, y38)], GND_C)
        self.line([(x26, y26), (self.rx + 90, y26), (self.rx + 90, y_sig), (xb, y_sig)], SIG_C)
        top, bot = y40 - 26, y_sig + 26
        self.add(f"<rect x='{xb}' y='{top}' width='130' height='{bot - top}' rx='6' fill='#2457b8' stroke='#163a7a' stroke-width='2'/>")
        for y, t in ((y40, "rot · 5 V"), (y38, "braun · GND"), (y_sig, "orange · Signal")):
            self.add(f"<circle cx='{xb}' cy='{y}' r='4' fill='#f2c14e' stroke='#7a5b10'/>")
            self.text(xb + 10, y + 4, t, 11, "start", "#fff", True)
        self.add(f"<rect x='{xb + 130}' y='{(top + bot) / 2 - 8}' width='70' height='16' rx='8' fill='#f4f4f4' stroke='#999' stroke-width='2'/>")
        self.text(xb + 165, (top + bot) / 2 + 28, "Arm", 11, "middle", "#555")
        self.text(xb + 65, top - 8, "Servo SG90", 12, "middle", "#222", True)
        self.max_x = max(self.max_x, xb + 220)

    def modul(self, xb, name, farbe, reihen):
        """Sensor-Modul als Kasten; reihen: [(y, Beschriftung)]."""
        ys = [y for y, _ in reihen]
        top, bot = min(ys) - 26, max(ys) + 22
        self.add(f"<rect x='{xb}' y='{top}' width='130' height='{bot - top}' rx='6' fill='{farbe}' stroke='#111' stroke-width='2'/>")
        for y, t in reihen:
            self.add(f"<circle cx='{xb}' cy='{y}' r='4' fill='#f2c14e' stroke='#7a5b10'/>")
            self.text(xb + 10, y + 4, t, 11, "start", "#fff", True)
        self.text(xb + 65, top - 8, name, 12, "middle", "#222", True)
        self.max_x = max(self.max_x, xb + 150)

    def boden_und_regen(self):
        """Regensensor (AO an GP27, Beinchen 32) und Bodenfeuchte (AOUT an GP26, Beinchen 31), beide an 3V3."""
        xr = self.rx + 140                      # Regen-Modul
        xv = xr + 170                           # 3V3-Leitung zum Bodenmodul
        xs = xv + 40                            # Boden-Modul
        x36, y36 = self.benutze(36, V33_C)
        x33, y33 = self.benutze(33, GND_C)
        x32, y32 = self.benutze(32, SIG_C)
        x31, y31 = self.benutze(31, SIG_C)
        x28, y28 = self.benutze(28, GND_C)
        self.line([(x36, y36), (xr, y36)], V33_C)
        self.text(x36 + 14, y36 - 8, "3,3 V", 11, "start", V33_C, True)
        j = self.rx + 90
        self.dot(j, y36, V33_C)
        self.line([(j, y36), (j, y36 - 48), (xv, y36 - 48), (xv, y32), (xs, y32)], V33_C)
        self.line([(x33, y33), (xr, y33)], GND_C)
        self.line([(x32, y32), (xr, y32)], SIG_C)
        self.line([(x31, y31), (xs, y31)], SIG_C)
        self.line([(x28, y28), (xs, y28)], GND_C)
        self.modul(xr, "Regensensor (Modul)", "#1d4e89", [(y36, "VCC"), (y33, "GND"), (y32, "AO")])
        self.modul(xs, "Bodenfeuchtesensor", "#333", [(y32, "VCC"), (y31, "AOUT"), (y28, "GND")])

    # --- Ausgabe -----------------------------------------------------------
    def svg(self, titel, hinweise):
        breite = max(self.max_x + 20, 900)
        unten = TOP + 19 * P + 70 + self.extra_unten
        h = unten + 24 * len(hinweise) + 20
        kopf = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {breite} {h}' width='{breite}' height='{h}'>",
                f"<rect width='100%' height='100%' fill='#ffffff'/>",
                f"<text x='20' y='34' font-size='20' {FONT} font-weight='bold' fill='#222'>{esc(titel)}</text>",
                f"<text x='20' y='56' font-size='12' {FONT} fill='#555'>Zeigt, was womit verbunden ist, nicht wo es auf dem Steckbrett sitzt. USB-Kabel beim Stecken abziehen!</text>"]
        fuss = []
        for i, t in enumerate(hinweise):
            fuss.append(f"<text x='20' y='{unten + 24 * i}' font-size='12' {FONT} fill='#333'>{esc(t)}</text>")
        return "\n".join(kopf + self.teile + fuss + ["</svg>"]) + "\n"


STANDARD = [
    "Beinchen-Nummern: USB oben, 1 oben links bis 20 unten links, 21 unten rechts bis 40 oben rechts.",
    "LED: das lange Bein (+) zeigt zum Widerstand, das kurze Bein (−) zu GND.  Taster: zwei diagonal gegenüberliegende Beinchen.",
    "Kabelfarben im Bild: schwarz = GND, rot = 3,3 V, lila = 5 V, blau = Signal. Eure Kabel dürfen andere Farben haben.",
]


def zeichne(ordner, titel, links, rechts=None, extra=()):
    """links: Liste von ("led", beinchen, farbe, ohm, label), ("taste", beinchen, label), ("gnd", [beinchen]),
    ("summer",) für den Summer an GP16 (unter dem Board zur GND-Schiene).
    rechts: "ldr", "piezo", "tmp36", "pir", "servo", "boden_regen".

    Achtung: Beinchen-Nummer, nicht GP-Nummer (GP15 = Beinchen 20).
    """
    b = Bild()
    gnd_x = b.bx - 210
    reihen, gnd_pins, extra_ys = [], [], []
    for teil in links:
        if teil[0] == "led":
            _, pin, farbe, ohm, label = teil
            b.reihe_led(pin, farbe, ohm, label, gnd_x)
            reihen.append(pin)
        elif teil[0] == "taste":
            _, pin, label = teil
            b.reihe_taste(pin, label, gnd_x)
            reihen.append(pin)
        elif teil[0] == "gnd":
            gnd_pins += teil[1]
        elif teil[0] == "summer":
            extra_ys.append(b.summer_unten(gnd_x))
    b.gnd_links(gnd_pins, reihen, gnd_x, extra_ys)
    for r in rechts or []:
        if r == "ldr":
            b.spannungsteiler(b.ldr_v, "", lambda x, y1, y2: b.widerstand_v(x, y1, y2, "10 kΩ"), "")
        elif r == "piezo":
            def unten(x, y1, y2):
                b.piezo_v(x, y1, y2)
                x2 = x + 90
                b.line([(x, y1 - 14), (x2, y1 - 14), (x2, y1 + 6)], "#333")
                b.widerstand_v(x2, y1 + 6, y2 + 6, "1 MΩ", "parallel")
                b.line([(x2, y2 + 6), (x2, y2 + 14), (x, y2 + 14)], GND_C)
                b.text(x - 30, (y1 + y2) / 2 + 4, "Piezo", 12, "end", "#222", True)
            # Piezo hängt nur zwischen GP26 und GND (kein 3V3)
            x31, y31 = b.benutze(31, SIG_C)
            x28, y28 = b.benutze(28, GND_C)
            xs = b.rx + 110
            b.line([(x31, y31), (xs, y31)], SIG_C)
            b.dot(xs, y31, SIG_C)
            b.line([(xs, y31), (xs, y31 + 14)], "#333")
            unten(xs, y31 + 14, y28 - 14)
            b.line([(xs, y28 - 14), (xs, y28), (x28, y28)], GND_C)
            b.dot(xs, y28, GND_C)
            b.max_x = max(b.max_x, xs + 170)
        elif r == "tmp36":
            b.tmp36()
        elif r == "pir":
            b.pir()
        elif r == "servo":
            b.servo()
        elif r == "boden_regen":
            b.boden_und_regen()
    b.board()
    (HIER / ordner / "schaltung.svg").write_text(b.svg(titel, STANDARD + list(extra)), encoding="utf-8")
    print("geschrieben:", ordner)


zeichne("265a-team-01", "Schaltung · Österreichische Ampel", [
    ("led", 20, "rot", "220 Ω", "LED rot"),
    ("led", 17, "gelb", "220 Ω", "LED gelb"),
    ("led", 16, "grün", "220 Ω", "LED grün"),
    ("gnd", [18]),
])

zeichne("265a-team-02", "Schaltung · Gartenlicht mit Bewegungsmelder", [
    ("led", 20, "warmweiß", "100 Ω", "LED warmweiß"),
    ("gnd", [18]),
], ["ldr", "pir"], [
    "Bewegungsmelder: Beschriftung VCC/OUT/GND steht unter der weißen Kuppel. Die LED nicht auf den Lichtsensor richten.",
])

zeichne("265a-team-03", "Schaltung · Raffstore-Steuerung", [
    ("taste", 15, "Taste RUNTER"),
    ("led", 17, "gelb", "220 Ω", "LED gelb (oben)"),
    ("taste", 19, "Taste HOCH"),
    ("led", 20, "rot", "220 Ω", "LED rot (unten)"),
    ("gnd", [13, 18]),
])

zeichne("265a-team-04", "Schaltung · Smarter Backofen", [
    ("led", 20, "rot", "220 Ω", "LED rot (Ofen)"),
    ("gnd", [18]),
], ["pir"], [
    "Bewegungsmelder: Beschriftung VCC/OUT/GND steht unter der weißen Kuppel.",
])

zeichne("265a-team-05", "Schaltung · Lüftungsampel", [
    ("led", 17, "gelb", "220 Ω", "LED gelb"),
    ("taste", 19, "Taste"),
    ("led", 20, "rot", "220 Ω", "LED rot"),
    ("gnd", [18]),
], ["tmp36"], [
    "TMP36: flache Seite zu euch, Beinchen nach unten. Falsch herum wird er heiß, dann sofort USB abziehen.",
])

zeichne("265a-team-06", "Schaltung · Lautstärkeampel", [
    ("led", 16, "grün", "220 Ω", "LED grün"),
    ("led", 17, "gelb", "220 Ω", "LED gelb"),
    ("taste", 19, "Taste"),
    ("led", 20, "rot", "220 Ω", "LED rot"),
    ("gnd", [18]),
], ["piezo"], [
    "Piezo: der 1-MΩ-Widerstand steckt in denselben zwei Reihen wie die Beinchen des Piezos (parallel).",
])

zeichne("265a-team-07", "Schaltung · Reaktionsspiel", [
    ("taste", 19, "Taste"),
    ("led", 20, "rot", "220 Ω", "LED rot"),
    ("gnd", [18]),
])

zeichne("265a-team-08", "Schaltung · Handy-Ein/Aus-Taste", [
    ("taste", 19, "Taste"),
    ("led", 20, "rot", "220 Ω", "LED rot (Display)"),
    ("gnd", [18]),
])


# --- Klasse 265b -------------------------------------------------------------

zeichne("265b-team-01", "Schaltung · Türklingel", [
    ("taste", 19, "Klingeltaste"),
    ("led", 20, "gelb", "220 Ω", "LED gelb"),
    ("gnd", [18]),
    ("summer",),
])

zeichne("265b-team-02", "Schaltung · Alarmanlage", [
    ("taste", 19, "Taste"),
    ("led", 20, "rot", "220 Ω", "LED rot (scharf)"),
    ("gnd", [18]),
    ("summer",),
], ["pir"], [
    "Bewegungsmelder: Beschriftung VCC/OUT/GND steht unter der weißen Kuppel.",
])

zeichne("265b-team-03", "Schaltung · Kühlschranklicht", [
    ("taste", 15, "Türkontakt (Taste)"),
    ("taste", 19, "Taste AUS/AUTO"),
    ("led", 20, "warmweiß", "100 Ω", "LED warmweiß"),
    ("gnd", [13, 18]),
])

zeichne("265b-team-04", "Schaltung · Klimawächter", [
    ("led", 16, "grün", "220 Ω", "LED grün"),
    ("led", 17, "blau", "100 Ω", "LED blau"),
    ("taste", 19, "Taste"),
    ("led", 20, "rot", "220 Ω", "LED rot"),
    ("gnd", [18]),
], ["tmp36"], [
    "TMP36: flache Seite zu euch, Beinchen nach unten. Falsch herum wird er heiß, dann sofort USB abziehen.",
])

zeichne("265b-team-05", "Schaltung · Bewässerungsanlage", [
    ("led", 16, "grün", "220 Ω", "LED grün (EIN)"),
    ("taste", 19, "Taste"),
    ("led", 20, "blau", "100 Ω", "LED blau (Pumpe)"),
    ("gnd", [18]),
], ["boden_regen"], [
    "Beide Sensoren bekommen 3,3 V vom selben Beinchen 36. Elektronik und Pico trocken halten, nur die Sensorspitzen ins Wasser.",
])

zeichne("265b-team-06", "Schaltung · Tageslichtlampe", [
    ("taste", 19, "Taste"),
    ("led", 20, "warmweiß", "100 Ω", "LED warmweiß"),
    ("gnd", [18]),
], ["ldr"], [
    "Die LED nicht auf den Lichtsensor richten.",
])

zeichne("265b-team-07", "Schaltung · Nachtlicht", [
    ("taste", 19, "Taste"),
    ("led", 20, "warmweiß", "100 Ω", "LED warmweiß"),
    ("gnd", [18]),
], ["ldr"], [
    "Die LED nicht auf den Lichtsensor richten.",
])

zeichne("265b-team-08", "Schaltung · Futterautomat", [
    ("taste", 15, "Taste MENGE"),
    ("taste", 19, "Taste FÜTTERN"),
    ("gnd", [13, 18]),
], ["servo"], [
    "Servo: Startet der Pico neu, sobald sich der Servo bewegt, reicht der USB-Strom nicht. Dann Lehrkraft fragen.",
])
