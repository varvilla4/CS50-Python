import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(figlet.getFonts()))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--f"):
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit("Font doesn't exist")
else:
    sys.exit("No the correct amount of argumnets")

str = input("Input: ")
print(f"Output: {figlet.renderText(str)}")



