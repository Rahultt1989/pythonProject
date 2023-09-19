import serial
import os
import pyttsx3

serialPort = serial.Serial(port="COM4", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)   # Initiate UART with  Baud rate 9600

serialString = ""    #Buffer to hold UART data

while 1:

    if serialPort.in_waiting > 0:    # wait for th string to receive.

        serialString = serialPort.readline()     # take the received string into our buffer.
        print(serialString.decode('Ascii'))
        pyttsx3.speak('Shutting down PC in 10 seconds')
        if serialString.decode('Ascii') == "ShutDown":     # check the received string and shut down if it is "ShutDown"
            print("Shutting down")
            os.system('shutdown /s /t 10')    # shut down in 10 seconds.
            pyttsx3.speak('Command received, Shutting down PC in 10 seconds')    # to get voice alert before shut down


