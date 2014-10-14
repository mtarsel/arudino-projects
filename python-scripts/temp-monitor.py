import serial
#pip install pyserial
import os
import time
import sys
#import MySQLdb #not needed at this time

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

#def getData():
#        sensor = ser.readline().split()
#        print sensor[0]
#        print sensor[1]
#        conn = MySQLdb.connect (host = "localhost", user = "user", passwd = "password", db = "db_name")
#        cursor = conn.cursor ()

 #       command = "INSERT INTO `monitor`.`data` (`id`, `sensor_id`, `time`, `temp`) VALUES (NULL, '%s', CURRENT_TIMESTAMP, '%s');" % (sensor[0], sensor[1])
 #       cursor.execute(command);
 #       cursor.close ()
  #      conn.close ()
#        return



#for i in range(5):
#        getData()

ser.close()
print "Closed the serial port"


#getData for all sensors
#writeToDataBase(sensor, temp)
