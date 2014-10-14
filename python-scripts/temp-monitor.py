import serial
#pip install pyserial

def receiving(ser):
    print "inside receiving..."
    global last_received

    buffer = ''
    while True:
        buffer = buffer + ser.read(ser.inWaiting())
        if '\n' in buffer:
            lines = buffer.split('\n') # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            buffer = lines[-1]

arduino_serial_port="/dev/ttyACM0"

#ser.open()
#ser.isOpen()
print "Opening serial port..."
ser = serial.Serial(arduino_serial_port,24000,timeout=0)
#ser = serial.Serial(arduino_serial_port,2400,timeout=10)


print "Reading from serial port..."
#print ser.read()

receiving(ser)


#print "Entire sensor: ", sensor


#print "sensor[0]: ", sensor[0]

#print "sensor[1]: ", sensor[1]

# temperature = (((temperature - .5)*100)*1.8)+32;  //this line is for Fahrenheit                                             

ser.close()
print "Closed the serial port. Exiting."
