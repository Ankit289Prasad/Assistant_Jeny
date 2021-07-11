import speech_recognition as sr
import pyttsx3 as p
from web_auto import *
from web_auto1 import *
from web_automation import *
from recommendations import *
from words import *

r1 = sr.Recognizer()
engine = p.init()
engine.say("Hello buddy!! I am Jeny")
print("Jeny : Hello buddy!! I am Jeny.")
engine.runAndWait()
with sr.Microphone() as source:
    engine.say('how may I help you?')
    print("Jeny : How may I help you?")
    engine.runAndWait()
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print("You  : "+text.capitalize())
    except sr.UnknownValueError:
        engine.say("Unable to Understand!")
        print("Jeny : Unable to Understand!")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say(e)
        print(e)
        engine.runAndWait()