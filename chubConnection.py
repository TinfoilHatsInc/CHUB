import smbus
import time
import storageHandler as sh
from random import randint

def auto_incr( _list):
    temp = 0
    if not _list:
        return 1
    else:
        for adr,sig in _list:
            if temp < adr:
                temp = adr
        return temp + 1

def compareHashes(hash1,hash2):
    for i in range(0,8):
        if hash1[i] != hash2[i]:
            return False    
    return True

class chubConnection:
    bus = smbus.SMBus(1)
    loginAddr = 127
    addressArr = []
    currentHash = [255,255,255,255,255,255,255,255]
    
    def __init__(self):
        pass

    def loginRequest(self):
        try:
            new_addr = auto_incr(self.addressArr)
            self.bus.write_byte_data(self.loginAddr, 128, new_addr)
            #time.sleep(1)
            sig = self.bus.read_byte(self.loginAddr)
            addr = self.loginResponse(self.currentHash,new_addr) 
            self.addressArr.append((addr,sig))
            print(self.addressArr)
            return sig
        except:
            print("no new module")
        return -1

    def loginResponse(self,sendHash, new_addr):
        self.bus.write_i2c_block_data(self.loginAddr, 127, sendHash)
        temp_addr = new_addr
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
        newhash = self.generateNewHash()
        for addr,sig in self.addressArr:
            myhash = self.isAliveRequest(addr)
            if compareHashes(self.currentHash,myhash):
                self.isAliveResponse(addr, newhash)
            else:
                sh.update_module(sig)
                self.addressArr.remove((addr,sig))
        self.currentHash = newhash
            

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
