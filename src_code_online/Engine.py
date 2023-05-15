import pyttsx3
import pyautogui
import speech_recognition as sr
import wmi

pyautogui.FAILSAFE = False


engine = pyttsx3.init()



# Set the voice type
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Choose the first voice in the list

# Adjust the pitch, rate, volume, and voice quality
engine.setProperty('pitch', 150)  # Increase the pitch (higher voice)
engine.setProperty('rate', 200)  # Increase the rate (faster speech)
engine.setProperty('volume', 1)  # Decrease the volume (quieter voice)
engine.setProperty('voice', voices[1].id)  # Choose a different voice type or variant
engine.setProperty('voice', 'english_rp+f3')  # Choose a specific voice variant

recognizer = sr.Recognizer()  

from AppOpener import open, close

def speak(text):
    """
    Use text-to-speech to speak the specified text.
    """
    engine.say(text)
    engine.runAndWait()
