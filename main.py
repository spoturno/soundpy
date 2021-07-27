#!/usr/bin/env python3

import speech_recognition as sr
import os
from gtts import gTTS

# from microphone to google voice
voice = ""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text == "stop":
                break
            text = r.recognize_google(audio)
            voice = voice + str(text)
        except:
            print("say something....")
hr = gTTS(text=voice, lang='en', slow=False)
hr.save("1.mp3")





