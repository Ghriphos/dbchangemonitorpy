import controller, pyodbc, dbconnect


"def lineCount():"
cnxn = dbconnect.dbconnection()
tableNames = controller.pickTableNames()
cursor = cnxn.cursor()
count = 0
tableLinesCount = {}
for name in tableNames:
    cursor.execute(f"SELECT COUNT(*) FROM {tableNames[count]};")
    lengthTablesReturn = cursor.fetchall()
    trueLenght = lengthTablesReturn[0][0]
    for lines in tableNames:
        if tableNames[count] not in tableLinesCount:
            tableLinesCount[tableNames[count]] = trueLenght
    count += 1
print(tableLinesCount)

