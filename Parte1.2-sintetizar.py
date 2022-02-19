# -*- coding: utf-8 -*-
"""

PARTE 2 - SINTETIZADOR DE VOZ - GOOGLE + ARQUIVOS DE ÁUDIO

Created on Thu Dec 16 01:55:57 2021

Libs
 - os
 - gtts
 - playsound
 - pygame (opt)
 
 
 https://gtts.readthedocs.io/en/latest/

@author: aglfen@gmail.com
"""


pip install gTTS

#Collecting gTTS
#  Downloading https://files.pythonhosted.org/packages/e4/9e/fe139150719281309c6e52a799e86d7d8d19f6f2593b340e3693f6ef2c77/gTTS-2.2.3-py3-none-any.whl
#Requirement already satisfied: six in c:\programdata\anaconda3\lib\site-packages (from gTTS) (1.12.0)
#Requirement already satisfied: click in c:\programdata\anaconda3\lib\site-packages (from gTTS) (7.0)
#Requirement already satisfied: requests in c:\programdata\anaconda3\lib\site-packages (from gTTS) (2.22.0)
#Requirement already satisfied: chardet<3.1.0,>=3.0.2 in c:\programdata\anaconda3\lib\site-packages (from requests->gTTS) (3.0.4)
#Requirement already satisfied: idna<2.9,>=2.5 in c:\programdata\anaconda3\lib\site-packages (from requests->gTTS) (2.8)
#Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\programdata\anaconda3\lib\site-packages (from requests->gTTS) (1.24.2)
#Requirement already satisfied: certifi>=2017.4.17 in c:\programdata\anaconda3\lib\site-packages (from requests->gTTS) (2019.9.11)
#Installing collected packages: gTTS
#Successfully installed gTTS-2.2.3
#Note: you may need to restart the kernel to use updated packages.

# python 3.6
# Collecting gTTS
#   Using cached gTTS-2.2.3-py3-none-any.whl (25 kB)
# Requirement already satisfied: six in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from gTTS) (1.16.0)
# Requirement already satisfied: click in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from gTTS) (8.0.3)
# Requirement already satisfied: requests in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from gTTS) (2.26.0)
# Requirement already satisfied: colorama in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from click->gTTS) (0.4.4)
# Requirement already satisfied: importlib-metadata in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from click->gTTS) (4.8.1)
# Requirement already satisfied: typing-extensions>=3.6.4 in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from importlib-metadata->click->gTTS) (3.10.0.2)
# Requirement already satisfied: zipp>=0.5 in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from importlib-metadata->click->gTTS) (3.6.0)
# Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from requests->gTTS) (1.26.7)
# Requirement already satisfied: idna<4,>=2.5 in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from requests->gTTS) (3.3)
# Requirement already satisfied: certifi>=2017.4.17 in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from requests->gTTS) (2021.5.30)
# Requirement already satisfied: charset-normalizer~=2.0.0 in c:\users\aglfe\.conda\envs\python3.6\lib\site-packages (from requests->gTTS) (2.0.4)
# Installing collected packages: gTTS
# Successfully installed gTTS-2.2.3
# Note: you may need to restart the kernel to use updated packages.

pip install playsound

# python 3.6
# Collecting playsound
#   Downloading playsound-1.3.0.tar.gz (7.7 kB)
# Building wheels for collected packages: playsound
#   Building wheel for playsound (setup.py): started
#   Building wheel for playsound (setup.py): finished with status 'done'
#   Created wheel for playsound: filename=playsound-1.3.0-py3-none-any.whl size=7037 sha256=2adaaf89d3a313e549e9099ef8a7635756436231053a3037be246c1cb02388b3
#   Stored in directory: c:\users\aglfe\appdata\local\pip\cache\wheels\2d\2e\fd\10abd9de9e1b013dfa324e4f93bcce680b5e856ad5b0149051
# Successfully built playsound
# Installing collected packages: playsound
# Successfully installed playsound-1.3.0
# Note: you may need to restart the kernel to use updated packages.

import os
from gtts import gTTS

genVoice = gTTS("Agora vamos usar o Google para gerar um áudio.", lang='pt') #'pt-br'

fileVoiceName = "genVoice01.mp3"
genVoice.save(fileVoiceName)

os.system(fileVoiceName)

# o Playsound é legal mas não funciona no colab
from playsound import playsound

playsound(fileVoiceName)


from IPython.display import Audio
Audio(fileVoiceName, autoplay=True)


#### Alternativa: pygame
pip install pygame

from pygame import mixer

mixer.init()
mixer.music.load(fileVoiceName)
mixer.music.play()


from gtts import lang

lang.tts_langs()

# tld = top level domain (accents available) for Google Translate
# https://www.google.com/supported_domains


genVoice = gTTS("Temos um combo com dois pastéis e um chopp", lang='pt', tld='com.br') 

fileVoiceName = "genVoice02.mp3"
genVoice.save(fileVoiceName)

playsound(fileVoiceName)

genVoice = gTTS("Temos um combo com dois pastéis e um chopp", lang='pt', tld='pt') 

fileVoiceName = "genVoice02.mp3"
genVoice.save(fileVoiceName)

playsound(fileVoiceName)

