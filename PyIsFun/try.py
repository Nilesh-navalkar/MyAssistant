'''
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
ttos = pyttsx3.init()
voices = ttos.getProperty('voices')
ttos.setProperty('voice', voices[1].id)  

with sr.Microphone() as source:
	print('listening...')
	voice = listener.listen(source)
	listener.pause_threshold = 1
	listener.adjust_for_ambient_noise(source, duration=1)
	command = listener.recognize_google(voice)
	command = command.lower()
	print(command)
	ttos.say(command)
	ttos.runAndWait()
'''
from calendar import c
import cv2 as cv

cam = cv.VideoCapture(0)
result, image = cam.read()
if result:
	print("taking picture")
	cv.imwrite("mypic.png", image)  #saving image in local storage
	print("picture taken")
else:
    print("No image detected. Please! try again")