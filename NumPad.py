import serial as USB #Make sure to do pip install pyserial in CMD
import time as clock
import pyautogui as cmd
import webbrowser as net
from MemeFunctions import *
import google.generativeai as Megatron
from moviepy.editor import VideoFileClip as VFC
from os import system as stm
import cv2

port = None

while True:
    for p in range(0,10):
        try:
            USB.Serial(f"COM{p}")
            clock.sleep(2)
            port = p
            break
            

        except:
            print("Waiting for input")
            #continue

    if port != None:
        break


if __name__ == '__main__':

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = Megatron.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    Megatron.configure(api_key="AIzaSyA8ApgHh3DVJYL1m5RL9dpPRUiDzfdYjvI")
    c = 0

    sender = "sb10599@dnsalbarsha.com"

    logo = "C:/Users/HassanHN/OneDrive/Pictures/Memepad.png"

    # Load an image
    img = cv2.imread(logo)

    # Display the image
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    print('''
        ⠀⠀⠀⠀⠀⣀⡠⠶⠄⠠⠒⠒⠂⡠⠴⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⠤⠎⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⡀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢆⠀⠀⠀⠀
    ⡜⠙⠀⠀⠀⠀⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠓⡆⠀⠀
    ⠀⢢⠀⠀⠀⡄⠒⠚⠳⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⣄⠀
    ⠀⠈⠆⠀⡜⠬⢅⡂⠠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⠄⡀⠒⠂⠀⠀⠀⠠⠼⡀
    ⠀⠀⠈⢢⠱⡀⠀⠀⡩⠃⠀⠀⡠⠀⠀⠀⠀⠠⢌⣀⡀⠀⠑⡀⠀⠀⠀⠀⠠⢇
    ⠀⠀⠀⠀⠑⢬⡉⠉⠀⠀⠀⠀⠑⠀⠀⠀⠀⠏⠀⠒⠢⠤⠬⠁⠀⠀⠀⡠⠌⠜
    ⠀⠀⠀⠀⠀⠀⠈⠒⠤⣀⠀⠑⠖⠒⠒⠀⠀⠈⠢⠤⠤⠄⠂⢀⡠⠔⠉⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠉⡐⣲⡤⢤⢀⣀⣀⠤⢤⠄⠒⠈⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⡏⠋⣳⠈⠊⠐⠁⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡳⠤⣓⠄⣛⣙⡤⢤⡤⠤⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠈⠈⠐⠊⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⢄⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣃⡀⠀⠀⢈⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠉⡔⠈⠁⠐⠢⠤⠤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠘⠢⠤⠄⣀⣀⠠⠄⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ''')

    print("Welcome to Pillow World, Brian")
    mp3("Pillow")

    password = cmd.password(text="Enter gmail password: ", title='NumPad', default='', mask='&')


    try:
        ser = USB.Serial("COM4") #COM can be found in Arduino IDE
        clock.sleep(2)
        mp3('Approved')
        print("NumPad Started")
        
        
        while True:
            try:
                li = ser.readline().decode("utf-8") 
                KEY = str(li)

            except:
                print("Arduino Disconnected")
                mp3("Meme")
                break

            print(f"Key: {KEY}")

            try:
                if KEY[0] == "*":
                        print("OFF")
                        off = cmd.alert("Turning Off")
                        if off == "OK":
                            mp3("losers")
                            break

                        else:
                            print("OFF canceled")

                if KEY[0] == "#":
                    print("Censoring")
                    mp3("Cnesor")

                if KEY[0] == "A":
                    print("Opening Noon")
                    mp3('Sandwich')
                    net.open("noon.com")
                    
                if KEY[0] == "B":
                    print("Opening Youtube")
                    net.open("Youtube.com")
                    mp3('YOTUUBE')

                if KEY[0] == "C":
                    print("Screenshot")
                    mp3("Cheese")  
                    n = cmd.prompt("Name picture")
                    cmd.screenshot(f"C:/Users/HassanHN/OneDrive/Pictures/SCreenies/NP_{n}.png")

                if KEY[0] == "D":
                    print("I ran out of ideas :/")
                    mp3("Here")
                    VFC("C:/Users/HassanHN/Videos/Upside.mov").resize(0.6).preview()
                    VHS.quit() 

                    stm("systeminfo")
                    clock.sleep(5)

                    D = cmd.confirm("Also here are your PC specs")

                    if D == "Cancel":
                        mp3("Crack")
                        S = cmd.prompt("Enter CMD Command")
                        stm(S)

                    else:
                        continue

        
            except:
                continue


            try:
                if int(KEY) == 5:
                    print("Translator")
                    cmd.keyDown("ctrl")
                    for f in range(2):
                        cmd.press("c")
                    cmd.keyUp("ctrl")
                    mp3("Smarter")

                if int(KEY) == 0:
                    print("Counter")
                    c= c+1
                    mp3("House")
                    cmd.alert(f"Counter: {c}")

                if int(KEY) == 1:
                    print("Counter Edit")
                    mp3("Domain")
                    c= int(cmd.prompt(text='Counter edit', title='NumPad' , default=''))
                    cmd.alert(f"Counter: {c}")

                if int(KEY) == 8:
                    print("Show Counter")
                    mp3("Move")
                    cmd.alert(f"Counter: {c}")


                if int(KEY) == 7:
                    print("Quick Email")
                    rcp = []

                    sub= cmd.prompt(text='Subject', title='NumPad' , default='')
                    bd = cmd.prompt(text='Body', title='NumPad' , default='')

                    rcpN = int(cmd.prompt(text='Number of Recipants', title='NumPad' , default=''))
                    for i in range(rcpN):
                        r = cmd.prompt(text='Recipant', title='NumPad' , default='')
                        rcp.append(r)

                    email(sub, bd, sender, rcp, password)
                    mp3("Short")


                if int(KEY) == 4:
                    print("Closing tab")
                    cmd.keyDown("alt")
                    cmd.press("f4")
                    cmd.keyUp("alt")
                    mp3("Walt")
                    

                if int(KEY) == 9:
                    mp3("Fan")
                    print("Fan ON")

                if int(KEY) == 6:
                    mp3("Ice")
                    print("Fan OFF")

                if int(KEY) == 3:
                    message = cmd.prompt("User")
                    mp3("Check")
                    response = chat_session.send_message(message)
                    cmd.alert(response.text)
                    
                if int(KEY) == 2:
                    print("Timer") 
                    mp3("Warudo") 
                    Chrono()


            except:
                continue
    
    

    except:
        mp3("NoMeme")
        print("Arduino not connected")
                  
