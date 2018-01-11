import smbus

bus = smbus.SMBus(1)
loginAddr = 0x7F
addressArr = []


def login(loginAddr, sendHash):
    try:
        bus.read_byte(loginAddr)
        print(hex(loginAddr))
        bus.write_byte_data(loginAddr, 128, len(addressArr) + 1)

        if bus.read_byte(loginAddr) == 200:
            bus.write_i2c_block_data(loginAddr, 127, sendHash)
            if bus.read_byte(loginAddr) == 200:
                print("login successfull")
    except:
        print("no active login needed")




def checkStatus():
    for addr in addressArr:
        try:
            bus.write_byte(addr, 125)
            if bus.read_byte(addr) == 1:
                return 1
            else
                return 0
        except:
            print("failure in statuscheck on: " + addr)

def isAliveRequest():
    for addr in addressArr:
        try:
            bus.write_byte(addr, 124)
            return (bus.read_i2c_bloc_data(addr, 124), addr)
        except Exception as e:
            print("exception in requesting isAlive")

def isAliveResponse(address ,sendHash):
    try:
        bus.write_i2c_block_data(addr, 123, sendHash)
    except:
        print("failure in isAliveResponse")
