import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    time.sleep(5)
    img  = pyautogui.screenshot(name)
    img.show()

screenshot()

# during run pillo required message come, cmd administator mode pip install Pillow --upgrade and finally run