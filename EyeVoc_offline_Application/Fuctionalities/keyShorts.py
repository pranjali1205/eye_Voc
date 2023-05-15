#Gets speech recognition engine, Speak() function,
from Engine import *

#Gets function in mouse.py
from Fuctionalities.mouse import *

    
def mov_up():
    speak("moving up")
    pyautogui.hotkey("up")

def mov_down():
    speak("moving down")
    pyautogui.hotkey("down")
def mov_lft():
    speak("moving left by a character")
    pyautogui.hotkey("left")

def spl_setings():
    speak("opening special settings")
    pyautogui.hotkey("win","a")
    

def win_left():
    speak("moving window to left")
    pyautogui.hotkey("win","left")
    

def win_rgt():
    speak("moving window to right")
    pyautogui.hotkey("win","right")
    

def win_up():
    speak("moving window to up")
    pyautogui.hotkey("win","up")
    

def win_dwn():
    speak("moving window to down")
    pyautogui.hotkey("win","down")
    
def mov_rgt():
    speak("moving right by a character")
    pyautogui.hotkey("right")

def mov_lftWord():
    speak("moving left by a word")
    pyautogui.hotkey("ctrl","left")
    
def mov_rgtWord():
    speak("moving right by a word")
    pyautogui.hotkey("ctrl","right")
    
def undo():
    speak("undoing")
    pyautogui.hotkey("ctrl","z")
    
def undo():
    speak("undoing")
    pyautogui.hotkey("ctrl","z")
    
def redo():
    speak("redoing")
    pyautogui.hotkey("ctrl","y")
    
  
def scroll_up():
    """
    scroll up 10 "clicks"
    """
    speak("Scrolling up")
    pyautogui.scroll(50)
    
def scroll_down():
    """
    scroll down 10 "clicks"
    """
    speak("Scrolling down")
    pyautogui.scroll(-50)
    
def open_window(url):
    """
    Open a new window with the specified URL.
    """
    speak("Opening new window")
    pyautogui.hotkey("ctrl", "shift", "n")
    pyautogui.typewrite(url + "\n")
        
def close_window():
    """
    Close the current window.
    """
    speak("Closing window")
    pyautogui.hotkey("alt", "f4")


def change_window():
    """
    Close the current window.
    """
    speak("Changing window")
    pyautogui.hotkey("alt", "tab")


def open_tab():
    """
    Open a new tab in the IDE
    """
    speak("Opening new tab")
    pyautogui.hotkey("ctrl", "n")


def close_tab():
    """
    Close the current tab in a web browser.
    """
    speak("Closing tab")
    pyautogui.hotkey("ctrl", "w")


def change_tab():
    """
    Close the current window.
    """
    speak("Changing window")
    pyautogui.hotkey("ctrl", "tab")


def minimize_window():
    """
    Minimize the current window.
    """
    speak("Minimizing window")
    pyautogui.hotkey("win", "m")


def maximize_window():
    """
    Maximize the current window.
    """
    speak("Maximizing window")
    pyautogui.hotkey("win", "up")


def demaximize_window():
    """
    Maximize the current window.
    """
    speak("Demaximizing window")
    pyautogui.hotkey("win", "down")


def inc_vol():
    """
    Incearse the volume.
    """
    speak("Increasing the volume")
    pyautogui.hotkey("volumeup")


def dec_vol():
    """
    Decrease the volume.
    """
    speak("Decreasing the volume")
    pyautogui.hotkey("volumedown")


def mute():
    """
    Mute the volume.
    """
    speak("Muting the volume")
    pyautogui.hotkey("volumemute")
    

def prev_trck():
    """
    prvious track
    """
    speak("playing previous track")
    pyautogui.hotkey("prevtrack")

def nxt_trck():
    """
    next track
    """
    speak("playing next track")
    pyautogui.hotkey("nexttrack")
    
def pause():
    """
    pause
    """
    speak("pausing")
    pyautogui.hotkey("pause")
    
def next_line():
    speak(" entering next line")
    pyautogui.keyDown("ctrl")
    pyautogui.hotkey("enter")
    pyautogui.keyUp("ctrl")    
    
    
def enter():
    speak("pressing enter")
    pyautogui.hotkey("enter")

def backspace():
    speak(" clearing a character")
    pyautogui.hotkey("backspace")

def delete():
    speak(" deleting a character")
    pyautogui.hotkey("delete")

def save_file():
    speak("saving file")
    pyautogui.hotkey("ctrl","s")

def open_file():
    speak("opening file")
    pyautogui.hotkey("ctrl","o")

def capslock():
    speak(" capslock ")
    pyautogui.hotkey("capslock")

def page_up():
    speak(" scrolling up ")
    pyautogui.hotkey("pgup")
    
def page_down():
    speak("scrolling down")
    pyautogui.hotkey("pgdn")

def space():
    speak(" spacing ")
    pyautogui.hotkey("space")

def tab():
    speak("pressing tab")
    pyautogui.hotkey("\t")

    
def hold_alt():
    speak("holding alt")
    pyautogui.keyDown("alt")
    
def release_alt():
    speak("releasing alt")
    pyautogui.keyUp("alt")
    
def select_area():
    speak("selecting area")
    pyautogui.keyDown("shift")
    left_click()
    pyautogui.keyUp("shift")
    speak("area selected")
    
def entire_area():
    speak("selecting area")
    pyautogui.hotkey("ctrl","a")
    speak("area selected")

def select_line():
    speak("selecting line")
    pyautogui.click(clicks=3 ,button='left')

def select_word():
    speak("selecting word")
    pyautogui.click(clicks=2, button='left')
    
    
def convert_comnts():
    speak("converted to comments")
    pyautogui.keyDown("ctrl")
    pyautogui.hotkey("/")
    pyautogui.keyUp("ctrl")
    
def print_screen():
    speak("taking screen shot")
    pyautogui.hotkey("win","printscreen")
    
def new_browsTab():
    speak("Opening new tab in browser")
    pyautogui.hotkey("ctrl","t")    
    
def love():
    speak("it's Lovely")
    speak("I love you three thousand")
    
def comnts():
    speak("initiating line comment")
    pyautogui.typewrite("//")
    
def rename():
    speak("select object to rename")
    pyautogui.hotkey("f2")
    
def chng_allOcuur():
    speak("changing all occurances")
    pyautogui.hotkey("ctrl", "f2")
    
def clr_pword():
    speak("clearing previous word")
    pyautogui.hotkey("ctrl", "backspace") 
    
def clr_nxtword():
    speak("clearing next word")
    pyautogui.hotkey("ctrl", "shift","right","backspace") 
    
def clr_line():
    speak("clearing entire line")
    pyautogui.click(clicks=3)
    pyautogui.hotkey("backspace")
    
def spl_setings():
    speak("opening special settings")
    pyautogui.hotkey("win","a")
    

def win_left():
    speak("moving window to left")
    pyautogui.hotkey("win","left")
    

def win_rgt():
    speak("moving window to right")
    pyautogui.hotkey("win","right")
    

def win_up():
    speak("moving window to up")
    pyautogui.hotkey("win","up")
    

def win_dwn():
    speak("moving window to down")
    pyautogui.hotkey("win","down")

def stp_exectn():
    speak("execution stopped")
    pyautogui.hotkey("ctrl","c")


    
def copy():
    speak("copying")
    pyautogui.hotkey("ctrl","c")
    
def cut():
    speak("cutting")
    pyautogui.hotkey("ctrl","x")
    
def paste():
    speak("pasting")
    pyautogui.hotkey("ctrl","v")