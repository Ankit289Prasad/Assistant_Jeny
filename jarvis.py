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
    engine.say('how are you?')
    print("Jeny : How are you?")
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
i=0;
while i == 0 or i == 2:
    i = 0
    engine.say('how may I help you?')
    print("Jeny : How may I help you?")
    engine.runAndWait()
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r2.listen(source)
        try:
            text1 = r1.recognize_google(audio)
            print("You  : " + text1.capitalize())
        except sr.UnknownValueError:
            engine.say("Unable to Understand!")
            print("Jeny : Unable to Understand!")
            engine.runAndWait()
        except sr.RequestError as e:
            engine.say(e)
            print(e)
            engine.runAndWait()

    r3 = sr.Recognizer()
    if "information" in text1:
        engine.say("Information about what?")
        print("Jeny : Information about what?")
        engine.runAndWait()
        with sr.Microphone() as source1:
            audio2 = r3.listen(source1)
            try:
                information = r3.recognize_google(audio2)
                bot = info()
                bot.get_info(information)
            except sr.UnknownValueError:
                engine.say("Unable to Understand!")
                print("Jeny : Unable to Understand!")
                engine.runAndWait()
            except sr.RequestError as e:
                engine.say(e)
                print(e)
                engine.runAndWait()

    elif "meaning" in text1:
        mean(text1.split()[-1])

    elif "play" in text1:
        bot = music()
        engine.say("Okay buddy!! Playing '"+text1.split('play ')[1]+"'.")
        print("Jeny : Okay buddy!! Playing '" + text1.split('play ')[1].capitalize() + "'.")
        engine.runAndWait()
        bot.play(text1.split('play')[1])

    elif "review" in text1:
        bot = movie()
        if text1.split()[0] != "Review":
            bot.movie_review(text1.split('Review')[0])
        else:
            bot.movie_review(text.split('Review of')[1])

    elif "recommend" in text1 or ("suggest" in text1 and "movie" in text1):
        bot = recom()
        bot.recom_info()

    elif "joke" in text1:
        engine.say("You look good today!")
        print("Jeny : You look good today!")
        engine.runAndWait()

    else:
        i = 2

    if i == 2:
        engine.say("Unable to understand!! Try again!")
        print("Jeny : Unable to understand!! Try again!")
        engine.runAndWait()

    else:
        sR = sr.Recognizer()
        engine.say("Want to continue? (Yes/No)")
        print("Jeny : Want to continue? (Yes/No)")
        engine.runAndWait()
        with sr.Microphone() as source2:
            audio3 = sR.listen(source2)
            try:
                cond = sR.recognize_google(audio3)
                print("You  : "+cond.capitalize())
                if "yes" in cond and "no" not in cond:
                    i = 0
                elif "no" in cond and "yes" not in cond:
                    i = -1
                else:
                    i = -1
                    engine.say("Invalid speech!!...Terminated")
                    print("Jeny : Invalid speech!!...Terminated")
                    engine.runAndWait()
            except sr.UnknownValueError:
                engine.say("Unable to Understand!")
                print("Jeny : Unable to Understand!")
                engine.runAndWait()
            except sr.RequestError as e:
                engine.say(e)
                print(e)
                engine.runAndWait()
