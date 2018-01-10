import python_db_connection as pdbc
import data_types as dt
import json_serializer as js
import storageHandler as sh


temp = sh.read_file()
print(temp)
sh.move_module(1,2)
temp = sh.read_file()
print(temp)