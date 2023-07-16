import speedtest
from Speech import speak

speak("I'm calculating your network speed... please wait...")
speed=speedtest.Speedtest()
download_speed=speed.download()
upload_speed=speed.upload()
ctr_download=int(download_speed)/800000
ctr_upload=int(upload_speed)/800000
speak(f"your downloading speed is : {int(ctr_download)} Mb per second and Your uploading speed is : {int(ctr_upload)} Mb per second")