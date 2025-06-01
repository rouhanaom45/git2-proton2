# main_script.py
import pyautogui
import time
import subprocess

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

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('detector1.py')

    
