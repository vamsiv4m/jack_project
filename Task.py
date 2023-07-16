import datetime
import os
import random

from numpy import take
from Listen import take_command
from Sketch import sketch
import wikipedia
import requests
from Speech import speak
from Timesheet import timesheet
import Automation as auto
from bs4 import BeautifulSoup


def wishme():
    a=""
    time = datetime.datetime.now().hour
    if(time >= 0 and time < 12):
        a="Good Morning!"
    elif(time >= 12 and time < 17):
        a="Good Afternoon!"
    else:
        a="Good Evening!"
    speak(a)

def tellDay():
    a=""
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        a=f"The day is {day_of_the_week}"
        print(a)
    speak(a)

def tell_Tomorrow_Day():
    a=""
    day = datetime.datetime.today().weekday() + 2
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day >= 8:
        day=1
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        a=f"The day is {day_of_the_week}"
        print(a)
    speak(a)

def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    d=datetime.datetime.strptime(time,"%H:%M")
    speak(d.strftime("%I:%M %p"))
    
def Date():
    date=datetime.date.today()
    speak(date)

def wiki(text):
    try:
        result=wikipedia.summary(text,sentences=2)
        speak(result)
    except Exception:
        speak("I can't find it....")

def NonInputFunctions(query):
    query=str(query)
    if "samay" in query:
        Time()

    elif "temperature" in query:
        temp1(query)

    elif "date" in query:
        Date()
    elif "day" in query:
        tellDay()
    elif "timesheet" in query or "attendance" in query:
        timesheet()
    elif "sketch" in query:
        sketch()
    elif "shutdown" in query:
        auto.shutdown()
    elif "restart" in query:
        auto.restart()
    elif "music" in query:
        music()
    elif "mail" in query:
        import mailing as ml
        speak("Please mention mail id to whom you are sending")
        mailid=input("Enter mail id : ")
        speak("Tell your message : ")
        content=take_command()
        ml.sendEmail(mailid,content)
    elif "note" in query:
        speak("Tell me what to write...")
        text=take_command()
        speak("See the preview..")
        print(text)
        speak("Do you want to save?")
        yes_no=take_command().lower()
        if "yes" in yes_no:
            auto.notepad(text)
        if "no" in yes_no:
            speak("as your wish...")
    elif "youtube" in query:
        from youtube import youtube
        youtube()

    elif "chrome" in query:
        import chrome

    elif "speedtest" in query:
        import MySpeedTest
    

def music():
    musiclist=["song1.mp3","song2.mp3","song3.mp3","song4.mp3","song5.mp3","song6.mp3","song7.mp3"]
    getmusic=random.choices(musiclist)
    mystr="".join(getmusic)
    os.startfile(f"C:\\Users\\HP\\OneDrive\\Desktop\\jack voice assistant\\music\\{mystr}")

def temp1(search):
    speak("Tell the city name?")
    myplace=take_command().lower()
    url=f"https://www.google.com/search?q={search+myplace}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temperature=data.find("div",class_="BNeawe").text
    speak(f"Currently in {myplace} is {temperature} ")

