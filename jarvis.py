import speech_recognition as sr
import pyttsx3 as p
from web_auto import *
from web_auto1 import *
from web_automation import *
from recommendations import *
from words import *

r1 = sr.Recognizer()
engine = p.init()
engine.say("Hello buddy!! I am Jeny, how may I help you?")
print("Jeny : Hello buddy!! I am Jeny, how may I help you?")
engine.runAndWait()
with sr.Microphone() as source:
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print("You  : "+text)
    except sr.UnknownValueError:
        engine.say("Unable to Understand!")
        print("Jeny : Unable to Understand!")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say(e)
        print(e)
        engine.runAndWait()