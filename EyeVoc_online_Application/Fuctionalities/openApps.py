#Gets speech recognition engine, Speak() function,
from Engine import *
import os

# Definig open and close functions for some apps



  #  Notepad
def open_notepad():    
    speak("opening notepad")
    open("notepad")

def close_notepad():
    speak("closing notepad")
    close("notepad.exe")

def open_terminal():
    speak("opening terminal")
    open("cmd.exe")

def close_terminal():
    speak("closing terminal")
    close("cmd.exe")
    
    # Google
def open_google():    
    speak("opening google")
    open("google chrome")

def close_google():
    speak("closing google")
    close("google chrome.exe")

    # Whatsapp
def open_watsap():    
    speak("opening Whatsapp")
    open("whatsapp")

def close_watsap():
    speak("closing Whatsapp")
    close("whatsapp.exe")
    
def open_osk():    
    speak("opening on screen keyboard")
    open("on-screen keyboard")


def close_osk():    
    speak("opening on screen keyboard")
    close("osk.exe")

  # Mouse Cam 
def open_eviacam(): 
    
    # Refraining This Particular app from opening twice
        
    ti = 0
    name = 'eviacam.exe'
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name == name:   
            print("mouse cam already running")
            speak("mouse cam already running")
            ti = 1
            return
 
    if ti == 0:
        print("opening mouse cam")
        speak("opening mouse cam")
        os.startfile(r'C:\\Users\\AVINA\\OneDrive\\Desktop\\EyeVoc\\Enable_Viacam\\bin\eviacam.exe')

def close_eviacam():  
    speak("closing eviacam")  
    # close("eviacam.exe")
    name = 'eviacam.exe'
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name == name:   
            process.Terminate()
            break
 