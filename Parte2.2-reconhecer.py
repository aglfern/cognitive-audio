# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 02:21:12 2021

Isso aqui também usa o espeak

@author: aglfen@gmail.com
"""

pip install pyttsx3 

# pip install pyttsx3
# Collecting pyttsx3
#   Using cached pyttsx3-2.90-py3-none-any.whl (39 kB)
# Collecting pypiwin32
#   Using cached pypiwin32-223-py3-none-any.whl (1.7 kB)
# Collecting comtypes
#   Downloading comtypes-1.1.10.tar.gz (145 kB)
# Requirement already satisfied: pywin32 in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from pyttsx3) (228)
# Building wheels for collected packages: comtypes
#   Building wheel for comtypes (setup.py): started
#   Building wheel for comtypes (setup.py): finished with status 'done'
#   Created wheel for comtypes: filename=comtypes-1.1.10-py3-none-any.whl size=165856 sha256=d4e511d02215ee188bc11cb2222362f0cd91f522816f7e8da350eb0fd3e4c317
#   Stored in directory: c:\users\aglfe\appdata\local\pip\cache\wheels\c7\3e\26\faa526d811797151de13e75f09b9e6ebab418a7d482d12142e
# Successfully built comtypes
# Installing collected packages: pypiwin32, comtypes, pyttsx3
# Successfully installed comtypes-1.1.10 pypiwin32-223 pyttsx3-2.90
# Note: you may need to restart the kernel to use updated packages.

import pyttsx3

welcomeText = "Hey dude! Lets see if the recognizer does a good work!"
fileName = "sx3-generated.mp3"

mySint = pyttsx3.init()
voices = mySint.getProperty('voices')
mySint.setProperty('voice', voices[1].id) # English
mySint.setProperty('rate',150)
mySint.say(welcomeText)
mySint.save_to_file(welcomeText, fileName)
mySint.runAndWait()

import speech_recognition as sr

fileName = "speech-to-text_data_audio1.wav"

r = sr.Recognizer()
with sr.AudioFile(fileName) as source:
    audio = r.record(source)
    print("Sphinx: [" + recognizer.recognize_sphinx(audio) + "]")
    print("Google: [" + recognizer.recognize_google(audio) + "]")


# LiveSpeech test
# It's an iterator class for continuous recognition or keyword search from a microphone.
# https://pypi.org/project/pocketsphinx/

from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
    print("You said: [" + str(phrase) +"]")

# search not clear 
speech = LiveSpeech(lm=False, keyphrase='forward', kws_threshold=1e-20)
for phrase in speech:
    print(phrase.segments(detailed=True))
    


