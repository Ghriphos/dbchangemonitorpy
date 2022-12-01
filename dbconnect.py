import pyodbc


def dbconnection():
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS08;DATABASE=SecullumAcessoNet;UID=sa;PWD=12we34rt')

    return cnxn
