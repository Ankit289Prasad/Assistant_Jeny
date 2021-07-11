import speech_recognition as sr
import pyttsx3 as p
from web_auto import *
from web_auto1 import *
from web_automation import *
from recommendations import *
from words import *

r1 = sr.Recognizer()
engine = p.init()
engine.say("Hello buddy!! I am Jeny, how may I help you")
engine.runAndWait()