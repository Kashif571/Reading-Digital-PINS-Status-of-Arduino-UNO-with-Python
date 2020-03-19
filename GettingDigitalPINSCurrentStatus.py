from serial import Serial
import time
from tkinter import *
import tkinter as tk

arduinodata = Serial("COM6",9600)

data1 = arduinodata.readline()

win = Tk()
win.title("Arduino")
win.geometry("800x600+50+50")
win.config(bg='white')

label1=Label(win, text="Digital PIN Status", font=("Calibri",24,"bold"), bg='white', borderwidth=1, relief="solid", padx=20, pady=20) #"flat", "raised", "sunken", "ridge", "solid", and "groove"
label1.pack(pady=(15,60))

firstdata=str(data1)

newdata=[]

i=2
for a0 in range(10):
    newdata.append(firstdata[i])
    i=i+2

lblframe = tk.Frame(win)
for a1 in range(10):
    pre1=Label(lblframe, text=("PIN",(a1+2)), font=("Calibri",12, "bold"), bg="white", borderwidth=1, relief="solid", padx=5, pady=2)
    pre1.grid(row=0, column=a1)
def mylabels():
    for a3 in range(10):
        if (int(newdata[a3]) == 1):
            pre3=Label(lblframe, text="OFF", font=("Calibri",12,"bold"), bg="white", fg="Green", borderwidth=1, relief="solid", padx=11, pady=1)
            pre3.grid(row=2, column=a3, sticky="nw")
        else:
            pre3=Label(lblframe, text="ON", font=("Calibri",12,"bold"), bg="white", fg="Red", borderwidth=1, relief="solid", padx=11, pady=1)
            pre3.grid(row=2, column=a3, sticky="nw")

lblframe.pack()

mylabels()

def statuschanger():
    newdata.clear()
    data2 = arduinodata.readline()
    seconddata=str(data2)
    j=2
    for a6 in range(10):
        newdata.append(seconddata[j])
        j=j+2
    mylabels()

    win.after(100, statuschanger)

statuschanger()

win.mainloop()