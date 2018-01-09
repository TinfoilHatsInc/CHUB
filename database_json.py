
"""
this is currently underconstruction and might be removed
def __combine_all_data():
    rooms = []
    db_mods = dbcon.get_all_modules()
    db_eves = dbcon.get_all_events()
    db_rooms = dbcon.get_all_rooms()
    for room in db_rooms:
        temp_mods = []
        temp_events = []
        for mod in db_mods:
            if mod["Room"] == room["ID"]:
                temp_mods.append(mod)
        for eve in db_eves:
            if eve["Room"] == room["ID"]:
                temp_events.append(eve)
        modules = __combine_modules(temp_mods, dbcon.get_all_types(), dbcon.get_all_overrides())
        events = __combine_events(temp_events, dbcon.get_all_recordings)
        rooms.append(dt.room_jsn(room["ID"],room["Name"],modules,events))
    return rooms

def __combine_modules(_modules, _types, _overrides):
    modules = []
    for mod in _modules:
        temp_type = ""
        temp_over = []
        for typ in _types:
            if typ["ID"]==mod["Type"]:
                temp_type = typ
        for over in _overrides:
            if over["Module"] == mod["ID"]:
                temp_over.append(dt.config_override_jsn(over["Name"], over["Value"]))
        modules.append(dt.module_jsn(mod["ID"], mod["Name"], temp_type,mod["Alive"],temp_over))
    return modules

def __combine_events(_events, _recordings):   
    events = []
    for eve in _events:
        temp_rec = []
        for rec in _recordings:
            if eve["ID"] == rec["event"]:
                temp_rec.append(dt.recording_jsn(rec["ID"],rec["File_Location"]))
        events.append(dt.event_jsn(eve["ID"],eve["Date_Time"],temp_rec))
    return events

def data_to_json():
    return json.dumps(__combine_all_data(), indent=2)

def json_to_data(_json):
    return json.loads(_json)
"""