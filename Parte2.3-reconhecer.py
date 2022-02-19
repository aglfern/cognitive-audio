# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:46:57 2021

@author: aglfen@gmail.com
"""
import speech_recognition as SpeechRec

# SpeechRec.Microphone.list_working_microphones()

for index, name in enumerate(SpeechRec.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

recognizer = SpeechRec.Recognizer()

# Google
with SpeechRec.Microphone(1) as inputVoice:
    recognizer.adjust_for_ambient_noise(inputVoice,duration=1)
    print('Olá, diga algo em português:')
    responseAudio = recognizer.listen(inputVoice)
    print(recognizer.recognize_google(responseAudio, language='pt'))

# In a loop
with SpeechRec.Microphone(1) as inputVoice:
    print('Olá, diga algo em português:')
    while True:
        print('...Go on...')
#        recognizer.adjust_for_ambient_noise(inputVoice,duration=1)
        responseAudio = recognizer.listen(inputVoice)
        print("Google: [" + recognizer.recognize_google(responseAudio, language='pt') + "]")

# end loop


# In a loop
with SpeechRec.Microphone(1) as inputVoice:
    recognizer.adjust_for_ambient_noise(inputVoice,duration=1)
    print('Olá, diga algo em português:')
    while True:
        print('...Go on...')
        responseAudio = recognizer.listen(inputVoice)
        print("Google: [" + recognizer.recognize_google(responseAudio, language='pt') + "]")

# end loop


