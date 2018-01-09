import python_db_connection as pdbc
import data_types as dt
import json_serializer as js
import storageHandler as sh


temp = sh.read_file()
print(temp)
sh.add_module(3,'new module','Observer',1)

temp = sh.read_file()
print(temp)