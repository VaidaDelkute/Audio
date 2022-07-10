import speech_recognition as sr
import sys
import webbrowser
import pyttsx3
from time import ctime

def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say("You said " + words)
    engine.runAndWait()

talk("Good evening Mr. Mindaugas ir Mr.Vytautas. How I can help You?")

def command(ask = False):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        if ask:
            print(ask)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("You said: " + task)
    except sr.UnknownValueError:
        talk("I can't hear You")
        task = command()

    return task

def makeSomething(task):
    if "what is your name" in task:
        talk("My name is Pyaudio.")
    elif "what can you do" in task:
        talk("I can make Your dreams came true!")
    elif "what time is it" in task:
        talk (ctime())
    elif "i am bored" in task:
        talk("I will show You samething amazing.")
        url = 'astrodoc.ca'
        webbrowser.open(url)
    elif "i feel bad" in task:
        talk("I will help You.")
        url = 'sidabrilis.lt'
        webbrowser.open(url)
    elif "i am hungry" in task:
        talk("I am inviting You.")
        url = 'laurusrestoranas.lt'
        webbrowser.open(url)
    elif "i work too much" in task:
        talk("I will reserve the time.")
        url = 'rk-medicus.lt'
        webbrowser.open(url)
    elif "open website" in task:
        talk("I'm opening website.")
        url = 'bravogroup.hu/en/home/'
        webbrowser.open(url)
    elif "search" in task:
        talk("What do You want to search for?")
        search = command()
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        talk('Here is what I found for ' + search)
    elif "find location" in task:
        talk("What location You are looking for?")
        location = command()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        talk('Here is the location of ' + location)
    elif 'goodnight' in task:
        talk('It was nice to bee with You. Have a nice day!')
        sys.exit()

while True:
    makeSomething(command())


