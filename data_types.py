def module(_id, _name, _type, _room, _alive):
    """Data structure for the modules"""
    return {"ID": _id, "Name":_name, "Type": _type, "Room":_room, "Alive": _alive}


def module_type(_id, _name):
    """Data structure for the module_types"""
    return {"ID":_id, "Name":_name}

def room(_id, _name):
    """Data structure for the rooms"""
    return {"ID":_id, "Name":_name}

def recording(_id, _event, _location):
    """Data structure for the recordings"""
    return {"ID":_id, "event":_event, "File_Location":_location}

def event(_id, _room, _datetime):
    """Data structure for the events"""
    return {"ID":_id, "Room": _room, "Date_Time":_datetime}

def config_override(_module, _name, _value):
    """Data structure for the overrides"""
    return {"module":_module, "Name":_name, "Value":_value}