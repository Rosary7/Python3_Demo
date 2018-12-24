"""
Accessing Oracle:
'cx_Oracle' is a Python extension module that allows access to Oracle databases.
To access oracle from python, we have to install both Oracle Driver and Python Driver.

Pre-requisite:
1) Install Oracle Driver:
This can be done in 2 ways-
    i)Copy 'C:\oraclexe\app\oracle\product\11.2.0\server\jdbc\lib\ojdbc6.jar' into "C:\Java\jdk1.8.0_131\jre\lib\ext"
    (or)
    ii) Download the 'Oracle 12 instant client',unzip to "c:\Oracle\" and set path.
    set ORACLE_HOME=C:\your\path\to\instantclient_11_2
    set PATH=%ORACLE_HOME%;%PATH%
2) Install 'cx_Oracle' which is Python’s Driver:
ie: pip install cx_Oracle

"""
# Simple code to access Oracle
import cx_Oracle

try:
    #dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')
    #conn = cx_Oracle.connect(user='system', password='xyz', dsn=dsn_tns)

    # Syntax: connection = cx_Oracle.connect('user_name/password@host_name/service_name')
    conn = cx_Oracle.connect('system/xyz@localhost/xe')

    cur = conn.cursor()
    resultSet = cur.execute('select * from emp')
    for record in resultSet:
        print(record)
except cx_Oracle.DatabaseError as de:
    print('Database connection error:', de)
finally:
    if conn is not None:
        conn.close()
