# -*- coding: utf-8 -*-
"""

PARTE 1: SINTETIZADOR DE VOZ - Com texto no código

Created on Thu Dec 16 01:49:36 2021

Pre-requisitos
 - Instalação do ESPEAK
 
Libs
 - os
 - pyttsx3
 - datetime

# documentação da API
# https://pyttsx3.readthedocs.io/en/latest/engine.html#pyttsx3.voice.Voice

@author: aglfen@gmail.com
"""


# biblioteca para executar comandos do sistema operacional
import os

# testando o funcionamento e se o path do espeak está configurado corretamente
# dentro do command prompt, verifique o path
os.system('cmd')

# agora, testando chamar o programa com uma frase
os.system('espeak "Hello! Let''s code! Won''t you?"')

# incluindo parâmetros, idioma e velocidade
os.system('espeak -v pt -s 180 "Olá! Vamos programar juntos?"')


## USANDO A MESMA COISA MAS AGORA USANDO A BIBLIOTECA pyttsx3

# instalar a biblioteca - importante reiniciar o kernel depois
# pode ser necessário instalar pypiwin32, se der erro na instalação
pip install pyttsx3 

import pyttsx3

mySint = pyttsx3.init()

mySint.say("Ei! Tudo bem com você?")

mySint.runAndWait()



voices = mySint.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
    
mySint.setProperty('voice', voices[1].id)
mySint.say("Hey dude, how are you doing?")
mySint.runAndWait()

mySint.setProperty('rate',250)
mySint.say("Hey dude, how are you doing?")
mySint.runAndWait()

mySint.setProperty('volume',0.1)
mySint.say("Hey dude, how are you doing?")
mySint.runAndWait()

mySint.setProperty('rate',120)
mySint.setProperty('volume',0.8)
mySint.say("Hey dude, how are you doing?")
mySint.runAndWait()



import pyttsx3
from datetime import datetime

    
userName = "Alexandre"
currentHour = datetime.now().hour
currentMin = datetime.now().minute
currentDay = datetime.now().day

welcomeText = "Bom dia " + str(userName) + ", como você está hoje? Neste momento, são " + str(currentHour) + " horas e " + str(currentMin) + " minutos do dia " + str(currentDay) + "."

mySint = pyttsx3.init() # no windows vai pegar o sapi5
# mySint = pyttsx3.init("sapi5")
# mySint = pyttsx3.init("espeak") 
# não fez diferença quando tentei forçar - dúvida, precisava do espeak?


voices = mySint.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
    


mySint.setProperty('voice', voices[0].id)
mySint.setProperty('rate',180)
mySint.say(welcomeText)
mySint.runAndWait()

