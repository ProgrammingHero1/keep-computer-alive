import pyautogui
import time
pyautogui.FAILSAFE = False

while True:
    time.sleep(300)
    for i in range(0, 100):
        pyautogui.moveTo(0, i*5)
    for i in range(0, 3):
        pyautogui.press("shift")
