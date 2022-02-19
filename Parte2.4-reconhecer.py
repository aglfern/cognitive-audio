# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 00:39:52 2021

@author: aglfen@gmail.com

Important Links
# https://docs.microsoft.com/pt-br/azure/cognitive-services/speech-service/language-support
# https://github.com/Uberi/speech_recognition

# alternativa com o sdk azure
https://docs.microsoft.com/pt-br/azure/cognitive-services/speech-service/get-started-speech-to-text?tabs=windowsinstall&pivots=programming-language-python

"""
import speech_recognition as SpeechRec

for index, name in enumerate(SpeechRec.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

recognizer = SpeechRec.Recognizer()

# Azure
AZURE_SPEECH_KEY = "{coloque sua chave aqui}" 
AZURE_LOCATION = "brazilsouth"


# Não se esqueça de verificar se o microfone escolhido é o correto!
inputPhone = 0

with SpeechRec.Microphone(inputPhone) as inputVoice:
    print('Olá, diga algo em português:')
    recognizer.adjust_for_ambient_noise(inputVoice,duration=2)
    responseAudio = recognizer.listen(inputVoice)
    print('Iniciando reconhecimento...')
    try:
        rec = recognizer.recognize_azure(responseAudio, key=AZURE_SPEECH_KEY, location=AZURE_LOCATION, language='pt-BR')
    except SpeechRec.UnknownValueError:
        print("Microsoft Azure Speech could not understand audio")
    except SpeechRec.RequestError as e:
        print("Could not request results from Microsoft Azure Speech service; {0}".format(e))    
    
    print("Azure: [" + rec + "]")

    
    
# In a loop
with SpeechRec.Microphone(inputPhone) as inputVoice:
    recognizer.adjust_for_ambient_noise(inputVoice,duration=1)
    print('Olá, diga algo em português:')
    while True:
        print('----- outra vez (diga "fim" para encerrar):')
        responseAudio = recognizer.listen(inputVoice)
        print('Iniciando reconhecimento...')
        try:
            rec = recognizer.recognize_azure(responseAudio, key=AZURE_SPEECH_KEY, location=AZURE_LOCATION, language='pt-BR')
        except SpeechRec.UnknownValueError:
            print("Microsoft Azure Speech could not understand audio")
        except SpeechRec.RequestError as e:
            print("Could not request results from Microsoft Azure Speech service; {0}".format(e))    
    
        print("Azure: [" + rec + "]")
    
        if(rec=="fim" or rec=="Fim" or rec=="Fim."): break

# end loop


