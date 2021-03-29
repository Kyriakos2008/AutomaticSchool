import pyautogui
import tkinter as tk
from tkinter import filedialog, Text
import os
import sys 
import trace 
import threading 
import time 

pyautogui.FAILSAFE = False




def start():
    print("Doulefki")
    while 1:
        mute = pyautogui.locateCenterOnScreen('Mute.png')
        if mute != None:
            pyautogui.moveTo(mute)
            pyautogui.click()
            pyautogui.moveTo(10, 10)
        

t1 = threading.Thread(target=start)

def kostis():
    t1.start() 

def pampos():
    root.destroy()

root = tk.Tk()
canvas = tk.Canvas(root, height=300, width=300, bg="gray11")
canvas.pack()
root.title("Muter V1")

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
button = tk.Button(root, text="Start", pady=5, padx=10, bg="RoyalBlue", command=kostis )
button.place(x=130, y=100)
exit_button = tk.Button(root, text="Exit", command=pampos, bg="IndianRed1") 
exit_button.place(y=134, x=141) 
label = tk.Label(root, text="Apla pata Start vlaka", fg="black", bg="white")
label.config(font=("Courier", 14))
label.place(x=35, y=180)
label1 = tk.Label(root, text="Tze Exit gia na fkis manne", fg="black", bg="white")
label1.config(font=("Courier", 11))
label1.place(x=34, y=200)

root.mainloop()