import serial
import time
from tkinter import *
import struct
import csv


ser = serial.Serial('COM3', baudrate = 9600, timeout=1)
time.sleep(3)
if(ser.isOpen() == True):
    print('port is Open')
if(ser.isOpen() == False):
    print('Port is closed')


#Read dat ALWAYS FUNCTION
def serialConnection():
    ser.write(b'S')
    actualCounterData = ser.readline()
    actualValue = struct.unpack('h', actualCounterData)
    liveCounter.set(actualValue)


# Close window function
def close_window (): 

    root.destroy()

#Start Button Function
def getData():
    ser.write(b'C')
    CounterData = ser.readline()
    # counterValue =struct.unpack('h', CounterData) #https://www.delftstack.com/howto/python/how-to-convert-bytes-to-integers/
    print(str(CounterData[0]))
    # liveCounter.set(counterValue)


#Counter delete function
def delCounter():
    ser.write(b'R')
    CounterData = ser.readline(8)
    counterValue =struct.unpack('h', CounterData)
    #CounterData = ser.readline(24).decode().split('\r\n')
    #return CounterData(0)
    print(counterValue[0])

# write to csv file
def wrtieToFile():
    # header = ['Date', 'Time', 'Counter']
    pass


#Print the Results

def printFile():
    pass


root = Tk()

start_button = Button(root, text='Start', command=getData)
start_button.pack()
del_button = Button(root, text='Clear', command=delCounter)
del_button.pack()
close_button = Button(root, text='Quit', command=close_window)
close_button.pack()

#create a display window

liveCounter =StringVar()
liveCounter.set('Counter')

#create the label
result_label = Label(root, textvariable=liveCounter)
result_label.pack()
result_label.config(font='Ubuntu 18')

root.mainloop()