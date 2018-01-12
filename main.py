import storageHandler as sh
import time

time_start = time.time()

alive_counter = 300
login_counter = 30
test_counter = 0
is_running = True
while is_running:
    time_elapsed = time.time() - time_start
    #alarmstatus
    if time_elapsed >= alive_counter:
        print("CHECK alive")
        print(time_elapsed)
        alive_counter += 300
    elif time_elapsed >= login_counter:
        print("login attempt")
        print(time_elapsed)
        login_counter += 30
    else:
        print("Check alarm status")
        
    test_counter += 1
    if test_counter >= 1500:
        is_running = False
    time.sleep(1)



"""
print(time_active)
temp = sh.read_file()
print(temp)"""