# Digital-Pin-Status
The Program reads Digital PINS of Arduino UNO with Python Tkinter and Display on GUI Screen. 

# Working of Arduino UNO in Python Program:
Serial Method is used to read the Digital PINS of Arduino and then the values are stored into an array namely newdata. Then after using it once the array is cleared and stored the next data is read again from Arduino and then displayed it on GUI Screen. This Process Continous...

# Working of Python Tkinter:
With python Tkinter first, the Heading is Displayed, then a Row of Labels is Displayed below the heading that Displays the DIGITAL PINS heading as PIN0, PIN1, PIN2, etc.

Then in the next row "ON" and "OFF" text is showed that represents the states of the Arduino Board. If a PIN is ON it sends "1" as output. That output is stored in newdata Array and Finally, if the index of the array contains "1" it shows "ON" on GUI Screen. Similarly, if array Contains "0" it shows "OFF" on output Screen.

#Code with Descripion:
from serial import Serial
import time
from tkinter import *
import tkinter as tk

#Reading Arduino
arduinodata = Serial("COM6",9600)

#Storing Arduino Data in data1 Array
data1 = arduinodata.readline()

#Creating GUI Screen  
win = Tk()
win.title("Arduino")
win.geometry("800x600+50+50")
win.config(bg='white')

#Displaying Heading on GUI Screen  
label1=Label(win, text="Digital PIN Status", font=("Calibri",24,"bold"), bg='white', borderwidth=1, relief="solid", padx=20, pady=20) #"flat", "raised", "sunken", "ridge", "solid", and "groove"
label1.pack(pady=(15,60))

#Converting Datatype of data1 array from binary to string. 
firstdata=str(data1)

#Initiliazating Array to store Values of Current and Previous state of Arduino Digital Pins.
newdata=[]

#Storing Arduino data into arrays.
i=2
for a0 in range(10):
    newdata.append(firstdata[i])
    i=i+2

lblframe = tk.Frame(win)
#Displaying Digital PIN heading on GUI Screen.
for a1 in range(10):
    pre1=Label(lblframe, text=("PIN",(a1+2)), font=("Calibri",12, "bold"), bg="white", borderwidth=1, relief="solid", padx=5, pady=2)
    pre1.grid(row=0, column=a1)
#mylabels function will display values of predata and newdata array on GUI Screen.    
def mylabels():
    for a3 in range(10):
        #Displaying Data of array on GUI Screen
        if (int(newdata[a3]) == 1):
            pre3=Label(lblframe, text="OFF", font=("Calibri",12,"bold"), bg="white", fg="Green", borderwidth=1, relief="solid", padx=11, pady=1)
            pre3.grid(row=2, column=a3, sticky="nw")
        else:
            pre3=Label(lblframe, text="ON", font=("Calibri",12,"bold"), bg="white", fg="Red", borderwidth=1, relief="solid", padx=11, pady=1)
            pre3.grid(row=2, column=a3, sticky="nw")

lblframe.pack()

#Calling mylabel() function automatically when the GUI Screen is created. 
mylabels()

#Statuschanger function to change the status of array on GUI and in array
def statuschanger():
    #Clearing  array to store new values in it.
    newdata.clear()
    #Again Reading the Digital PINS of Arduino Board.
    data2 = arduinodata.readline()
    #Converting data of arduino Digital PINS from binary to string.
    seconddata=str(data2)
    #Storing Arduino data into arrays.
    j=2
    for a6 in range(10):
        newdata.append(seconddata[j])
        j=j+2
        #Calling mylabel function to Update Values on GUI Screen.
    mylabels()
    #Calling statuschanger again and again after every 100ms.
    win.after(100, statuschanger)

#Calling statuschanger() function automatically when the GUI Screen is created. 
statuschanger()

win.mainloop()
