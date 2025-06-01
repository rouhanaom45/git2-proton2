import pyautogui
import random
import time
import subprocess

def random_wait(min_time, max_time):
    time.sleep(random.uniform(min_time, max_time))

def random_click_within_rect(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)
    time.sleep(random.uniform(0.1, 0.3))  # Simulate human-like click

# Perform actions step by step
# Step 1: Perform a random click within the first rectangular area
random_click_within_rect((366, 348), (830, 360))
random_wait(0.5, 1)

# Step 2: Press Ctrl+V and sleep
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Step 3: Perform a random click within the second rectangular area
random_click_within_rect((428, 438), (900, 453))
random_wait(10, 12)

# Step 4: Run the script "continue.py" using subprocess
subprocess.run(["python3", "continue11.py"])
time.sleep(2)

# Step 5: Perform a random click within the third rectangular area
random_click_within_rect((504, 504), (838, 528))
random_wait(6, 8)

# Step 6: Perform a random click within the fourth rectangular area
random_click_within_rect((516, 482), (611, 498))
random_wait(0.5, 1)

# Step 7: Perform a random click within the fifth rectangular area
random_click_within_rect((501, 587), (843, 606))
random_wait(10, 12)

# Step 8: Run the script "welcom.py" using subprocess
subprocess.run(["python3", "welcom2.py"])
time.sleep(2)

# Step 9: Perform a sequence of random clicks with delays
random_click_within_rect((510, 551), (843, 570))
random_wait(3, 4)

random_click_within_rect((514, 549), (839, 569))
random_wait(3, 4)

random_click_within_rect((515, 550), (838, 572))
random_wait(3, 4)

random_click_within_rect((509, 564), (840, 585))
random_wait(3, 4)
pyautogui.click(93, 65)
time.sleep(2.5)
subprocess.run(["python3", "clik.py"])
# Step 10: Click on specific points and sleep
time.sleep(1.5)
pyautogui.press("tab")
time.sleep(0.6)
pyautogui.press("tab")
time.sleep(0.6)

# Press Enter key
pyautogui.press("enter")
time.sleep(1.7)
pyautogui.click(93, 65)
time.sleep(2.5)

pyautogui.click(293, 23)
time.sleep(1)
pyautogui.click(535, 64)
time.sleep(0.5)

time.sleep(0.7)
pyautogui.write('chrome://password-manager/passwords/proton.me')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(4)

pyautogui.click(454, 461)
time.sleep(1.5)

pyautogui.hotkey('ctrl', 'a')
time.sleep(0.4)

pyautogui.press('delete')
time.sleep(0.7)

pyautogui.hotkey('ctrl', 'v')
time.sleep(0.8)

pyautogui.click(889, 566)
time.sleep(4)

pyautogui.click(495, 21)
time.sleep(1.5)

subprocess.run(["python", "email-inbox.py"])
time.sleep(1)
