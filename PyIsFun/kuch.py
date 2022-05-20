'''import datetime
import pyttsx3


time = datetime.datetime.now().strftime('%I:%M %p')
s = pyttsx3.init()
voices = s.getProperty('voices')
s.setProperty('voice', voices[1].id)  
s.say("current time is "+time)
s.runAndWait()'''
''' 
import speech_recognition as sr

r=sr.Recognizer()
harvard = sr.AudioFile('aud.wav')
with harvard as source:
    audio = r.record(source)
    this=r.recognize_google(audio)
    print(this)
    '''

import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime
import pywhatkit
import pyjokes
import pyscreenshot
import cv2 as cv

r = sr.Recognizer()
def getcommand():
    try:
        with sr.Microphone() as source:
                        print('listening...')
                        voice = r.listen(source)
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source, duration=1)
                        command = r.recognize_google(voice)
                        print(command)
                        if "hey assistant" in command:
                            command=command.replace("hey assistant","")

                        return command
    except sr.UnknownValueError:
        return "not found"
        
s = pyttsx3.init()
def reply():
    c=getcommand()
    print(c)
    if "search" in c:
        c=c.replace("search","")
        info=wikipedia.summary(c,2)
        s.say(info)
        s.runAndWait()
    elif "current time" in c:
        s.say("current time is "+ datetime.datetime.now().strftime('%I:%M %p'))
        s.runAndWait()
    elif "play song" in c:
        c=c.replace("play song","")
        pywhatkit.playonyt(c)
    elif "say a joke"  in c:
        s.say(pyjokes.get_joke())
        s.runAndWait()
    elif "take screenshot" in c:
        img=pyscreenshot.grab()
        img.save("name.png")
        s.say("screenchot taken")
        s.runAndWait()
    elif("take my picture") in c:
        cam = cv.VideoCapture(0)
        result, image = cam.read()
        if result:
            s.say("taking picture")
            s.runAndWait()
            cv.imwrite("mypic.png", image)  #saving image in local storage
            s.say("picture taken")
            s.runAndWait()
        else:
            s.say("No image detected. Please! try again")
            s.runAndWait()
    else:
        s.say("i could not understand the command")
        s.runAndWait()


while True:
    reply()






