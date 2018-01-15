import storageHandler as sh
import time



def create_module_from(_signature):
    modules = []
    modules.append({'name':'Camera','type':'Observer'})
    modules.append({'name':'Siren','type':'Observer'})
    modules.append({'name':'Door','type':'Triggerer'})
    modules.append({'name':'Pressure','type':'Triggerer'})
    modules.append({'name':'Tripwire','type':'Triggerer'})
    modules.append({'name':'Motion','type':'Triggerer'})

    mod_id = _signature % 10000
    mod_info = _signature // 10000
    
    sh.add_module(modules[mod_info]['name']+str(mod_id),1,modules[mod_info]['type'],mod_id)


def main_loop():
    time_start = time.time()

    alive_counter = 300
    login_counter = 30
    test_counter = 0
    is_running = True
    while is_running:
        time_elapsed = time.time() - time_start
        if time_elapsed >= alive_counter:
            print("CHECK alive")
            print(time_elapsed)
            alive_counter += 300
        elif time_elapsed >= login_counter:
            print("login attempt")
            print(time_elapsed)
            login_counter += 30
        else:
            print("check whether the alarm is armed")
            if(sh.check_armed_status()):
                print("Check alarm status")
            
        test_counter += 1
        if test_counter >= 660:
            is_running = False
        time.sleep(1)

create_module_from(10000)

create_module_from(20000)

create_module_from(30000)
