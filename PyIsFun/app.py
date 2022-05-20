import pyttsx3
import datetime
import wikipedia
import pyjokes
import nltk


ignored_words = nltk.corpus.stopwords.words('english')
ttos = pyttsx3.init()
voices = ttos.getProperty('voices')
ttos.setProperty('voice', voices[1].id)  

joke=pyjokes.get_joke()
ttos.say(joke)
ttos.runAndWait()
print(joke)
tokens = nltk.word_tokenize(joke)   #tokenize
words = [w for w in tokens if w not in ignored_words]   #remove useless words
print(words)

for i in words:
    ttos.say(wikipedia.summary(i,2))
    ttos.runAndWait()


