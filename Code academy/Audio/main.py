import speech_recognition as sr
import sys
import webbrowser
import pyttsx3


def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say("You said " + words)
    engine.runAndWait()

talk("Good evening Mr. Mindaugas ir Mr.Vytautas. My name is Pyaudio. Please talk with me.")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("You said: " + task)
    except sr.UnknownValueError:
        talk("I can't hear you")
        task = command()

    return task

def makeSomething(task):
    if 'open website' in task:
        talk("I'm opening website")
        url = 'astrodoc.ca'
        webbrowser.open(url)
    elif 'goodnight' in task:
        talk('Yes, sure, no problem.')
        sys.exit()

while True:
    makeSomething(command())


