import random
import sys
from pyfiglet import Figlet
figlet = Figlet()



if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    i = input('Input: ')


elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in figlet.getFonts():
            f = sys.argv[2]
            figlet.setFont(font=f)
            i = input('Input: ')

else:
    sys.exit('Invalid Usage')


print(figlet.renderText(i))
