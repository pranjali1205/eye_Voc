## eye_Voc
This innovative tool is designed to empower individuals who may have limited hand mobility by providing them with a wayto code using only their voice. With this tool, users can also handle a computer completely using just voice commands.</br>
Developers can also use this for hands free coding. Presently our tool provides coding in java, python, c and c++.</br>
( if any word doesn't get recognised properly, you can always open on screen keybord using comand "open keybord", type the word you require ,and later use "close keyboard" to close it )</br></br>

# Understanding the file structure
There are total of 5 folders and 7 files:-
1. Enable_Viacam : This is folder for eye tracker that we are using. Once you open this folder, scroll down you will find a file named eviacam.exe. Double tap on                     it to open.</br>
                   If you find it difficult to open evicam this way, you also download it from this link-> https://eviacam.crea-si.com/index.php
  </br></br>                 
2. EyeVoc_offline_Application :  This is the folder for our offline application. We made this so that even the people who don't have python installed in their                           systems can use our application.</br>
                    To use the application, open the folder.Scroll down, you will find EyeVoc_offline.exe file( one with icon).Doble tap to open it.
  </br></br>                  
3. EyeVoc_online_Application : This is the folder for our online application.</br>
                     To use the application, open the folder.Scroll down, you will find EyeVoc_offline.exe file( one with icon).Doble tap to open it.
  </br></br>                   
4. src_code_offline : This contains entire source code of offline mode. In oder to run the application through source code, make sure you have python installed in                     your systems. Also install the dependencies mentioned below (under dependencies headline) and make the path changes as mention below(under Changes needed for running the source code for offline mode headline).</br>
                     Once everything is setup, run the Main.py program.
    </br></br>                 
 5. src_code_online : This contains entire source code of online mode. In oder to run the application through source code, make sure you have python installed in                          your systems. Also install the dependencies mentioned below (under dependencies headline) and make the path changes as mention below(under Changes needed for running the source code for offline mode headline).</br>
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
  10. intructions.pdf : Refer to this file to know the intructions to use application in detail.
  </br></br>
  11. offline_demo.webm and online_mode_demo.mp4 : These are demo videos for our offline and online modedl respectively.
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
# Changes needed for running the source code
● In <b>Engine.py</b> file(" of offline version")</br>
At line no. 10, update the <b> path of vosk-model-samll-en-in-0.4</b> folder according to your local system. 
</br></br>
●  In <b>OpenApps.py</b> (Make this change in both versions).</br>
At line no. 71, change the <b> path of eviacam.exe file</b>. </br>
(You can get the path of eviacam by opening Enable_viacam folder, then open bin
folder, then look for evicam.exe file.) 
</br> or ( if you installed eviacam through link, udpate the path according to where you have downloaded it.)
</br></br></br>

# Pros and cons of online and offline versions
</br> <b>Online :</b></br>
- this version has better accuracy, as it is trained on huge collection of words.
- However, it may take a bit longer to respond since it relies on Google's speech recognition technology to recognize the words. To verify each word, the system needs to connect to a server, and the recognized word is then sent back as a response.As a result the response speed depends on the internet speed. 
</br></br>
</br> <b>Offline :</b></br>
(Since we can't access internet everywhere, we thought of bringing a offline version which can be used anywhere without worrying about the net connection)
- This version has a very quick response time.
- However, it may not always predict the word correctly, as it is only trained on commonly used words.Because of which many morden words or the words which we do not use in day to day life might not be present in the data. For eg :- "Whatsapp" isn't there in the collection of words. But in oder to use it we added alternatives which were getting recognised when tried to say whatsapp.So we added "what's up" as an ulternative to that.</br> 
- We have done the same practise for all other words to enhance the accuracy of our tool. 
</br></br></br>

# Link to all the voice commands
</br> https://docs.google.com/document/d/19MFWQ_5MpEi7aJvZREQXF3sdn0hBGh0vE0YTHDRHvIw/edit
</br></br></br>
<b>NOTE :</b> We have developed this tool entirely on Windows platform. So the users using other os might face some dependencies problem. Hence we suggest using windows os to test or exprience functionalities of our tool.

