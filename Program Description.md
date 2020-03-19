# Digital-Pin-Status
The Program reads Digital PINS of Arduino UNO with Python Tkinter and Display on GUI Screen. 

# Working of Arduino UNO in Python Program:
Serial Method is used to read the Digital PINS of Arduino and then the values are stored into an array namely newdata. Then after using it once the array is cleared and stored the next data is read again from Arduino and then displayed it on GUI Screen. This Process Continous...

# Working of Python Tkinter:
With python Tkinter first, the Heading is Displayed, then a Row of Labels is Displayed below the heading that Displays the DIGITAL PINS heading as PIN0, PIN1, PIN2, etc.

Then in the next row "ON" and "OFF" text is showed that represents the states of the Arduino Board. If a PIN is ON it sends "1" as output. That output is stored in newdata Array and Finally, if the index of the array contains "1" it shows "ON" on GUI Screen. Similarly, if array Contains "0" it shows "OFF" on output Screen.
