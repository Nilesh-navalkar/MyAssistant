Python speech recognition:
    pip install SpeechRecognition
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
            print('listening...')
            voice = r.listen(source)
            command = r.recognize_google(voice)

    harvard = sr.AudioFile('aud.wav')
    with harvard as source:
            audio = r.record(source)
            this=r.recognize_google(audio)
_____________________________________________________________________________
            

Python text to speech:
    pip install pyttsx3
    import pyttsx3

    t2s = pyttsx3.init()
    voices = engine.getProperty('voices')  --->set of all voices
    t2s.setProperty('voice', voices[1].id) --->female voice
    def talk(text):
        t2s.say(text)
        t2s.runAndWait()

_____________________________________________________________________________

python wikipedia:
    pip install wikipedia
    import wikipedia

    info = wikipedia.summary(this, 10)

_____________________________________________________________________________

python whatsapp/email/yt:
    pip install pywhatkit
    import pywhatkit


    pywhatkit.playonyt(song)               #plays the song by opening youtube
    pywhatkit.image_to_ascii_art("p.jpg")  #converts p.jpg to ascii art
    pywhatkit.text_to_handwriting("text")  #returns png which contains text in handwriting

_____________________________________________________________________________

python datetime:
    import datetime

    time = datetime.datetime.now().strftime('%I:%M %p') #(12)hours-min-am/pm

_____________________________________________________________________________


python pyjokes:
    pip install pyjokes
    import pyjokes

    pyjokes.get_joke()

_____________________________________________________________________________


python screenshot:
    pip install pyscreenshot
    import pyscreenshot 

    img = pyscreenshot.grab()
    img.save("screencap.png")


_____________________________________________________________________________

python cv2 webcam image capture:

import cv2 as cv

cam = cv.VideoCapture(0)
result, image = cam.read()

if result:
	cv.imshow("framename", image)   #showing image output
	cv.imwrite("mypic.png", image)  #saving image in local storage
	cv.waitKey(0)  
	cv.destroyWindow("GeeksForGeeks")    #If keyboard interrupt occurs, destroy image window
else:
	print("No image detected. Please! try again")

_____________________________________________________________________________
    
python cv2 webcam vid capture:

import cv2

vid = cv2.VideoCapture(0)

while(True):
	
	
	ret, frame = vid.read()  # Capture the video frameby frame
	cv2.imshow('frame', frame) # Display the resulting frame
	if cv2.waitKey(1) & 0xFF == ord('q'):  # the 'q' button is set as the quitting button 
		break

vid.release() # After the loop release the cap object
cv2.destroyAllWindows() # Destroy all the windows

_____________________________________________________________________________

python ntlk
    pip install nltk
    #nltk.download('stopwords')
    #nltk.download('punkt')
    import nltk

    tokens = nltk.word_tokenize(sentence)   #tokenize
    words = [w for w in words if w not in stopwords.words(“english”)]   #remove useless words
    print(words)

