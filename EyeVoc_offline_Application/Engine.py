import pyttsx3
import pyautogui
import speech_recognition as sr
import wmi
from vosk import Model, KaldiRecognizer
import json
import pyaudio

# model = Model("C:\\Users\\AVINA\\OneDrive\\Desktop\\EyeVoc\\src_code_offline\\vosk-model-small-en-in-0.4")
model = Model("C:\\Users\\AVINA\\OneDrive\\Desktop\\EyeVoc\\src_code_offline\\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model,16000)
mic = pyaudio.PyAudio()
stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16,input=True, frames_per_buffer=4096)
stream.start_stream()




pyautogui.FAILSAFE = False
engine = pyttsx3.init()

# Set the voice type
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # Choose the first voice in the list

# Adjust the pitch, rate, volume, and voice quality
engine.setProperty('pitch', 150)  # Increase the pitch (higher voice)
engine.setProperty('rate', 200)  # Increase the rate (faster speech)
engine.setProperty('volume', 1)  # Decrease the volume (quieter voice)
engine.setProperty('voice', voices[1].id)  # Choose a different voice type or variant
engine.setProperty('voice', 'english_rp+f3')  # Choose a specific voice variant





    
from AppOpener import open, close

def speak(text):
    """
    Use text-to-speech to speak the specified text.
    """
    engine.say(text)
    engine.runAndWait()
