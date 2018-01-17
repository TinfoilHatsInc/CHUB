import storageHandler as sh
import chubConnection as cc
import time
import camera_recording as cr


def create_module_from(_signature):
    modules = []
    modules.append({'name':'Siren','type':'Observer'})
    modules.append({'name':'Door','type':'Triggerer'})
    modules.append({'name':'Pressure','type':'Triggerer'})
    modules.append({'name':'Tripwire','type':'Triggerer'})
    modules.append({'name':'Motion','type':'Triggerer'})
    
    if _signature == 192:
        mod = modules[2]
    elif _signature == 128:
		mod = modules[4]
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
                    if not alarm_latch:
                        tempid = sh.add_event(trig)
                        sh.add_recording(tempid, cr.recordnow())
                    conn.alarmed()
                    alarm_latch = True
            else:
                if alarm_latch:
                    conn.dealarm()
                    alarm_latch = False
            
        test_counter += 1
        if test_counter >= 1500:
            is_running = False
        time.sleep(1)

main_loop()
