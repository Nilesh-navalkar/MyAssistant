import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(source, duration=1)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

        return command
    except:
        return "whatchasaid"


def run_alexa():
    Command = take_command()
    print(Command)
    if 'play' in Command:
        song = Command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in Command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search' in Command:
        this = Command.replace('search', '')
        info = wikipedia.summary(this, 10)
        print(info)
        talk(info)
    elif 'joke' in Command:
        talk(pyjokes.get_joke())
    elif 'hello' in Command:
        talk("hell u ")
    else:
        talk('Please say the command again.')


while True:
    run_alexa()