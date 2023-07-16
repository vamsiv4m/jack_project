import webbrowser
from Listen import take_command
from Speech import speak
try:
    speak("what you are looking for?")
    mytext=take_command().lower()
    webbrowser.open_new_tab(f"https://www.google.com/search?q={mytext}")
    
except Exception :
    speak("please tell again..")