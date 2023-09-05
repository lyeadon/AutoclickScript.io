import pyautogui
import keyboard

while True:
    if keyboard.is_pressed("1") and keyboard.is_pressed("ctrl"):
        pyautogui.click(200, 655, duration = 0.5)
        pyautogui.click(1000, 300, duration = 0.5)
        pyautogui.typewrite("NA")
        pyautogui.click(1000, 375, duration = 0.5)
        pyautogui.click(1000, 475, duration = 0.5)
        pyautogui.click(1100, 575, duration = 0.5)

    if keyboard.is_pressed("2") and keyboard.is_pressed("ctrl"):
        pyautogui.click(1000, 300, duration = 0.5)
        pyautogui.typewrite("Do not call")
        pyautogui.click(1000, 375, duration = 0.5)
        pyautogui.click(1000, 525, duration = 0.5)
        pyautogui.click(1100, 450, duration = 0.5)

    if keyboard.is_pressed("3") and keyboard.is_pressed("ctrl"):
        pyautogui.click(1000, 300, duration = 0.5)
        pyautogui.typewrite("Gate Keeper")
        pyautogui.click(1000, 375, duration = 0.5)
        pyautogui.click(1000, 550, duration = 0.5)
        pyautogui.click(1100, 450, duration = 0.5)


    if keyboard.is_pressed("4") and keyboard.is_pressed("ctrl"):
        pyautogui.click(1000, 300, duration = 0.5)
        pyautogui.typewrite("Not interested")
        pyautogui.click(1000, 375, duration = 0.5)
        pyautogui.click(1000, 500, duration = 0.5)
        pyautogui.click(1100, 450, duration = 0.5)

    if keyboard.is_pressed("5") and keyboard.is_pressed("ctrl"):
        pyautogui.click(1000, 300, duration = 0.5)
        pyautogui.typewrite("CB")
        pyautogui.click(1000, 375, duration = 0.5)
        pyautogui.click(1000, 450, duration = 0.5)
        pyautogui.click(1100, 575, duration = 0.5)

    if keyboard.is_pressed("6") and keyboard.is_pressed("ctrl"):
        pyautogui.click(1000, 300, duration = 0.5)
        pyautogui.typewrite("WN")
        pyautogui.click(1000, 375, duration = 0.5)
        pyautogui.click(1000, 575, duration = 0.5)
        pyautogui.click(1100, 450, duration = 0.5)

    if keyboard.is_pressed("8") and keyboard.is_pressed("ctrl"):
        pyautogui.click(1000, 300, duration = 0.5)
        pyautogui.typewrite("Hung up")
        pyautogui.click(1000, 375, duration = 0.5)
        pyautogui.click(1000, 600, duration = 0.5)
        pyautogui.click(1100, 575, duration = 0.5)