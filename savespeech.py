import speech_recognition as sr
import pyttsx3

## author: Mohamed Abdiaziz
## Description: This is speech recognition like google assistant

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.say("hello, I am Ahmed, i'm listening to you, call to help you by Saying; Hello Ahmed")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.Recognize_google(voice)
        command = command.lower()
        if 'Ahmed' in command:
            command = command.replace('How can i help you! ', '')
            print(command)
except:
    print("hello")
