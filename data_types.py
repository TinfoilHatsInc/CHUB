def module(_id, _name, _type, _room, _alive):
    """Data structure for the modules"""
    return {"id": _id, "name":_name, "type": _type, "room":_room, "alive": _alive}


def module_type(_id, _name):
    """Data structure for the module_types"""
    return {"id":_id, "name":_name}

def room(_id, _name):
    """Data structure for the rooms"""
    return {"id":_id, "name":_name}

def recording(_id, _event, _location):
    """Data structure for the recordings"""
    return {"id":_id, "event":_event, "location":_location}

def event(_id, _name, _datetime):
    """Data structure for the events"""
    return {"id":_id, "name": _name, "datetime":_datetime}

def config_override(_module, _name, _value):
    """Data structure for the overrides"""
    return {"module":_module, "name":_name, "value":_value}