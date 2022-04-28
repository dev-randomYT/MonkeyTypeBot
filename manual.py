import pyautogui
import time as t
import keyboard as kb

t.sleep(4)

text = "The headache wouldn't go away. She's taken medicine but even that didn't help. The monstrous throbbing in her head continued. She had this happen to her only once before in her life and she realized that only one thing could be happening."

charList = [i for i in text]

t.sleep(0.01)

for char in charList:
    kb.write(text)
    