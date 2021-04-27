import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def taking_command():
    try:
        with sr.Microphone() as source:
            print("\nListening . . .\n")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
    except (RuntimeError, TypeError, NameError, sr.UnknownValueError, UnboundLocalError):
        print('Sorry, I could not understand that.')
        talk('sorry, i could not understand that.')
    return command


def run_assistant():
    command = taking_command()
    if 'play' in command:
        song = command.replace('play', '')
        print('playing . . .')
        talk('playing ' + song + ' on youtube')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time is ' + time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'wikipedia' or 'info' or 'who is' or 'what is' in command:
        person = command.replace('who is' or 'what is', '')
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except:
            print('Sorry, I could not understand that.')
            talk('sorry, i could not understand that.')
    else:
        print('Please, say that again.')
        talk('Did you said something , sorry I could not able to hear that.')
        talk('Please, say that again.')


try:
    while True:
        run_assistant()
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate the Program")
    pass
