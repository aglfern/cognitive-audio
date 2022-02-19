# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 18:58:54 2021

@author: aglfen@gmail.com

https://github.com/Azure-Samples/cognitive-services-speech-sdk/blob/master/samples/python/console/speech_sample.py

https://www.youtube.com/watch?v=h9lnrVZclOk
https://github.com/caiomsouza/Microsoft-Cognitive-Services/tree/master/speech-to-text

https://stackoverflow.com/questions/58854194/microsoft-speech-to-text-python-sdk-spxerr-invalid-header-issue


https://docs.microsoft.com/pt-br/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech?view=azure-python


Samples
https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/quickstart/python

"""

# pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk


# mySubsc = "575424fa-3707-4cc1-90f2-5c2f97dc202d"
myKey = "{coloque sua chave aqui}" 
myRegion = "brazilsouth"

speech_config = speechsdk.SpeechConfig(subscription=myKey, region=myRegion)


#### Parte 1 - Sintetizar


# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Receives a text from console input.
print("Type some text that you want to speak...")
textEntered = input()

print("This is your text: [" + textEntered + "]")

textEntered = "Hey there what is up?"

# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
result = speech_synthesizer.speak_text_async(textEntered).get()

# Checks result.
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(textEntered))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")
   

#### Changing the voice


    # Creates a speech synthesizer.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

    print("Enter a locale in BCP-47 format (e.g. en-US) that you want to get the voices of, or enter empty to get voices in all locales.")
    try:
        text = input()
    except EOFError:
        pass

    text = 'en-US'

    result = speech_synthesizer.get_voices_async(text).get()
    # Check result
    if result.reason == speechsdk.ResultReason.VoicesListRetrieved:
        print('Voices successfully retrieved, they are:')
        for voice in result.voices:
            print(voice.name)
    elif result.reason == speechsdk.ResultReason.Canceled:
        print("Speech synthesis canceled; error details: {}".format(result.error_details))    
   
    
    
#### Parte 2 - Reconhecer 

audioFile = 'speech-to-text_data_audio1.wav'

# não reconhece .wav...
#from playsound import playsound
#playsound("speech-to-text_data_audio1.wav")

import os
os.system(audioFile)

# não funciona com mp3...
audio_input = speechsdk.audio.AudioConfig(filename=audioFile)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

result = speech_recognizer.recognize_once()

print('Audio file content convert to text:')
print('|')
print(result)


#### Com microfone


def speech_recognize_once_from_mic():
    """performs one-shot speech recognition from the default microphone"""
    # <SpeechRecognitionWithMicrophone>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Creates a speech recognizer using microphone as audio input.
    # The default language is "en-us".
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language='pt-BR')

    # Starts speech recognition, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed. It returns the recognition text as result.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = speech_recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    # </SpeechRecognitionWithMicrophone>


import json

def speech_recognize_once_from_file_with_detailed_recognition_results():
    """performs one-shot speech recognition with input from an audio file, showing detailed recognition results including word-level timing"""
    # <SpeechRecognitionFromFileWithDetailedRecognitionResults>
    speech_config = speechsdk.SpeechConfig(subscription=myKey, region=myRegion)

    # Ask for detailed recognition result
    speech_config.output_format = speechsdk.OutputFormat.Detailed

    # If you also want word-level timing in the detailed recognition results, set the following.
    # Note that if you set the following, you can omit the previous line
    #   "speech_config.output_format = speechsdk.OutputFormat.Detailed",
    # since word-level timing implies detailed recognition results.
    speech_config.request_word_level_timestamps()

    audio_config = speechsdk.audio.AudioConfig(filename=audioFile)

    # Creates a speech recognizer using a file as audio input, also specify the speech language
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, language="en-US", audio_config=audio_config)

    # Starts speech recognition, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed. It returns the recognition text as result.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = speech_recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))

        # Time units are in hundreds of nanoseconds (HNS), where 10000 HNS equals 1 millisecond
        print("Offset: {}".format(result.offset))
        print("Duration: {}".format(result.duration))

        # Now get the detailed recognition results from the JSON
        json_result = json.loads(result.json)

        # The first cell in the NBest list corresponds to the recognition results 
        # (NOT the cell with the highest confidence number!)
        print("Detailed results - Lexical: {}".format(json_result['NBest'][0]['Lexical']))
        # ITN stands for Inverse Text Normalization
        print("Detailed results - ITN: {}".format(json_result['NBest'][0]['ITN']))
        print("Detailed results - MaskedITN: {}".format(json_result['NBest'][0]['MaskedITN']))
        print("Detailed results - Display: {}".format(json_result['NBest'][0]['Display']))

        # Print word-level timing. Time units are HNS.
        words = json_result['NBest'][0]['Words']
        print(f"Detailed results - Word timing:\nWord:\tOffset:\tDuration:")
        for word in words:
            print(f"{word['Word']}\t{word['Offset']}\t{word['Duration']}")

        # You can access alternative recognition results through json_result['NBest'][i], i=1,2,..

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    # </SpeechRecognitionFromFileWithDetailedRecognitionResults>


speech_recognize_once_from_file_with_detailed_recognition_results()
