from numpy import take
import speech_recognition as sr
def take_command():
    query=''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        r.energy_threshold=430
        r.dynamic_energy_ratio=2.3
        audio=r.listen(source,0,3)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}")
    except:
        return ""
    
    query=str(query)
    return query.lower()
