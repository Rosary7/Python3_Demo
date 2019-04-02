"""
Accessing MySql using "pymysql" driver:
1)PyMySQL is an interface for connecting to a MySQL db from Python.
2)It implements the Python Database API v2.0 and contains a pure-Python MySQL client library.
3)The goal of PyMySQL is to be a drop-in replacement for MySQLdb.

Pre-requisite:
  C:\Program Files\Python 3.5\Lib>pip install pymysql
"""

# MySql - Check db version
import pymysql

con = None
try:
     # open db connection
     #con = pymysql.connect(<host>,<userName>,<password>,<db_name>)
     con = pymysql.connect("localhost","root","root","poc_db")
     # create a db cursor object
     cursor = con.cursor()
     # execute SQL query
     cursor.execute("SELECT VERSION()")
     # Retrieve a single row
     data = cursor.fetchone()
     print ("DB version : %s " % data)

except pymysql.err.OperationalError as oe:
    print('Credentials error:', oe)
except pymysql.err.InternalError as ie:
    print('Database  error:', ie)
except Exception as e:
    print('General  error:', e)
finally:
    if con is not None:
        con.close()

