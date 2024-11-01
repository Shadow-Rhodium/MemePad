from multiprocessing import Process
import os
import smtplib
from email.mime.text import MIMEText
import pygame as VHS
import time as clock

def email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


def mp3(dir):
    VHS.mixer.init()

    try:
        VHS.mixer.music.load(f"C:/Users/HassanHN/Music/Meme/{dir}.mp3")
        VHS.mixer.music.play()
        while VHS.mixer.music.get_busy():  # wait for music to finish playing
            clock.sleep(1)  # Load the popular external library

    except:
        print("No Sound File")

def Watch():
    os.system("c:/Users/HassanHN/OneDrive/Desktop/timer.py")

def Chrono():
    Process(target=Watch).start()

