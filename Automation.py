from os import startfile
import calendar
import time
import os
import Speech
import pygetwindow as pg
from pynput.keyboard import Controller,Key
def notepad(text):
    filename=f"myfile{calendar.timegm(time.gmtime())}.txt"
    with open(filename,"w") as file:
        file.write(text)
    path_1="C:\\Users\\HP\\OneDrive\\Desktop\\jack voice assistant\\"+filename
    path_2="C:\\Users\\HP\\OneDrive\\Desktop\\jack voice assistant\\notepad\\"+filename
    os.rename(path_1,path_2)
    os.startfile(path_2)

def close_notepad():
    os.system("TASKKILL /F /im Notepad.exe")


def visual_studio():
    startfile("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

def shutdown():
    Speech.speak("Shutdown process will start in 5 seconds...")
    os.system("shutdown /s /t 5")

def restart():
    Speech.speak("Your system will restart in 5 seconds...")
    os.system("shutdown /r /t 5")
