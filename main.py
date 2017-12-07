import python_db_connection as pdbc
import data_types as dt

temp_module = dt.module(1,'somethingelse',1,0,1)

print(temp_module.values())
pdbc.update_model(temp_module)
