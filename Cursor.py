import warnings
warnings.filterwarnings("ignore")
import pyautogui
import threading
import time

minutes = 450

def timer(timer_runs):
    time.sleep(5)
    while timer_runs.is_set():
        x,y = 749,375
        #x,y = 766,1065
        #x,y, = 3737,786
        pyautogui.moveTo(x,y)
        pyautogui.doubleClick()
        time.sleep(60)
        x, y = 760,380
        pyautogui.moveTo(x,y)
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer,args=(timer_runs,))
t.start()
time.sleep(60*minutes)
timer_runs.clear()
