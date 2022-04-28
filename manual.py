import pyautogui
import time as t
import keyboard as kb

t.sleep(4)

text = "The quick brown fox jumps over the lazy dog"

charList = [i for i in text]

t.sleep(0.01)

for char in charList:
    kb.write(text)
    