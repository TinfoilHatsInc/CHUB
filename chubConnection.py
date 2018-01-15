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

	def loginRequest():
		try:
			bus.write_byte_data(loginAddr, 128, len(addressArr) + 1)
			#time.sleep(1)
			sig = bus.read_byte(loginAddr)
			addr = loginResponse(currentHash) 
			addressArr.append((addr,sig))
			print(addressArr)
			return sig
		except:
			print("no new module")
		return -1;

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
					alarmed()
					return sig				
			except:
				print("failure in statuscheck on: " + str(addr))
		return 0

	def isAliveRequestAll():
		for addr,sig in addressArr:
			isAliveRequest(addr)
			currentHash = generateNewHash()
			isAliveResponse(addr, currentHash)
			
			

	def generateNewHash():
		tempHash = []
		for x in range(0,8):
			tempHash.append(randint(0,255))
		return tempHash

	def isAliveRequest(addr):
		receivedHash = []
		try:
			bus.write_byte(addr, 124)
			for x in range (0, 8):
				receivedHash.append(bus.read_byte(addr))
			print(receivedHash)
		except Exception as e:
			print("exception in requesting isAlive")
		return receivedHash


	def isAliveResponse(address, sendHash):
		try:
			bus.write_i2c_block_data(address, 123, sendHash)
			print("sent this hash")
			print(sendHash)
		except Exception as e:
			print("failure in isAliveResponse")
			print e

	def alarmed():
		for addr,sig in addressArr:
			alarm(addr)
			
	def alarm(address):
		try:
			bus.write_byte(address, 122)
		except Exception as e:
			print("cant ring alarm")

	def dealarm():
		for addr,sig in addressArr:
			noAlarm(addr)

	def noAlarm(address):
		try:
			bus.write_byte(address, 121)
		except:
			print("alarm cant be reached")
