#Gets speech recognition engine, Speak() function,
from Engine import *



# Following are some of the Mouse functions
 
def left_click():
    """
    Left click.
    """
    speak("Left button clicked")
    pyautogui.click(button='left')
    
def double_click():
    """
    2 Left click.
    """
    speak("Left button clicked twice")
    pyautogui.click(clicks=2,button='left')


def right_click():
    """
    Right click.
    """
    speak("Right button clicked")
    pyautogui.click(button='right')
    
def drag():
    speak("drag initiated")
    pyautogui.click(button='left')
    pyautogui.mouseDown()

def hold_leftButt():
    speak("holding Left button")
    pyautogui.mouseDown()
    
def release_leftButt():
    speak("releasing Left button")
    pyautogui.mouseUp()

