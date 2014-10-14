#
#   Author:
#       Mick Tarsel
#
# The code below was tested with the Arduino UNO board and TMP36 Temperature Sensor
#
#   This will read from the serial port with an arduino and parse the import.
#
#
#
#



import serial
#pip install pyserial

arduino_serial_port='/dev/ttyACM0'

print "Opening serial port..."
ser = serial.Serial(arduino_serial_port,9600)

print "Reading from serial port..."
#print ser.readline()

#read data forever
while True:

    #each temperature is split by a '\n' so lets use split() and parse it
    print ser.readline().split()

ser.close()
print "Closed the serial port. Exiting."
