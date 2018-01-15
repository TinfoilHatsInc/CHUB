import smbus
import time

bus = smbus.SMBus(1)
loginAddr = 127
addressArr = []
currentHash = [255,255,255,255,255,255,255,255]

def loginRequest(loginAddr):
    try:
        bus.write_byte_data(loginAddr, 128, len(addressArr) + 1)
        #time.sleep(1)
        sig = bus.read_byte(loginAddr)
        addr = loginResponse(currentHash) 
        addressArr.append((addr,sig))
        print(addressArr)
    except:
        print("no new module")

def loginResponse(sendHash):
    bus.write_i2c_block_data(loginAddr, 127, sendHash)
    temp_addr = len(addressArr) + 1
    if bus.read_byte(temp_addr) == 200:
        print("login successfull")
        return temp_addr



def checkAlarmStatus():
    for addr,sig in addressArr:
        try:
            bus.write_byte(addr, 125)
            if bus.read_byte(addr) == 1:
                print("alarm")
            else:
                print("no alarm")

        except:
            print("failure in statuscheck on: " + addr)

def isAliveRequest():
    for addr,sig in addressArr:
        receivedHash = []
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
print("next device small test")
time.sleep(30)
loginRequest(loginAddr)
time.sleep(1)
loginResponse([1, 2, 3, 4, 5, 6, 7, 8])
time.sleep(1)
checkAlarmStatus()
