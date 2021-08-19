import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Imran m\OneDrive\Documents\python.accdb;')
print("Connect Sucessfully")
cursor = conn.cursor()
cursor.execute('select * from Record')

for row in cursor.fetchall():
    print(row)