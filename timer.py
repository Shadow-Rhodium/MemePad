import time as clock
import pyautogui as cmd
from pygame import mixer as audio
import random as Spin


audio.init()
def alarm(dir, msg):
    D = 0
    audio.music.load(f"C:/Users/HassanHN/Music/Meme/{dir}.mp3")
    audio.music.play()

    while audio.music.get_busy():  # wait for music to finish playing
        clock.sleep(1)
        D = cmd.alert(msg)  # Load the popular external library
        if D == "OK":
            break



i = cmd.prompt("Set Timer: ")
try:
    ii = int(i)

except:
    ii = Spin.randrange(0,100)

print(f'{ii} seconds')

for f in range(ii):
    print(f'{f} seconds')
    clock.sleep(1)

alarm("Ding2", "Timer Done")


 


            



