import pyautogui
import time
from speech2text import Speech2text

# program will sleep for 2 seconds, give you time for place mouse in desirable place
time.sleep(2)
listener = Speech2text()

expression = listener.listen()
print(expression)
commands = expression.split(' ')
print(commands)
for command in commands:
    command = command.replace(" ", "")
    command = command.replace(".", ",")
    print(command)
    pyautogui.write(command)
    pyautogui.press('down')

