# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 01:05:07 2021

IMPORTANTE: Este código roda no python 3.6 apenas


@author: aglfen@gmail.com
"""
pip install pyaudio

# pip install pyaudio
# Collecting pyaudio
#   Downloading PyAudio-0.2.11-cp36-cp36m-win_amd64.whl (52 kB)
# Installing collected packages: pyaudio
# Successfully installed pyaudio-0.2.11
# Note: you may need to restart the kernel to use updated packages.

pip install SpeechRecognition

# pip install SpeechRecognition
# Collecting SpeechRecognition
#   Downloading SpeechRecognition-3.8.1-py2.py3-none-any.whl (32.8 MB)
# Installing collected packages: SpeechRecognition
# Successfully installed SpeechRecognition-3.8.1
# Note: you may need to restart the kernel to use updated packages.

pip install pocketSphinx

# pip install pocketSphinx
# Collecting pocketSphinx
#   Downloading pocketsphinx-0.1.15-cp36-cp36m-win_amd64.whl (29.1 MB)
# Installing collected packages: pocketSphinx
# Successfully installed pocketSphinx-0.1.15
# Note: you may need to restart the kernel to use updated packages.

# Location
# C:\Users\aglfe\.conda\envs\python3.6\Lib\site-packages\pocketsphinx


import speech_recognition as SpeechRec

SpeechRec.Microphone.list_working_microphones()

for index, name in enumerate(SpeechRec.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

recognizer = SpeechRec.Recognizer()

phoneId = 0

# Sphinx
with SpeechRec.Microphone(phoneId) as inputVoice:
    print('Hi, please say something in English')
    recognizer.adjust_for_ambient_noise(inputVoice,duration=2)
    responseAudio = recognizer.listen(inputVoice)
    print(recognizer.recognize_sphinx(responseAudio))
    
# Google
with SpeechRec.Microphone(phoneId) as inputVoice:
    print('Hi, please say something in English (and keep saying)')
    recognizer.adjust_for_ambient_noise(inputVoice,duration=2)
    responseAudio = recognizer.listen(inputVoice)
    print(recognizer.recognize_google(responseAudio))


# Both, in a loop
with SpeechRec.Microphone(phoneId) as inputVoice:
    recognizer.adjust_for_ambient_noise(inputVoice,duration=1)
    print('Hi, please say something in English (and keep saying)')
    recon = ''
    while recon != 'stop' and recon !='Stop.':
        print('...Go on...')
        responseAudio = recognizer.listen(inputVoice)
        
        # recognize speech using Sphinx
        try:
            print("Sphinx: [" + recognizer.recognize_sphinx(responseAudio) + "]")
        except SpeechRec.UnknownValueError:
            print("Sphinx could not understand audio")
        except SpeechRec.RequestError as e:
            print("Sphinx error; {0}".format(e))
        
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            recon = recognizer.recognize_google(responseAudio)
            print("Google: [" + recon + "]")
        except SpeechRec.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except SpeechRec.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# if(rec=="fim" or rec=="Fim" or rec=="Fim."): break
            
# end loop