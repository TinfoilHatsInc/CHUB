import smbus
import time

bus = smbus.SMBus(1)
loginAddr = 127
addressArr = []


def loginRequest(loginAddr):
    bus.write_byte_data(loginAddr, 128, len(addressArr) + 1)
    time.sleep(1)
#this returns the signature instead
    var = bus.read_byte(loginAddr)
    print(var)
def loginResponse(sendHash):
    bus.write_i2c_block_data(loginAddr, 127, sendHash)
    if bus.read_byte(1) == 200:
	addressArr.append(len(addressArr) + 1)
        print("login successfull")
	print(addressArr)


#TODO: rewrite return logic
def checkAlarmStatus():
    for addr in addressArr:
        try:
            bus.write_byte(addr, 125)
            if bus.read_byte(addr) == 1:
                print "alarm"
            else:
                print "no alarm"
        except:
            print("failure in statuscheck on: " + addr)

def isAliveRequest():
    for addr in addressArr:
	receivedHash = list()
        try:
            bus.write_byte(addr, 124)
            for x in range (0, 8):
		receivedHash.append(bus.read_byte(addr))
	    print(receivedHash)
        except Exception as e:
            print("exception in requesting isAlive")

def isAliveResponse(address, sendHash):
    try:
        bus.write_i2c_block_data(address, 123, sendHash)
    except Exception as e:
        print("failure in isAliveResponse")
	print e

def alarm(address):
    try:
        bus.write_byte(address, 122)
    except Exception as e:
        print("cant ring alarm")

def noAlarm(address):
    try:
	bus.write_byte(address, 121)
    except:
	print("alarm cant be reached")

loginRequest(loginAddr)
time.sleep(1)
loginResponse([123, 122, 5, 192, 168, 4, 201, 202])
time.sleep(1)
checkAlarmStatus()
time.sleep(1)
isAliveRequest()
time.sleep(1)
isAliveResponse(1, [1, 2, 10, 15, 166, 142, 200, 200])
time.sleep(1)
isAliveRequest()
time.sleep(1)
alarm(1)
time.sleep(1)
checkAlarmStatus()
time.sleep(10)
loginRequest(loginAddr)
time.sleep(1)
loginResponse([1,2,3,4,5,6,7,8])
