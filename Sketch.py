import cv2
import tkinter as tk
from tkinter import filedialog
from Speech import speak
import random
responses=["Converting image to sketch ... please wait....",
                "Generating a sketch for you sir",
                "Drawing takes time... A line has time in it.",
                "I wish I could draw the image how I see .",
                "Sketch everything! and keep your curiosity fresh",
                "To learn to draw is to draw and draw and draw.",
                "I love the quality of my pencil. It helps me to get to the core of a thing."]
def sketch():
    try:
        speak(random.choices(responses))
        speak("Please select a file....")
        filetypes = (
            ('jpg type', '*.jpg'), 
            ('png type', '*.png*')
        )
        filepath=filedialog.askopenfilename(filetypes=filetypes,initialdir="/Pictures")
        img = cv2.imread(filepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_MEAN_C, 7, 7)
        color = cv2.bilateralFilter(img, 9, 250, 250)
        cv2.imshow("edges", edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception :
        speak("please open file")
        sketch()
