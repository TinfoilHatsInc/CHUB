import json
import data_types
import datetime



def data_to_json(_rooms):
    return json.dumps(_rooms, indent=2)

def json_to_data(_json):
    return json.loads(_json)

def write_file(_rooms):
    file = open("/home/jona/TinfoilHats/CHUB/storage.json","w")
    file.write(data_to_json(_rooms))
    file.close()
    
def read_file():
    file = open("/home/jona/TinfoilHats/CHUB/storage.json","r")
    temp = json_to_data(file.read())
    return temp

def __auto_increment(_list):
    temp = 0
    if not _list:
        return 1
    else:
        for i in _list:
            if temp < i['ID']:
                temp = i['ID']
        return temp + 1


def add_module(_id, _name, _alive, _type, _room = 0):
    temp = read_file()
    for room in temp:
        if _room == room['ID']:
            room['Modules'].append(data_types.module_jsn(_id,_name,_alive,_type))
    write_file(temp)

def add_event(_triggerer):
    temp = read_file()
    temp_id = 0
    for room in temp:
        for module in room['Modules']:
            if module['ID'] == _triggerer:
                temp_id = __auto_increment(room['Events'])
                room['Events'].append(data_types.event_jsn(temp_id, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),[]))
    write_file(temp)
    return temp_id

def update_event_status(_event_id,_room_id,_importance):
    temp = read_file()
    for room in temp:
        if room['ID'] == _room_id:
            for event in room['Events']:
                if event['ID'] == _event_id:
                    event['Important'] = _importance
    write_file(temp)

def add_recording(_event_id, _location):
    temp = read_file()
    for room in temp:
        for event in room['Events']:
            if _event_id == event['ID']:
                event['Recordings'].append(data_types.recording_jsn(__auto_increment(event['Recordings']),_location))
    write_file(temp)

def add_room(_name):
    temp = read_file()
    temp.append(data_types.room_jsn(__auto_increment(temp),_name,[],[]))
    write_file(temp)

def move_module(_module_id,_room_id):
    temp = read_file()
    temp_mod = 0
    for room in temp:
        for module in room['Modules']:
            if module['ID'] == _module_id:
                temp_mod = module
                room['Modules'].remove(module)
    write_file(temp)
    add_module(temp_mod['ID'],temp_mod['Name'],temp_mod['Type'], temp_mod['Alive'],_room_id)


def send_to_front_end():
    return read_file()