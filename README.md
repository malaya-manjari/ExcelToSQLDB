# ExcelToSQLDB
Upload excel file data to MSSQL database
1. Install the required libraries:<br>
pip install pandas pyodbc openpyxl

2. Import the necessary libraries and establish a connection to the MSSQL database:<br>
import pandas as pd<br>
import pyodbc<br>
<br>
3. Create a connection string<br>
server = 'your_server_name'<br>
database = 'your_database_name'<br>
username = 'your_username'<br>
password = 'your_password'<br>
driver = '{Driver for SQL Server}'<br>
<br>
4. Read the Excel data using pandas library
