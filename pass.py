import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import os
# import datetime
# import wikipedia #pip install wikipedia
# import webbrowser
# import pywhatkit as kit
# import os
# import smtplib
# import random
# import pyautogui
# import psutil
# import pyjokes

code=['Hey you have to tell a passcode to access Jarvis! Please tell the passcodewhe you see listening in the console!']
mauka=['The password is wrong please repeat!']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def ask():
    speak(code)

def chance():
    speak(mauka)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    ask()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'ben' in query:
            os.system('python main.py')
            exit()
        else:
            speak('Your passcode is not Correct!')
            chance()
