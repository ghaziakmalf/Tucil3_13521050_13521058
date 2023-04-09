from lib.colors import *

def commandStart():
    """
    Splash for start/exit
    Input: -
    Output: Print start/exit command
    """

    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|               START/EXIT               |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " START")
    print(LIGHT_RED + "2." + WHITE + " EXIT")


def commandAlgorithm():
    """
    Splash for algorithm selection
    Input: -
    Output: Print algorithm selection command
    """

    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|             PICK ALGORITHM             |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " UNIFORM COST SEARCH (UCS)")
    print(LIGHT_RED + "2." + WHITE + " A* SEARCH")
    print(LIGHT_RED + "3." + WHITE + " BOTH")


def commandInputOption():
    """
    Splash for input option
    Input: -
    Output: Print input option command
    """

    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|             INPUT OPTIONS              |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " FILE")
    print(LIGHT_RED + "2." + WHITE + " GOOGLE MAPS")


def commandSave():
    """
    Splash for save solution
    Input: -
    Output: Print save solution command
    """

    print(WHITE     + "==========================================")
    print(LIGHT_RED + "|             SAVE SOLUTION?             |")
    print(WHITE     + "==========================================")
    print(LIGHT_RED + "1." + WHITE + " YES")
    print(LIGHT_RED + "2." + WHITE + " NO")