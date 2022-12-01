import pyodbc, dbconnect


def pickTableNames():
    cnxn = dbconnect.dbconnection()

    cursor = cnxn.cursor()

    cursor.execute(
        "SELECT s.name AS SchemaName ,t.name AS TableName ,c.name AS ColumnName FROM sys.schemas AS s JOIN sys.tables AS t ON t.schema_id = s.schema_id JOIN sys.columns AS c ON c.object_id = t.object_id ORDER BY SchemaName ,TableName ,ColumnName;")
    rows = cursor.fetchall()

    tableNames = []
    count = 0

    for row in rows:
        if rows[count][1] not in tableNames:
            tableNames.append(rows[count][1])
        count += 1

    return tableNames


