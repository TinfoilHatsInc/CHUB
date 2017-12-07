import sqlite3 as sql

_db_name = 'CHUB.DB'



def insert_module(module):
	"""Insert new module into database"""
	_conn = sql.connect(_db_name)
	_c = _conn.cursor()
	_c.execute('INSERT INTO Module VALUES (?,?,?,?,?)', module.values())
	_conn.commit()
	_conn.close()
