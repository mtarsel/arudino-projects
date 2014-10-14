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
import datetime #for logging the timestamp
import time #for timestamp

arduino_serial_port='/dev/ttyACM0'

print "Opening serial port..."
ser = serial.Serial(arduino_serial_port,115200)

print "Reading from serial port..."

#read data forever
while True:

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #each temperature is split by a '\n' so lets use split() and parse it

        ser.readline()
        serial_data = ser.readline().split()

        print "timestamp, fernheit: ", st, " ", serial_data

ser.close()
print "Closed the serial port. Exiting."
