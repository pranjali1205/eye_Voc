## eye_Voc
This innovative tool is designed to empower individuals who may have limited hand mobility by providing them with a wayto code using only their voice. With this tool, users can also handle a computer completely using just voice commands.</br>
Developers can also use this for hands free coding. Presently our tool provides coding in java, python, c and c++.</br>
( if any word doesn't get recognised properly, you can open on screen keybord using comand "open kebord", type the word you require and later use "close keyboaed" to close it )</br></br>

# Understanding the file structure
There are total of 5 folders :-
1. Enable_Viacam : This is folder for eye tracker that we are using. Once you open this folder, scroll down you will find a file named eviacam.exe. Double tap on it                    to open.
                   If you find it difficult to open evicam this way, you also download it from this link-> https://eviacam.crea-si.com/index.php
  </br></br>                 
2. EyeVoc_offline_Application :  This is the folder for our offline application. We made this so that even the people who don't have python installed in their                           systems can use our application.
                    To use the application, open the folder.Scroll down, you will find EyeVoc_offline.exe file( one with icon).Doble tap to open it.
  </br></br>                  
3. EyeVoc_online_Application : This is the folder for our online application.
                     To use the application, open the folder.Scroll down, you will find EyeVoc_offline.exe file( one with icon).Doble tap to open it.
  </br></br>                   
4. src_code_offline : This contains entire source code of offline mode. In oder to run the application through source code, make sure you have python installed in                        your systems. Also install the dependencies mentioned below (under dependencies headline).
                     Once everything is setup, run the Main.py program.
    </br></br>                 
 5. src_code_online : This contains entire source code of online mode. In oder to run the application through source code, make sure you have python installed in                          your systems. Also install the dependencies mentioned below (under dependencies headline).
                       Once everything is setup, run the Main.py program
     </br></br>                  
  6. EyeVoc.pptx : This contains our prsentation slides.
  </br></br>
  7. Prgram_flow.png : This picture shows how the control flows between all the files of source code.
  </br></br>
  8. Team3 Report.pdf : This is the report for our pdf.
  </br></br>
  9. features.png :  This pic shows all the features we have implemented in our tool.
  </br></br>
  10.intructions.pdf : Refer to this file to know the intructions to use application in detail.
   Later we have demo videos.
   </br></br></br>
# Dependencies that neeeds to be installed
pyttsx3 : $ pip install pyttsx3 </br>
pyautogui : $ pip install pyautogui </br>
speech_recognition : $ pip install SpeechRecognition </br>
wmi : $ pip install wmi </br>
os : $ import os </br>
re : $ pip install re </br>
AppOpener : $ pip install AppOpener </br>
Pythonping : $ pip install pythonping </br>
</br>
one additional library for offline version -</br>
VOSK : $ pip install vosk
</br></br></br>

# Link to all the voice commands
</br> https://docs.google.com/document/d/19MFWQ_5MpEi7aJvZREQXF3sdn0hBGh0vE0YTHDRHvIw/edit
</br></br></br>
<b>NOTE :</b> We have developed this tool entirely on Windows platform. So the users using other os might face some dependencies problem. Hence we suggest using windows os to test or exprience functionalities of our tool.

