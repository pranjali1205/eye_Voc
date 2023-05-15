#Gets speech recognition engine, Speak() function,
from Engine import *
from Engine import recognizer
import re
       
def dictate_mode():
    """
    Type text based on spoken words, until the command "exit dictation" is given.
    """ 
    speak("Diactate to me")
    text = ""
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
    
        try:
            # Use Google Speech Recognition to convert audio to text
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            if re.search("exit dictation", command.lower()) or re.search("exit", command.lower()):
                speak("exited dictation mode")
                break
            else:
                text += command
                pyautogui.typewrite(command + " ")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
