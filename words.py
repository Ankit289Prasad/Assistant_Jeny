import pyttsx3 as p
import csv as c

engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def mean(name):
    name = name.capitalize()
    destination = "Dictionary_csv/"+name[0]+".csv"
    with open(destination, 'r') as csv_file:
        csv_reader = c.reader(csv_file)
        s = ""
        C = 0
        for line in csv_reader:
            #print(line)
            for ele in line:
                s = ele
                if s.split()[0] == name and C == 0:
                    engine.say("The meaning of '"+name+"' is"+s.split(')')[1])
                    print("The meaning of '"+name+"' is :"+s.split(')')[1])
                    engine.runAndWait()
                    C = 1

        if C==0:
            engine.say("Sorry buddy!! Unable to find the meaning of '"+name+"'.")
            print("Sorry buddy!! Unable to find the meaning of '" + name + "'.")
            engine.runAndWait()

#mean("jarvis")