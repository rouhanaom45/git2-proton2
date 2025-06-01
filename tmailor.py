import pyautogui
import time
import subprocess

# Path to Chrome browser executable
chrome_path = "/usr/bin/google-chrome"

# Function to wait for a specified time
def wait(seconds):
    time.sleep(seconds)

# Main Script
# Step 1: Sleep for 1 second
wait(1)

# Step 2: Open Chrome in incognito mode
subprocess.run([
    chrome_path,
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-software-rasterizer",
    "--remote-debugging-port=9222",
    "--incognito",
    "about:blank"  # Start with a blank page
])
wait(2.5)

# Step 3: Write "tmailor.com" and press Enter
pyautogui.write("tmailor.com")
time.sleep(0.7)
pyautogui.press("enter")
wait(10)
subprocess.run(["python3", "consent.py"])
time.sleep(1)
subprocess.run(["python3", "copy0.py"])
time.sleep(2)

pyautogui.click(1169, 631)
wait(1)
# Step 6: Click on (538, 62)
pyautogui.click(549, 628)
wait(2)
