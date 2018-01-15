import storageHandler as sh
import chubConnection as cc
import time



def create_module_from(_signature):
    modules = []
    modules.append({'name':'Siren','type':'Observer'})
    modules.append({'name':'Door','type':'Triggerer'})
    modules.append({'name':'Pressure','type':'Triggerer'})
    modules.append({'name':'Tripwire','type':'Triggerer'})
    modules.append({'name':'Motion','type':'Triggerer'})
	
	if _signature == 9:
		mod = modules[0]		 
    else:
		print(_signature)
		
    sh.add_module(mod['name'],1,mod['type'],_signature)


def main_loop():
    time_start = time.time()
	conn = cc.chubConnection()
    alive_counter = 300
    login_counter = 30
    test_counter = 0
    is_running = True
    
    alarm_latch = False
    while is_running:
        time_elapsed = time.time() - time_start
        if time_elapsed >= alive_counter:
            print("CHECK alive")
            conn.isAliveRequestAll()
            alive_counter += 300
        elif time_elapsed >= login_counter:
            sig = conn.loginRequest()
            if sig != -1:
				create_module_from(sig)
            login_counter += 30
        else:
            print("check whether the alarm is armed")
            if(sh.check_armed_status()):
				trig = conn.checkAlarmStatus()
				if trig != 0:
					sh.add_event(trig)
					#record and add location
					conn.alarmed()
					alarm_latch = True
			else:
				if alarm_latch:
					conn.dealarm()
					alarm_latch = False
            
        test_counter += 1
        if test_counter >= 660:
            is_running = False
        time.sleep(1)

