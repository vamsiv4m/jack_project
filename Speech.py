import pyttsx3 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',160)

def speak(text):
    print(f"My AI : {text}")
    engine.say(f'<pitch middle="10">{text}</pitch>')
    engine.runAndWait()

