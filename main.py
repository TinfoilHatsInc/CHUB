import python_db_connection as pdbc
import data_types as dt
import json_serializer as js
import storageHandler as sh


temp = sh.read_file()
print(temp)
sh.update_event_status(1,2,True)
temp = sh.read_file()
print(temp)