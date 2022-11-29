import pyodbc

cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS08;DATABASE=test;UID=sa;PWD=12we34rt')

cursor = cnxn.cursor()

cursor.execute("select * from users")
rows = cursor.fetchall()

rowsCount = len(rows)

for row in rows:
    print(row)

print(rowsCount)
