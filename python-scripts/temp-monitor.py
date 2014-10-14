import serial
#pip install pyserial
import os
import time
import sys

arduino_serial_port = "/dev/ttyACM0"
print "Opened serial port..."

ser = serial.Serial(arduino_serial_port,24000,timeout=0)
#ser = serial.Serial(arduino_serial_port,2400,timeout=10)


print "Reading from serial port..."
ser.readline()

sensor = ser.readline().split()

print "Entire sensor: ", sensor


print "sensor[0]: ", sensor[0]

print "sensor[1]: ", sensor[1]


ser.close()
print "Closed the serial port. Exiting."
