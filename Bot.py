import pyautogui
import time
import keyboard
import random

def click(x,y):
    pyautogui.moveTo(x,y)
    if x == 669:
        pyautogui.press('d')
    elif x == 752:
        pyautogui.press('f')
    elif x == 836:
        pyautogui.press('j')
    elif x == 923:
        pyautogui.press('k')
    time.sleep(0.015) #This pauses the script for 0.01 seconds


while keyboard.is_pressed('q') == False:

    if pyautogui.pixelMatchesColor(669, 465,(0, 0, 0)):
        click(669, 465)
    if pyautogui.pixelMatchesColor(752, 465,(0, 0, 0)):
        click(752, 465)
    if pyautogui.pixelMatchesColor(836, 465,(0, 0, 0)):
        click(836, 465)
    if pyautogui.pixelMatchesColor(923, 465,(0, 0, 0)):
        click(923, 465)
