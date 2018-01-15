import smbus
import time

bus = smbus.SMBus(1)


address = 0x04

def writeNumber(value):
    bus.write_i2c_block_data(address, 127, value)
    return -1

def readNumber():
    number = bus.read_i2c_block_data(address, 127)
    return number

while True:
    var = list()
    var.append(input("Enter 1 - 9: "))
    if not var:
        continue

    writeNumber(var)
    print "RPI: Hi Arduino, I sent you ", var
    time.sleep(2)

    number = readNumber()
    print "Arduino: Hey RPI, I received a digit ", number
    print
