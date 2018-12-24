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
# Various Oracle exception code
import cx_Oracle

CONN_INFO = {
    'host': 'localhost',
    'port': 1521,
    'user': 'system',
    'psw': 'mpp',
    'service': 'xe'
}

CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)
QUERY = ' SELECT * FROM EMP  WHERE EMPNAME = :name'

class DB:
    def __init__(self):
        self.conn = cx_Oracle.connect(CONN_STR)

    def myquery(self, query, params=None):
        try:
            my_cursor = self.conn.cursor()
            my_result = my_cursor.execute(query, params).fetchall()
            return my_result
        except cx_Oracle.DatabaseError as de:
            print("Oracle exception............: ", de)
        finally:
            my_cursor.close()

if __name__ == "__main__":
    try:
        print("Entering try()")
        db = DB()  # Exception created here if db connection details are wrong
        result = db.myquery(QUERY, {'name': 'Peter'})
        print(result)
    except cx_Oracle.DatabaseError as de:
        de_error, = de.args # In Python, it's the comma that makes something a tuple. ie: 'de_error,'
        if de_error.code == 12541:
            print("Oracle exception. Check Oracle 'ojdbc6' driver/service name/port etc.: ", de)
            print(de_error.message)
            print(de_error.context)
        elif de_error.code == 1017:
            print('Check your credentials.')
        elif de_error.code == 1146:
            print("Insufficient privileges")
        else:
            print('Database connection error: %s'.format(de_error))

