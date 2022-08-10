import pyautogui as pg
import time

print("program will rn i 6 sec")
time.sleep(6)

for i in range(50):
    pg.write("jiji")
    time.sleep(0.6)
    pg.press("Enter")
