"""**********Database Data Types**********"""

def module_db(_id, _name, _type, _room, _alive):
    """Data structure for the modules"""
    return {"ID": _id, "Name":_name, "Type": _type, "Room":_room, "Alive": _alive}

def type_db(_id, _name):
    """Data structure for the module_types"""
    return {"ID":_id, "Name":_name}

def room_db(_id, _name):
    """Data structure for the rooms"""
    return {"ID":_id, "Name":_name}

def recording_db(_id, _event, _location):
    """Data structure for the recordings"""
    return {"ID":_id, "event":_event, "File_Location":_location}

def event_db(_id, _room, _datetime):
    """Data structure for the events"""
    return {"ID":_id, "Room": _room, "Date_Time":_datetime}

def config_override_db(_module, _name, _value):
    """Data structure for the overrides"""
    return {"Module":_module, "Name":_name, "Value":_value}

"""**********Json Data Types**********"""

def recording_jsn(_id,_location):
    return {"ID":_id, "File_Location":_location}

def config_override_jsn(_name, _value):
    return {"Name":_name, "Value": _value}

def module_jsn(_id, _name, _type,_alive, _override = "None"):
    return {"ID": _id, "Name":_name, "Type": _type, "Alive": _alive, "Override": _override}

def event_jsn(_id, _datetime, _recordings):
    return {"ID":_id,"Datetime":_datetime,"Recordings":_recordings}

def room_jsn(_id, _name, _modules, _events):
    return {"ID": _id, "Name": _name, "Modules": _modules,"Events": _events}

