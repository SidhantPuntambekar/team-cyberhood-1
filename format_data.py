import sqlite3
import pandas as pd
import numpy as np

def analize():
	path = "Kismet-20200222-19-14-45-1.kismet"
	connection = sqlite3.connect(path)

	sql = "SELECT * FROM devices"

	df = pd.read_sql_query(sql, connection)
	total = len(df)

	return total
	
print(analize())