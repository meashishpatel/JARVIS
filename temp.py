import pyautogui
import time
pyautogui.keyDown("win")
pyautogui.keyUp("win")
# time.sleep(2)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
pyautogui.keyUp("enter")