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
csv_file = "tempData.csv"


print "Opening serial port..."
ser = serial.Serial(arduino_serial_port,115200)

print "Opening csv file..."
csv_object = open(csv_file, "wb")

print "Reading from serial port..."

#read data forever
while True:

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #each temperature is split by a '\n' so lets use split() and parse it

        ser.readline()
        serial_data = ser.readline().split()

        str_serial_data = ', '.join(serial_data)


        print "timestamp, fernheit: ", st, " ", str_serial_data

        csv_object.write( st);
        csv_object.write( ",");
        csv_object.write( str_serial_data);
        csv_object.write( "\n");


ser.close()
# Close opend file
csv_object.close()
print "Closed the serial port. Exiting."
