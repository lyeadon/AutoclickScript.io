import pyautogui
import keyboard

while True:
    if keyboard.is_pressed("1"):
        pyautogui.click(1000, 700, duration = 0.5)
        pyautogui.typewrite("NA")

    if keyboard.is_pressed ("2"):
        pyautogui.click(1000, 700, duration = 0.5)
        pyautogui.typewrite("Do not call")


