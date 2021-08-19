import  pyodbc
try:
    conn_string = r'driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Imran m\OneDrive\Documents\malik.accdb;'
    conn= pyodbc.connect(conn_string)
    print("database Connected")
except pyodbc.Error as e:
    print("Error in Connection",e)

