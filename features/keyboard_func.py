from datetime import datetime
from pyautogui import screenshot, press
from keyboard import press_and_release
from time import sleep

def screenshot():
    c_time = datetime.now().strftime("%d %m %Y")
    kk = screenshot()
    kk.save(f"screenshot_{c_time}.png")

def minimize():
    press_and_release("windows + m")
    return("I have Minimized it")

def laptop_settings():
    press_and_release("windows + i")
    return("Opened Settings")

def search_history():
    open("www.google.com")
    sleep(4)
    press_and_release("ctrl + h")
    return("Opened Your Search History")

def volumeup():
    press("volumeup")
    press("volumeup")
    press("volumeup")
    press("volumeup")
    press("volumeup")
    return("Volume has Increased!")

def volumedown():
    press("volumedown")
    press("volumedown")
    press("volumedown")
    press("volumedown")
    press("volumedown")
    return("Volume has Decreased!")

def volumemute():
    press("volumemute")
    return("I have Muted the System")

def volumeunmute():
    press("volumeup")
    press("volumedown")
    return("I have Unmuted the System")