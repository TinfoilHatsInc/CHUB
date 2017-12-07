import sqlite3 as sql

_db_name = 'CHUB.DB'

def __executeSingle(_message, _values):
	"""Handle Single line execution"""
	_conn = sql.connect(_db_name)
	_c = _conn.cursor()
	_c.execute(_message, _values)
	_conn.commit()
	_conn.close()

def __sortforupdate(_dict, _amount = 1):
	"""sort the dict into a list with ID last"""
	_list = []
	for key,value in _dict.items():
		_list.append(value)
	_list = _list[_amount:] +_list[:_amount]
	return _list



def insert_module(_module):
	"""Insert new module into database"""
	__executeSingle('INSERT INTO Module VALUES (?,?,?,?,?)', _module.values())

def update_model(_model):
	"""Update Exisiting Module in database"""
	__executeSingle('UPDATE Module SET Name=?,Type=?,Room=?,Alive=? WHERE ID=?',__sortforupdate(_model))



def insert_room(_room):
	"""Insert a new room into the database"""
	__executeSingle('INSERT INTO Room VALUES (?,?)', _room.values())

def update_room(_room):
	"""Update existing room in database"""
	__executeSingle('UPDATE Room SET Name=? WHERE ID=?',__sortforupdate(_room))



def insert_recording(_recording):
	"""Insert a new recording into the database"""
	__executeSingle('INSERT INTO Recording Values (?,?,?)',_recording.values())	

def update_recording(_recording):
	"""update existing recording in database"""
	__executeSingle('UPDATE Recording SET Event=?, File_Location=? WHERE ID=?',__sortforupdate(_recording))



def insert_event(_event):
	"""insert a new event into the database"""
	__executeSingle('INSERT INTO Recording VALUES (?,?,?)',_event.values())

def update_event(_event):
	"""update existing event in database"""
	__executeSingle('UPDATE Event SET Room=?, Date_Time=? WHERE ID=?',__sortforupdate(_event))



def insert_type(_type):
	"""Insert a new type into the database"""
	__executeSingle('INSERT INTO Type VALUES (?,?)', _type.values())

def update_type(_type):
	"""update existing type in database"""
	__executeSingle('UPDATE Type SET Name=? Where ID=?', __sortforupdate(_type))


def insert_override(_overide):
	"""Insert a new override into the database"""
	__executeSingle('INSERT INTO ConfigurationOverrides VALUES (?,?,?)', _overide.values())

def update_override(_override):
	"""update existing override in database"""
	__executeSingle('UPDATE ConfigurationOverrides SET Value=? WHERE Module=? AND Name =?', __sortforupdate(_override, 2))