import pandas as pd
import pyodbc

# SET DB parameters
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'

# Set the MSSQL database table
table_name = 'your_table_name'

def getDbCon():
    conn_str = (
        r'DRIVER=' + driver +
        r';SERVER=' + server +
        r';DATABASE=' + database +
        r';UID=' + username +
        r';PWD=' + password
    )
    # Create a connection
    conn = pyodbc.connect(conn_str)
    return conn

# Read the Excel file
def readExcelInputs():
    excel_file = input("Please provide your excel file path")
    sheet_name = input("Please provide sheetname")
    return excel_file, sheet_name

if __name__ == "__main__":
    connect = getDbCon()
    excel_file, sheet_name = readExcelInputs()
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    df.to_sql(table_name, connect, if_exists='replace', index=False)
    
    # Close the connection
    connect.close()
