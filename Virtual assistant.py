import pyttsx3
from datetime import datetime as dt
import speech_recognition as sr
import wikipedia as wiki
import webbrowser as wb
import os
import time as t
wake = False
hour = dt.now().hour
minute = dt.now().minute
second = dt.now().second
assistant = pyttsx3.init()
voices = assistant.getProperty("voices")
assistant.setProperty("voice",voices[1].id)
def timeNow():
        speak(f"{hour} hours {minute} minutes {second} seconds")
def speak(audio):
    assistant.say(audio)
    assistant.runAndWait()
def wishMe():
    if (hour > 0 and hour <= 10):
        speak("Good morning sir, I am Swift. your virtual instructor and helper, You can ask or order me anything that's in my range.")
    elif(hour >10 and hour <= 15):
        speak("Good afternoon sir, I am Swift. your virtual instructor and helper, You can ask or order me anything that's in my range.")
    elif(hour >15 and hour <= 17):
        speak("Good evening sir, I am Swift. your virtual instructor and helper, You can ask or order me anything that's in my range.")
    elif(hour > 17 and hour <=23):
        speak("Good night sir, I am Swift. your virtual instructor and helper, You can ask or order me anything that's in my range.")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.dynamic_energy_adjustment_damping = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language= "en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("I can't understand what you are saying.")
        speak("I cant't understand what you are saying")
        return "None"
    return query
while True:
        while True:
            if(wake != True):
                speak("Say awake or wake up to make swift turn on.")
                query = takeCommand().lower()
                t.sleep(6)
                if ("wake up" in query or "awake" in query):
                        wake = True
                        speak("Waking swift")
                        hour = dt.now().hour
                        minute = dt.now().minute
                        second = dt.now().second
                        wishMe()
                        while True:
                            query = takeCommand().lower()
                            if "search" in query:
                                speak("please wait sir!")
                                query = query.split("search")[1]
                                speak(f"Searching wikipedia about {query}")
                                results = wiki.summary(query, sentences = 2)
                                speak("According to wikipedia")
                                print(results)
                                speak(results)
                            elif "open youtube" in query:
                                speak("Opening youtube sir")
                                speak("Please wait")
                                wb.open("youtube.com")
                            elif "open chrome" in query:
                                speak("Opening chrome sir")
                                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                            elif ("what is your name" in query or "name" in query):
                                speak("My name is Swift sir.")
                            elif "time" in query:
                                timeNow()
                            elif "hibernate yourself" in query:
                                os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')
                            elif "wake up" in query:
                                speak("I am always awake sir.")
                            elif ("introduce yourself" in query or "who are you" in query):
                                speak("I am swift sir, your virtul instructor and helper, I am developed and managed by Anirban")
                            elif ("open ideal c" in query):
                                speak("openning ideal c sir")
                                os.startfile("C://Program Files/JetBrains/IntelliJ IDEA Community Edition 2020.3/bin/idea64.exe")
                            elif ("open pycharm" in query):
                                speak("openning pycharm sir")
                                os.startfile("C:/Program Files/JetBrains/PyCharm Community Edition 2020.3.2/bin/pycharm64.exe")
                            elif ("open android studio" in query):
                                speak("openning android studio sir")
                                os.startfile("C:/Program Files/Android\Android Studio/bin/studio64.exe")
                            elif ("open zoom" in query):
                                speak("openning zoom sir")
                                os.startfile("C:/Users/Administrator/AppData/Roaming/Zoom/bin/Zoom.exe")
                            elif ("open vs code" in query):
                                speak("openning vs code sir")
                                os.startfile("C:/Users/Administrator/AppData/Local/Programs/Microsoft VS Code/Code.exe")
                            elif ("don't disturb" in query or "stop disturbing" in query):
                                speak("Oh sorry sir!I didn't knew i was annoying you.")
                                quit()
                            elif ("meaning" in query):
                                speak("please wait sir.")
                                query = "meaning" + query.split("meaning")[1]
                                speak(f"searching the {query}")
                                results = wiki.summary(query, sentences = 2)
                                speak(f"according to wikipedia")
                                speak(results)
                                print(results)
                            elif ("swift sleep" in query or "go to sleep" in query or "close yourself" in query):
                                speak("As you wish sir!")
                                speak("Closing swift")
                                wake = False
                                quit()
                            else:
                                speak("I can't understand what you are saying., please elaborate")
                else :
                    continue
