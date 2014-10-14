#
#   Author:
#       Mick Tarsel
#
# The code below was tested with the Arduino UNO board and TMP36 Temperature Sensor
#
#   This will read from the serial port with an arduino and parse the import.
#


import csv
import serial
#pip install pyserial
import datetime
import time

arduino_serial_port='/dev/ttyACM0'
csv_file = 'temperature.csv'


timestamp_temp={}

print "Opening serial port..."
ser = serial.Serial(arduino_serial_port,9600)

print "Reading from serial port..."
#print ser.readline()

#read data forever
while True:


        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #each temperature is split by a '\n' so lets use split() and parse it

        print "timestamp, temperature: ", st, " ", ser.readline().split()


        #store it in a dictionary for anarchy
       # timestamp_temp[st] = ser.readline().split()

        #print timestamp_temp

ser.close()
print "Closed the serial port. Exiting."
