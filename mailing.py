import smtplib
from Speech import speak
def sendEmail(to,content):
    try:
        server= smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('world143hello@gmail.com','Jj@9876543210')
        server.sendmail('world143hello@gmail.com',to,content)
        server.close()
        speak("Mail has sent successfully")
    except Exception:
        print("Something went wrong check your mail Id once...")