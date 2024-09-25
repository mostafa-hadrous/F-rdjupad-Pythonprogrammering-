import pandas as pd
import numpy as np
import scipy.stats as stats
from sqlalchemy import create_engine
import openpyxl as xlsx


engine = create_engine('mssql://LAPTOP-0CQU405Q/DS?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
connection = engine.connect()

df = pd.read_sql(sql="select * from [Employee Sample Data]", con=connection)
df

query_2 = """
select Country,
	   COUNT(country) as'Number of Employee',
		sum(Annual_Salary) as 'Total Annual Salaries',
		sum(Annual_Salary * Bonus)as 'Bonus'
	   from [Employee Sample Data]
	   where Exit_Date is null
	   group by (Country);
"""
df1 =pd.read_sql(query_2, con=connection)
df1

query_1 = """
select Department, 
		count(Department) as 'Number of Employees'
		from [Employee Sample Data]
		where Exit_Date is null
		group by(Department)
		order by ([Number of Employees]);
"""
df2 = pd.read_sql(query_1, con=connection)
df2

query_3= """
select year (Hire_Date) as 'Start year',
       count (Hire_Date) 'Number of Employee' 
	   from [Employee Sample Data]
	   group by year (Hire_Date)
	   order by year (Hire_Date);
"""
df3=pd.read_sql(query_3, con=connection)
df3

query_4= """select Gender,
	   COUNT(Gender) as 'Number of Gender'
	   from [Employee Sample Data]
       where Exit_Date is null
	   group by (Gender)"""
df4=pd.read_sql(query_4, con=connection)
df4


excel_file = pd.ExcelWriter('PySql Country Employee.xlsx')

df1.to_excel(excel_file, sheet_name= 'number of employee')
df2.to_excel(excel_file, sheet_name= 'Total Employees By Department')
df3.to_excel(excel_file, sheet_name= 'Hired Date  ')
df4.to_excel(excel_file, sheet_name= 'Male and Female Employee')

excel_file.close()


import logging

# Create a logger
logging.basicConfig(level=logging.INFO, filename='PySql logfile.log', filemode= 'a',
                    format='%(asctime)s: %(name)s : %(levelname)s : %(message)s : %(lineno)s',
                    datefmt='%Y-%m-%d %H:%M')

logger= logging.getLogger('Test logging ')

try:
    df4.to_excel(excel_file, sheet_name= 'Employee')
    excel_file.close()
except:
    logger.error(f'It is not allow to change the sheet name')

# Log messages

#logger.info("Program started")
#logger.debug("This is a debug message")
#logger.warning("This is a warning message")
#logger.error("This is an error message")
#logger.critical("This is a critical message")
#logger.info("Program finished")


# Import the 'unittest' module for writing unit tests.
import unittest
# Import the 'sqlite3' module for working with SQLite databases.
import sqlite3
# Define a test case class 'TestDatabaseConnection' that inherits from 'unittest.TestCase'.
class TestDatabaseConnection(unittest.TestCase):
    # Define a test method 'test_database_connection' to test database connection.
    def test_database_connection(self):
        # Create a database connection in memory.
        conn = connection
        # Execute a simple query to select the value 1.
        conn.execute("select * from [Employee Sample Data]")
        # Close the database connection.
        conn.close()
# Check if the script is run as the main program.
unittest.main(argv=[''], verbosity=2, exit=False)

