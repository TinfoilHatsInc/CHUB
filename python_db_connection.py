import sqlite3 as sql

db_name = 'CHUB.DB'

def Module(id,name,type,room,alive):
	return (id,name,type,room,alive)


def new_module(module):
	conn = sql.connect(db_name)
	c = conn.cursor()
	c.execute('INSERT INTO Module VALUES (?,?,?,?,?)', module)
	conn.commit()
	conn.close()
