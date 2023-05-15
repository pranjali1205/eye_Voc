## eye_Voc
This innovative tool is designed to empower individuals whomay have limited hand mobility by providing them with a wayto code using only their voice. With this tool, users can alsohandle a computer completely using just voice commands.

# Understanding the file structure
There are total of 5 folders :-
1. Enable_Viacam : This is folder for eye tracker that we are using. Once you open this folder, scroll down you will find a file named eviacam.exe. Double tap on it                    to open.
                   If you find it difficult to open evicam this way, you also download it from this link-> https://eviacam.crea-si.com/index.php
                   
2. EyeVoc_offline_Application :  This is the folder for our offline application. We made this so that even the people who don't have python installed in their                           systems can use our application.
                    To use the application, open the folder.Scroll down, you will find EyeVoc_offline.exe file( one with icon).Doble tap to open it.
                    
3. EyeVoc_offline_Application : This is the folder for our online application.
                     To use the application, open the folder.Scroll down, you will find EyeVoc_offline.exe file( one with icon).Doble tap to open it.
                     
4. src_code_offline : This contains entire source code of offline mode. In oder to run the application through source code, make sure you have python installed in                        your systems. Also install the dependencies mentioned below (under dependencies headline).
                     Once everything is setup, run the Main.py program.
                     
 5. src_code_offline : This contains entire source code of online mode. In oder to run the application through source code, make sure you have python installed in                          your systems. Also install the dependencies mentioned below (under dependencies headline).
                       Once everything is setup, run the Main.py program
                       
  6. EyeVoc.pptx : This contains our prsentation slides.
  
  7. Prgram_flow.png : This picture shows how the control flows between all the files of source code.
  
  8. Team3 Report.pdf : This is the report for our pdf.
  
  9. features.png :  This pic shows all the features we have implemented in our tool.
  
  10.intructions.pdf : Refer to this file to know the intructions to use application in detail.
   Later we have demo videos.
   
# Dependencies that neeeds to be installed
pyttsx3 : $ pip install pyttsx3 </br>
pyautogui : $ pip install pyautogui
speech_recognition : $ pip install SpeechRecognition
wmi : $ pip install wmi
os : $ import os
re : $ pip install re
AppOpener : $ pip install AppOpener
Pythonping : $ pip install pythonping

one additional library for offline version -
VOSK : $ pip install vosk
