import time
import pyautogui
import tkinter as tk 

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/Akash/Documents/Python-learning/screenshot/screenshot_data/{}.png'.format(name)
    # time.sleep(5) GUI Wait till 5sec
    time.sleep(2)
    img  = pyautogui.screenshot(name)
    img.show()

# screenshot()

# during run pillo required message come, cmd administator mode pip install Pillow --upgrade and finally run

root  = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take Screenshot",
    command = screenshot
)
button.pack(side = tk.LEFT)

close = tk.Button(
    frame,
    text = "QUIT",
    command = quit
)
close.pack(side = tk.LEFT)

root.mainloop()