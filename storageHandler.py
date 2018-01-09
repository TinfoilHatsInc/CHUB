import json
import data_types


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

def add_module(_id, _name, _alive, _type, _room = 0):
    temp = read_file()
    for room in temp:
        if _room == room['ID']:
            room['Modules'].append(data_types.module_jsn(_id,_name,_alive,_type))
    write_file(temp)

def add_event(_id,_triggerer):
    temp read_file()
    for room in temp:
        for module in room['Modules']:
            if module['ID'] == _triggerer:
                room['Events'].append(data_types.event_jsn(_id, _date_time,[]))
    write_file(temp)
    return _id

def send_to_front_end():
    return read_file()