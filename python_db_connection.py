import sqlite3 as sql
import data_types as dt

_db_name = 'CHUB.DB'

def __executePush(_message, _values):
	"""Handle Single line execution"""
	_conn = sql.connect(_db_name)
	_c = _conn.cursor()
	_c.execute(_message, _values)
	_conn.commit()
	_conn.close()

def __executePull(_message):
	_conn = sql.connect(_db_name)
	_c = _conn.cursor()
	temp = []
	for mod in _c.execute(_message):
		temp.append(mod)
	_conn.close()
	return temp

def __sortforupdate(_dict, _amount = 1):
	"""sort the dict into a list with ID last"""
	_list = []
	for key,value in _dict.items():
		_list.append(value)
	_list = _list[_amount:] +_list[:_amount]
	return _list


def insert_module(_module):
	"""Insert new module into database"""
	__executePush('INSERT INTO Module VALUES (?,?,?,?,?)', _module.values())

def update_model(_model):
	"""Update Exisiting Module in database"""
	__executePush('UPDATE Module SET Name=?,Type=?,Room=?,Alive=? WHERE ID=?',__sortforupdate(_model))

def get_all_modules():
	"""Retrieve all modules in the database"""
	temp = __executePull('SELECT * FROM Module')
	modules = []
	for mod in temp:
		modules.append(dt.module_db(mod[0],mod[1],mod[2],mod[3],mod[4]))
	return modules


def insert_room(_room):
	"""Insert a new room into the database"""
	__executePush('INSERT INTO Room VALUES (?,?)', _room.values())

def update_room(_room):
	"""Update existing room in database"""
	__executePush('UPDATE Room SET Name=? WHERE ID=?',__sortforupdate(_room))

def get_all_rooms():
	"""Retrieve all rooms in the database"""
	temp = __executePull('SELECT * FROM Room')
	rooms = []
	for rom in temp:
		rooms.append(dt.room_db(rom[0],rom[1]))
	return rooms


def insert_recording(_recording):
	"""Insert a new recording into the database"""
	__executePush('INSERT INTO Recording Values (?,?,?)',_recording.values())	

def update_recording(_recording):
	"""update existing recording in database"""
	__executePush('UPDATE Recording SET Event=?, File_Location=? WHERE ID=?',__sortforupdate(_recording))

def get_all_recordings():
	"""retrieve all recordings in the database"""
	temp = __executePull('SELECT * FROM Recording')
	recordings = []
	for rec in temp:
		recordings.append(dt.recording_db(rec[0], rec[1], rec[2]))
	return recordings



def insert_event(_event):
	"""insert a new event into the database"""
	__executePush('INSERT INTO Recording VALUES (?,?,?)',_event.values())

def update_event(_event):
	"""update existing event in database"""
	__executePush('UPDATE Event SET Room=?, Date_Time=? WHERE ID=?',__sortforupdate(_event))

def get_all_events():
	"""retrieves all events in database"""
	temp = __executePull('SELECT * FROM Event')
	events = []
	for eve in temp:
		events.append(dt.event_db(eve[0], eve[1], eve[2]))
	return events



def insert_type(_type):
	"""Insert a new type into the database"""
	__executePush('INSERT INTO Type VALUES (?,?)', _type.values())

def update_type(_type):
	"""update existing type in database"""
	__executePush('UPDATE Type SET Name=? Where ID=?', __sortforupdate(_type))

def get_all_types():
	"""retrieve all types in the database"""
	temp = __executePull('SELECT * FROM Type')
	types = []
	for typ in temp:
		types.append(dt.type_db(typ[0], typ[1]))
	return types

def insert_override(_overide):
	"""Insert a new override into the database"""
	__executePush('INSERT INTO ConfigurationOverrides VALUES (?,?,?)', _overide.values())

def update_override(_override):
	"""update existing override in database"""
	__executePush('UPDATE ConfigurationOverrides SET Value=? WHERE Module=? AND Name =?', __sortforupdate(_override, 2))

def get_all_overrides():
	"""retrieve all overrides in the database"""
	temp = __executePull('SELECT * FROM ConfigurationOverrides')
	overrides = []
	for over in temp:
		overrides.append(dt.config_override_db(over[0], over[1], over[2]))
	return overrides