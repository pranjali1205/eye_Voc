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
        data = stream.read(4096)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            command = result["text"]
            print("You said: " + command)
            if re.search("exit dictation", command.lower()) or re.search("exit", command.lower()):
                speak("exited dictation mode")
                break
            else:
                text += command
                pyautogui.typewrite(command + " ")
 
