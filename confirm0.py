# main_script.py
import pyautogui
import time
import subprocess


time.sleep(1)
pyautogui.click(1111, 629)
time.sleep(1)
pyautogui.click(689, 629)
time.sleep(1)
pyautogui.click(96, 63)
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
def detect_web_button(script_name):
    """Run an external script to detect the web button and keep trying until successful."""
    while True:
        # Start the external detection script
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for it to finish

        if process.returncode == 0:  # Success code indicates the button was found
            print(f"Web button detected and clicked by {script_name}. Proceeding with tasks...")
            return  # Exit the loop and proceed to next tasks
        else:
            print(f"Web button not detected by {script_name}. Retrying...")
            time.sleep(1)
            pyautogui.press('down')
            time.sleep(0.1)
            pyautogui.press('down')
            time.sleep(0.1)
            pyautogui.press('down')
            time.sleep(0.1)
def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(31)
    pyautogui.click(96, 63)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(4)
    subprocess.run(["python3", "start00.py"])
    print("All tasks completed.")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.8)  # Wait for 0.8 seconds

    # Copy to clipboard using Ctrl+C  
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1.4)
    subprocess.run(["python3", "clipboard.py"])
    time.sleep(0.7)
    pyautogui.click(1348, 22)
    time.sleep(1.2)
if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('detect.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
