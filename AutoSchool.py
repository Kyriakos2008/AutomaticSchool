import pyautogui
import time
import keyboard
import random
import sys
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, Text
import os

pyautogui.FAILSAFE = False

def leave():
    leave1 = pyautogui.locateCenterOnScreen('leave.png')
    pyautogui.moveTo(leave1)
    pyautogui.click

def start():
    while 1:
        joina = pyautogui.locateCenterOnScreen('joina.png', confidence=0.8)
        if joina != None:
            print(joina)
            pyautogui.moveTo(joina)
            pyautogui.click()
            time.sleep(1)
            mic1 = pyautogui.locateCenterOnScreen('mic.png')
            if mic1 != None:
                pyautogui.moveTo(mic1)
                pyautogui.click()
                mic1 = None
                time.sleep(1)
            joinb = pyautogui.locateCenterOnScreen('joinb.png')
            pyautogui.moveTo(joinb)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(0, 0)
            time.sleep(1)
            chat1 = pyautogui.locateCenterOnScreen('chat.png')
            pyautogui.moveTo(chat1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('Gia', interval = 0.2)
            chat2 = pyautogui.locateCenterOnScreen('chatsend.png')
            pyautogui.moveTo(chat2)
            pyautogui.click()
            time.sleep(2100)
            leave()
            break
    #2
    while 1:
        joinc = pyautogui.locateCenterOnScreen('joina.png', confidence=0.8)
        if joinc != None and joinc != joina:
            print(joinc)
            pyautogui.moveTo(joinc)
            pyautogui.click()
            time.sleep(2)
            mic1 = pyautogui.locateCenterOnScreen('mic.png')
            if mic1 != None:
                pyautogui.moveTo(mic1)
                pyautogui.click()
                mic1 = None
                time.sleep(1)
            joinb = pyautogui.locateCenterOnScreen('joinb.png')
            pyautogui.moveTo(joinb)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(0, 0)
            time.sleep(1)
            chat1 = pyautogui.locateCenterOnScreen('chat.png')
            pyautogui.moveTo(chat1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('Gia', interval = 0.2)
            chat2 = pyautogui.locateCenterOnScreen('chatsend.png')
            pyautogui.moveTo(chat2)
            pyautogui.click()
            time.sleep(2100)
            leave()
            break
    time.sleep(1200)
    #3
    while 1:
        joind = pyautogui.locateCenterOnScreen('joina.png', confidence=0.8)
        if joind != None and joind != joina and joind != joinc:
            print(joind)
            pyautogui.moveTo(joind)
            pyautogui.click()
            time.sleep(2)
            mic1 = pyautogui.locateCenterOnScreen('mic.png')
            if mic1 != None:
                pyautogui.moveTo(mic1)
                pyautogui.click()
                mic1 = None
                time.sleep(1)
            joinb = pyautogui.locateCenterOnScreen('joinb.png')
            pyautogui.moveTo(joinb)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(0, 0)
            time.sleep(1)
            chat1 = pyautogui.locateCenterOnScreen('chat.png')
            pyautogui.moveTo(chat1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('Gia', interval = 0.2)
            chat2 = pyautogui.locateCenterOnScreen('chatsend.png')
            pyautogui.moveTo(chat2)
            pyautogui.click()
            time.sleep(2100)
            leave()
            break
    #4
    while 1:
        joine = pyautogui.locateCenterOnScreen('joina.png', confidence=0.8)
        if joine != None and joine != joina and joine != joinc and joine != joind:
            print(joine)
            pyautogui.moveTo(joine)
            pyautogui.click()
            time.sleep(2)
            mic1 = pyautogui.locateCenterOnScreen('mic.png')
            if mic1 != None:
                pyautogui.moveTo(mic1)
                pyautogui.click()
                mic1 = None
                time.sleep(1)
            joinb = pyautogui.locateCenterOnScreen('joinb.png')
            pyautogui.moveTo(joinb)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(0, 0)
            time.sleep(1)
            chat1 = pyautogui.locateCenterOnScreen('chat.png')
            pyautogui.moveTo(chat1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('Gia', interval = 0.2)
            chat2 = pyautogui.locateCenterOnScreen('chatsend.png')
            pyautogui.moveTo(chat2)
            pyautogui.click()
            time.sleep(2100)
            leave()
            break   
    time.sleep(1200)
    #5
    while 1:
        joinf = pyautogui.locateCenterOnScreen('joina.png', confidence=0.8)
        if joinf != None and joinf != joina and joinf != joinc and joinf != joind and joinf != joine:
            print(joinf)
            pyautogui.moveTo(joinf)
            pyautogui.click()
            time.sleep(2)
            mic1 = pyautogui.locateCenterOnScreen('mic.png')
            if mic1 != None:
                pyautogui.moveTo(mic1)
                pyautogui.click()
                mic1 = None
                time.sleep(1)
            joinb = pyautogui.locateCenterOnScreen('joinb.png')
            pyautogui.moveTo(joinb)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(0, 0)
            time.sleep(1)
            chat1 = pyautogui.locateCenterOnScreen('chat.png')
            pyautogui.moveTo(chat1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('Gia', interval = 0.2)
            chat2 = pyautogui.locateCenterOnScreen('chatsend.png')
            pyautogui.moveTo(chat2)
            pyautogui.click()
            time.sleep(2100)
            leave()
            break
    #6
    while 1:
        joing = pyautogui.locateCenterOnScreen('joina.png', confidence=0.8)
        if joing != None and joing != joina and joing != joinc and joing != joind and joing != joine and joing != joinf:
            print(joing)
            pyautogui.moveTo(joing)
            pyautogui.click()
            time.sleep(2)
            mic1 = pyautogui.locateCenterOnScreen('mic.png')
            if mic1 != None:
                pyautogui.moveTo(mic1)
                pyautogui.click()
                mic1 = None
                time.sleep(1)
            joinb = pyautogui.locateCenterOnScreen('joinb.png')
            pyautogui.moveTo(joinb)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(0, 0)
            time.sleep(1)
            chat1 = pyautogui.locateCenterOnScreen('chat.png')
            pyautogui.moveTo(chat1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('Gia', interval = 0.2)
            chat2 = pyautogui.locateCenterOnScreen('chatsend.png')
            pyautogui.moveTo(chat2)
            pyautogui.click()
            time.sleep(2100)
            leave()
            break
    time.sleep(1200)
    #7
    while 1:
        join7 = pyautogui.locateCenterOnScreen('joina.png', confidence=0.8)
        if join7 != None and join7 != joina and join7 != joinc and join7 != joind and join7 != joine and join7 != joinf and join7 != joing:
            print(join7)
            pyautogui.moveTo(join7)
            pyautogui.click()
            time.sleep(2)
            mic1 = pyautogui.locateCenterOnScreen('mic.png')
            if mic1 != None:
                pyautogui.moveTo(mic1)
                pyautogui.click()
                mic1 = None
                time.sleep(1)
            joinb = pyautogui.locateCenterOnScreen('joinb.png')
            pyautogui.moveTo(joinb)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(0, 0)
            time.sleep(1)
            chat1 = pyautogui.locateCenterOnScreen('chat.png')
            pyautogui.moveTo(chat1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('Gia', interval = 0.2)
            chat2 = pyautogui.locateCenterOnScreen('chatsend.png')
            pyautogui.moveTo(chat2)
            pyautogui.click()
            time.sleep(2100)
            leave()
            break
    ora = datetime.datetime.now()
    twra = ora.strftime("%A")

    if twra != "Wednesday" or twra == "Friday":
        while 1:
            join8 = pyautogui.locateCenterOnScreen('joina.png', confidence=0.8)
            if join8 != None and join8 != joina and join8 != joinc and join8 != joind and join8 != joine and join8 != joinf and join8 != joing and join8 != join7:
                print(join8)
                pyautogui.moveTo(join8)
                pyautogui.click()
                time.sleep(2)
                mic1 = pyautogui.locateCenterOnScreen('mic.png')
                if mic1 != None:
                    pyautogui.moveTo(mic1)
                    pyautogui.click()
                    mic1 = None
                    time.sleep(1)
                joinb = pyautogui.locateCenterOnScreen('joinb.png')
                pyautogui.moveTo(joinb)
                pyautogui.click()
                time.sleep(2)
                pyautogui.moveTo(0, 0)
                time.sleep(1)
                chat1 = pyautogui.locateCenterOnScreen('chat.png')
                pyautogui.moveTo(chat1)
                pyautogui.click()
                time.sleep(2)
                pyautogui.write('Gia', interval = 0.2)
                chat2 = pyautogui.locateCenterOnScreen('chatsend.png')
                pyautogui.moveTo(chat2)
                pyautogui.click()
                time.sleep(2100)
                leave()
                break



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
root = tk.Tk()
canvas = tk.Canvas(root, height=300, width=300, bg="gray10")
canvas.pack()
root.title("School Bot V2")

frame = tk.Frame(root, bg="gray40")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
button = tk.Button(root, text="Start", pady=5, padx=10, bg="RoyalBlue", command=start)
button.place(x=130, y=100)
exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="IndianRed1") 
exit_button.place(y=134, x=141) 
label = tk.Label(root, text="Press start to start", fg="black", bg="gray40", font = "Verdana 10 bold")
label.config(font=("Courier", 14))
label.place(x=35, y=180)
label1 = tk.Label(root, text="Press exit to exit", fg="black", bg="gray40", font = "Verdana 10 bold")
label1.config(font=("Courier", 11))
label1.place(x=65, y=200)

root.mainloop()
