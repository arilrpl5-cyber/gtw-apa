import time
import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)

os.system("cls" if os.name == "nt" else "clear")

lyrics = [
    ("mbg...", 1),
    ("( mas bahlil ganteng )", 0.8),
    ("buah apa yang paling manis...", 0.6),
    ("BUAAAHLILLLLL 😭🔥", 0.7),
    ("tambah ganteng aja...", 0.6),
    ("my little bolu ketan 💖", 0.5),
]

aqua = Fore.WHITE

def ketik(text, speed=0.060):
    for char in text:
        sys.stdout.write(aqua + Style.BRIGHT + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading():
    print(aqua + "\nloading music...\n")

    for i in range(31):
        bar = "█" * i + "░" * (30 - i)

        sys.stdout.write(
            aqua + f"\r[{bar}] {i * 3}%"
        )

        sys.stdout.flush()
        time.sleep(0.05)

    print("\n")

print(aqua + Style.BRIGHT + r"""
╔══════════════════════════════════╗
║                                  ║
║         🎧 TERMINAL MUSIC        ║
║                                  ║
║      MBG - BUAHLIL EDITION       ║
║                                  ║
╚══════════════════════════════════╝
""")

time.sleep(1)

loading()

os.system("cls" if os.name == "nt" else "clear")

print(aqua + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(aqua + "▶ NOW PLAYING")
print(aqua + Style.BRIGHT + "MBG - Mas Bahlil Ganteng")
print(aqua + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

for text, delay in lyrics:

    sys.stdout.write(aqua + "♫  ")
    sys.stdout.flush()

    ketik(text)

    bars = ["▁▂▃▄▅", "▅▄▃▂▁", "▃▄▅▄▃"]

    for b in bars:
        sys.stdout.write(
            aqua + "\r♫ " + b
        )
        sys.stdout.flush()
        time.sleep(0.15)

    print("\r                ")

    time.sleep(delay)

ending = "♪ mas bahlill 💖 ♪"

print()

for c in ending:
    sys.stdout.write(aqua + Style.BRIGHT + c)
    sys.stdout.flush()
    time.sleep(0.03)

print("\n")
print(aqua + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")