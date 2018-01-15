import smbus
import time
from random import randint

class chubConnection:
    bus = smbus.SMBus(1)
    loginAddr = 127
    addressArr = []
    currentHash = [255,255,255,255,255,255,255,255]
    
    def __init__(self):
        pass

    def loginRequest(self):
        try:
            self.bus.write_byte_data(self.loginAddr, 128, len(self.addressArr) + 1)
            #time.sleep(1)
            sig = self.bus.read_byte(self.loginAddr)
            addr = self.loginResponse(self.currentHash) 
            self.addressArr.append((addr,sig))
            print(self.addressArr)
            return sig
        except:
            print("no new module")
        return -1

    def loginResponse(self,sendHash):
        self.bus.write_i2c_block_data(self.loginAddr, 127, sendHash)
        temp_addr = len(self.addressArr) + 1
        if self.bus.read_byte(temp_addr) == 200:
            print("login successfull")
            return temp_addr



    def checkAlarmStatus(self):
        for addr,sig in self.addressArr:
            try:
                self.bus.write_byte(addr, 125)
                if self.bus.read_byte(addr) == 1:
                    print("alarm")
                    self.alarmed()
                    return sig                
            except:
                print("failure in statuscheck on: " + str(addr))
        return 0

    def isAliveRequestAll(self):
        for addr,sig in self.addressArr:
            self.isAliveRequest(addr)
            self.currentHash = self.generateNewHash()
            self.isAliveResponse(addr, self.currentHash)
            
            

    def generateNewHash(self):
        tempHash = []
        for x in range(0,8):
            tempHash.append(randint(0,255))
        return tempHash

    def isAliveRequest(self, addr):
        receivedHash = []
        try:
            self.bus.write_byte(addr, 124)
            for x in range (0, 8):
                receivedHash.append(self.bus.read_byte(addr))
            print(receivedHash)
        except Exception as e:
            print("exception in requesting isAlive")
        return receivedHash


    def isAliveResponse(self,address, sendHash):
        try:
            self.bus.write_i2c_block_data(address, 123, sendHash)
            print("sent this hash")
            print(sendHash)
        except Exception as e:
            print("failure in isAliveResponse")
            print(e)

    def alarmed(self):
        for addr,sig in self.addressArr:
            self.alarm(addr)
            
    def alarm(self,address):
        try:
            self.bus.write_byte(address, 122)
        except Exception as e:
            print("cant ring alarm")

    def dealarm(self):
        for addr,sig in self.addressArr:
            self.noAlarm(addr)

    def noAlarm(self, address):
        try:
            self.bus.write_byte(address, 121)
        except:
            print("alarm cant be reached")
