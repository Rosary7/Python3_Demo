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
    set ORACLE_HOME=C:\Oracle\instantclient_11_2
    set PATH=%ORACLE_HOME%;%PATH%
2) Install 'cx_Oracle' which is Python’s Driver:
ie: pip install cx_Oracle

"""

# Oracle CRUD example
import cx_Oracle

class DB:
    def __init__(self):
        #dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')
        #self.__oracleConnection = cx_Oracle.connect(user='system', password='mpp', dsn=dsn_tns)

        self.__oracleConnection = cx_Oracle.connect('system/mpp@localhost/xe')

    def createTable(self):
        """ DDL """
        try:
            oracleCursor = self.__oracleConnection.cursor()
            oracleCursor.execute("CREATE TABLE EMP (empNo INTEGER not NULL PRIMARY KEY, empName VARCHAR(255), empAddress VARCHAR(255))")
            oracleCursor.execute('COMMIT') # Commit
            print('Table created.')
            print()
        except cx_Oracle.DatabaseError as de:
            print("Oracle exception............: ", de)
            print()
        finally:
            oracleCursor.close

    def insertData(self):
        """ DML """
        try:
            oracleCursor = self.__oracleConnection.cursor()
            oracleCursor.execute("INSERT INTO EMP (empNo, empName, empAddress) VALUES(600, 'Arun', 'US')")
            oracleCursor.execute('COMMIT') # Commit
            print('1 row inserted.')
            print()
        except cx_Oracle.DatabaseError as de:
            print("Oracle exception............: ", de)
            print()
        finally:
            oracleCursor.close

    def readAllData(self):
        """ DML """
        try:
            oracleCursor = self.__oracleConnection.cursor()
            resultSet = oracleCursor.execute('select * from emp')
            for record in resultSet:
                print(record)
            print()
        except cx_Oracle.DatabaseError as de:
            print("Oracle exception............: ", de)
            print()
        finally:
            oracleCursor.close

    def readOneRow(self, params):
        """ DML """
        print('Read one row:')
        try:
            oracleCursor = self.__oracleConnection.cursor()
            QUERY = ' SELECT * FROM EMP  WHERE EMPNAME = :name'
            # Syntax: cursor.execute(QUERY, params).fetchall()
            resultSet = oracleCursor.execute(QUERY, params).fetchall()  # fetchall() -> Need not iterate resultSet
            print(resultSet)
            print()
        except cx_Oracle.DatabaseError as de:
            print("Oracle exception............: ", de)
            print()
        finally:
            oracleCursor.close

    def updateRow(self, newAddress, empIdInput):
        """ DML """
        try:
            oracleCursor = self.__oracleConnection.cursor()
            # Start transaction
            self.__oracleConnection.begin()
            UPDATE_QUERY = 'update EMP  set empAddress = :newAddress where empNo = :empIdInput'
            oracleCursor.execute(UPDATE_QUERY,(newAddress,empIdInput))
            # End transaction
            self.__oracleConnection.commit()
            print('1 row updated')
        except cx_Oracle.DatabaseError as de:
            # Rollback transaction
            self.__oracleConnection.rollback()
            print("Oracle exception in updateRow()............: ", de)
            print()
        finally:
            oracleCursor.close

    def insertBatch(self):
        """ DML """
        SQL = "INSERT INTO EMP (empNo, empName, empAddress) VALUES(:1, :2, :3)"
        data = [
            (601,'Maria', 'India' ),
            (602, 'Vicky', 'France'),
            (603, 'Pio', 'Singapore')
        ]
        try:
            oracleCursor = self.__oracleConnection.cursor()
            oracleCursor.prepare(SQL)
            oracleCursor.executemany(None, data)
            oracleCursor.execute('COMMIT') # Commit
            print('3 rows inserted.')
            print()
        except cx_Oracle.DatabaseError as de:
            print("Oracle exception............: ", de)
            print()
        finally:
            oracleCursor.close

if __name__ == "__main__":
    try:
        print("Entering main..")
        db = DB()
        #db.createTable()
        #db.insertData()
        db.readAllData()
        db.updateRow('Canada1', 100)
        db.insertBatch()

        db.readAllData()
        db.readOneRow({'name': 'Peter'})
    except cx_Oracle.DatabaseError as de:
        print('Database error:',de)

