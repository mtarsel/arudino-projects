import serial
#pip install pyserial
import time


#ser = serial.Serial(
#    port = "/dev/ttyACM0",
#   baudrate = 9600,
#    parity=serial.PARITY_ODD,
#    stopbits=serial.STOPBITS_TWO,
#    bytesize=serial.SEVENBITS
#)

#ser.open()
#ser.isOpen()
print "Opened serial port..."

print ser.readline()
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
