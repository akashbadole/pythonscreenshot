import time
import pyautogui

def screenshot():
    time.sleep(5)
    img = pyautogui.screenshot('akash.png')
    img.show()

screenshot()

# during run pillo required message come, cmd administator mode pip install Pillow --upgrade and finally run