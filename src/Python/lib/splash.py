import time
from lib.colors import *

# Splash Screen
def splash():
    print(LIGHT_GREEN)
    print("    /$$      /$$/$$$$$$$$/$$       /$$$$$$  /$$$$$$ /$$      /$$/$$$$$$$$/$$")
    print("   | $$  /$ | $| $$_____| $$      /$$__  $$/$$__  $| $$$    /$$| $$_____| $$")
    print("   | $$ /$$$| $| $$     | $$     | $$  \\__| $$  \\ $| $$$$  /$$$| $$     | $$")
    print("   | $$/$$ $$ $| $$$$$  | $$     | $$     | $$  | $| $$ $$/$$ $| $$$$$  | $$")
    print("   | $$$$_  $$$| $$__/  | $$     | $$     | $$  | $| $$  $$$| $| $$__/  |__/")
    print("   | $$$/ \\  $$| $$     | $$     | $$    $| $$  | $| $$\\  $ | $| $$         ")
    print("   | $$/   \\  $| $$$$$$$| $$$$$$$|  $$$$$$|  $$$$$$| $$ \\/  | $| $$$$$$$$/$$")
    print("   |__/     \\__|________|________/\\______/ \\______/|__/     |__|________|__/")

    print(WHITE)
    print("W", end="", flush=True)
    time.sleep(0.05)
    print("e", end="", flush=True)
    time.sleep(0.05)
    print("l", end="", flush=True)
    time.sleep(0.05)
    print("c", end="", flush=True)
    time.sleep(0.05)
    print("o", end="", flush=True)
    time.sleep(0.05)
    print("m", end="", flush=True)
    time.sleep(0.05)
    print("e", end="", flush=True)
    time.sleep(0.05)
    print(" ", end="", flush=True)
    time.sleep(0.05)
    print("t", end="", flush=True)
    time.sleep(0.05)
    print("o", end="", flush=True)
    time.sleep(0.05)
    print(" ", end="", flush=True)
    time.sleep(0.05)
    print("S", end="", flush=True)
    time.sleep(0.05)
    print("h", end="", flush=True)
    time.sleep(0.05)
    print("o", end="", flush=True)
    time.sleep(0.05)
    print("r", end="", flush=True)
    time.sleep(0.05)
    print("t", end="", flush=True)
    time.sleep(0.05)
    print("e", end="", flush=True)
    time.sleep(0.05)
    print("s", end="", flush=True)
    time.sleep(0.05)
    print("t", end="", flush=True)
    time.sleep(0.05)
    print(" ", end="", flush=True)
    time.sleep(0.05)
    print("P", end="", flush=True)
    time.sleep(0.05)
    print("a", end="", flush=True)
    time.sleep(0.05)
    print("t", end="", flush=True)
    time.sleep(0.05)
    print("h", end="", flush=True)
    time.sleep(0.05)
    print(" ", end="", flush=True)
    time.sleep(0.05)
    print("S", end="", flush=True)
    time.sleep(0.05)
    print("o", end="", flush=True)
    time.sleep(0.05)
    print("l", end="", flush=True)
    time.sleep(0.05)
    print("v", end="", flush=True)
    time.sleep(0.05)
    print("e", end="", flush=True)
    time.sleep(0.05)
    print("r")

    print(YELLOW)
    print("A Group Algorithm Strategy Project")
    print("Made By " + UNDERLINE + "Naufal Syifa Firdaus (13521050)" + RESET + YELLOW + " and " + UNDERLINE + "Ghazi Akmal Fauzan (13521058)" + RESET)

    print(LIGHT_RED)
    print("Loading", end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)

    print(WHITE)
    print("Solver Loaded!")
    print(RESET)