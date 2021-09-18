import sqlite3
from tkinter import *
import cv2

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def shutdown():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s')


def restart():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('restarting your computer')
    os.system('restart -s')


def gooffline():
    speak('ok sir')
    speak('closing all systems')
    speak('disconnecting to servers')
    speak('going offline')
    quit()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning A J")
        window.update()
        speak("Good Morning A..J...")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon A J")
        window.update()
        speak("Good Afternoon A..J...")
    else:
        var.set("Good Evening A J")
        window.update()
        speak("Good Evening A..J...")
    speak("Myself SMART CHATBOT. How may I help you sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='orange')
    wishme()
    while True:
        btn1.configure(bg='orange')
        query = takeCommand().lower()

        '''savedata = open('data.txt', "a")
        savedata.write(query)'''

        with open('data.txt',"a+") as file_object:
            file_object.seek(0)
            data=file_object.read(100)
            if len(data)>0:
                file_object.write("\n")
            file_object.write(query)

        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")

                    query = query.lower()
                    query = query.replace("what is")
                    query = query.replace('who is')
                    query = query.replace('do u know')
                    query = query.replace('how to')

                    results = wikipedia.summary(query, sentences = 3)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open course era' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")
        elif 'shutdown' in query:
            shutdown()
        elif 'restart' in query:
            restart()
        elif "offline" in query.lower():
            gooffline()

        elif "play video" in query.lower():
            speak("playing video")
            video = "H:\\movies\\autobiography.s01e09.the.story.of.ford.vs.ferrari.720p.web.x264-robots[eztv].mkv"
            print(video)
            os.startfile(os.path.join(video, video[2]))

        elif 'open stack overflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')


        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = "C:\\Users\\admin\\OneDrive\\Desktop\\DESKTOP\\wedding"
            songs = os.listdir(music_dir)
            n = random.randint(0, 3)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" % strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")



        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        elif 'open calculator' in query:
            var.set("opening CALCULATOR")
            window.update()
            speak("opening CALCULATOR")
            webbrowser.open("calculator.com")

        elif 'your name' in query:
            var.set("Myself SMART BOT Sir")
            window.update()
            speak('myself SMART BOT sir')

        elif 'who creates you' in query:
            var.set('My Creator is AJ')
            window.update()
            speak('My Creator is A..J..')

        elif 'say hello' in query:
            var.set('Hello Everyone! My self SMART BOT')
            window.update()
            speak('Hello Everyone! My self SMART BOT')

        elif 'open pycharm' in query:
            var.set("Openong Pycharm")
            window.update()
            speak("Opening Pycharm")
            path = "H:\pycharm\PyCharm 2021.1.2\bin\pycharm64.exe"
            os.startfile(path)

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(path)



        elif "play rock paper" in query:
            var.set("Opening Game")
            window.update()
            speak('opening Game')
            os.system('python Rock_Paper.py')



        elif 'open anaconda' in query:
            var.set('Opening Anaconda')
            window.update()
            speak('opening anaconda')
            os.startfile("C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)")





        elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg', frame)
            stream.release()


        elif 'open chat' in query:
            var.set("Opening Chat")
            window.update()
            speak('Opening Chat')
            os.system('python chat.py')



def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='white', fg='black')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='02.gif', format='gif -index %i' % (i)) for i in range(100)]
window.title('AJ SMART CHATBOT ')

label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)

#creating database
'''def create():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users( slno integer primary key autoincrement , user1 TEXT , user2 TEXT)")
    conn.commit()
    conn.close()
create()'''

btn0 = Button(text='WISH ME', width=20, command=wishme, bg='black', fg='white')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='PLAY', width=20, command=play, bg='yellow', fg='black')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


#saving database
'''def savedata():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute('INSERT INTO users(user,text) VALUES (?,?)',(var1.get(),var.get()))
    conn.commit()'''


window.mainloop()





