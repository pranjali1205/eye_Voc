#Gets speech recognition engine, Speak() function,
from Engine import *



# Following are some of the symblos
 
  
def exclaim():
    speak("Exclamtion mark")
    pyautogui.hotkey("!")
    
def single_quotes():
    speak("Single quotes ")
    pyautogui.typewrite("''")
    
def double_quotes():
    speak("Double quotes")
    pyautogui.typewrite(' " " ')
    
def hash():
    pyautogui.hotkey("#")
    speak("hash written")
    
def at_rate():
    speak("At the rate")
    pyautogui.hotkey("@")
    
def dollar():
    speak("dollar")
    pyautogui.hotkey("$")
    
def Amper():
    speak("Ampersand")
    pyautogui.hotkey("&")
    
def percent():
    speak("Percent")
    pyautogui.hotkey("%")
    
def open_brac():
    pyautogui.hotkey("(")
    speak("bracket opened")
    
def close_brac():
    pyautogui.hotkey(")")
    speak("bracket closed")
    
def open_flowerbrac():
    pyautogui.hotkey("{")
    speak("flower bracket opened")
    
def close_flowerbrac():
    pyautogui.hotkey("}")
    speak("flower bracket closed")
    
def open_Rectbrac():
    pyautogui.hotkey("[")
    speak("Rectangle bracket opened")
    
def close_Rectbrac():
    pyautogui.hotkey("]")
    speak("Rectangle bracket closed")
    
def asterisk():
    speak("Asterisk")
    pyautogui.hotkey("*")

def back_tick():
    speak("back tick")
    pyautogui.typewrite("`")

def similar_to():
    speak("is similar to")
    pyautogui.typewrite("~")
    
def modulus():
    speak("modulus")
    pyautogui.hotkey("%")
    
def exponent():
    speak("exponent")
    pyautogui.typewrite("**")
    
def floor_div():
    speak("floor division")
    pyautogui.typewrite("//")
    
def minus():
    speak("minus")
    pyautogui.hotkey("-")
    
def plus():
    speak("plus")
    pyautogui.hotkey("+")
    
def divide():
    speak("divide")
    pyautogui.hotkey("/")
    
def multiply():
    speak("mutiplying with")
    pyautogui.hotkey("*")
    
def coma():
    speak("coma")
    pyautogui.hotkey(",")
    
def equal_to():
    speak("is equal to")
    pyautogui.hotkey("=")
    
def check_eql():
    speak("check whether equal to")
    pyautogui.typewrite("==")
    
def nt_eq():
    speak("not equal to")
    pyautogui.typewrite("!=")
    
def gt_eq():
    speak("greater than or equal to")
    pyautogui.typewrite(">=")
    
def lt_eq():
    speak("is less than or equal to")
    pyautogui.typewrite("<=")
    
def gt():
    speak("is greater than")
    pyautogui.hotkey(">")
    
def lt():
    speak("is less than")
    pyautogui.hotkey("<")
    
def full_stop():
    speak("full stop")
    pyautogui.hotkey(".")
    
def f_slash():
    speak("forward slash")
    pyautogui.hotkey("/")
    
def b_slash():
    speak("backward slash")
    pyautogui.hotkey("\\")
    
def colon():
    speak("colon")
    pyautogui.hotkey(":")
    
def semi_colon():
    speak("semi colon")
    pyautogui.hotkey(";")
    
def under_score():
    speak("under score")
    pyautogui.hotkey("_")
    
def one():
    speak("number one")
    pyautogui.hotkey("1")
    
def two():
    speak("number two")
    pyautogui.hotkey("2")
    
def three():
    speak("number")
    pyautogui.hotkey("")
    
def four():
    speak("number four")
    pyautogui.hotkey("4")
    
def five():
    speak("number five")
    pyautogui.hotkey("5")
    
def six():
    speak("number six")
    pyautogui.hotkey("6")
    
def seven():
    speak("number seven")
    pyautogui.hotkey("7")
    
def eight():
    speak("number eight")
    pyautogui.hotkey("8")
    
def nine():
    speak("number nine")
    pyautogui.hotkey("9")
    
def zero():
    speak("number zero")
    pyautogui.hotkey("0")
    