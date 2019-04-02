"""
Accessing MySql using "pymysql" driver:

Pre-requisite:-
  Install "pymysql" driver:
  C:\Program Files\Python 3.5\Lib>pip install pymysql
"""

# MySql - CRUD
import pymysql

def createConnnection():
    try:
        con = pymysql.connect("localhost","root","root","poc_db")
        return con
    except pymysql.err.OperationalError as oe:
        print('Credentials error:', oe)
    except pymysql.err.InternalError as ie:
        print('Database  error:', ie)
    except Exception as e:
        print('General  error:', e)


def createTable():
    create_table_sql = """CREATE TABLE EMP_TABLE (
             FIRST_NAME  CHAR(20) NOT NULL,
             AGE INT,
             INCOME FLOAT )"""
    con = None
    try:
        con = createConnnection()
        cursor = con.cursor()
        cursor.execute("DROP TABLE IF EXISTS EMP_TABLE")
        cursor.execute(create_table_sql)
        print('EMP_TABLE Table Created')
        print()
    except pymysql.err.OperationalError as oe:
        print('Credentials error:', oe)
    except pymysql.err.InternalError as ie:
        print('Database  error:', ie)
    except Exception as e:
        print('General  error:', e)
    finally:
        if con is not None:
            con.close()


def insertData():
    insert_sql =   """INSERT INTO EMP_TABLE(FIRST_NAME,AGE,INCOME)
                      VALUES ('Peter', '20',20000)"""
    con = None
    try:
        con = createConnnection()
        cursor = con.cursor()
        cursor.execute(insert_sql)
        con.commit()
        print('One row inserted and committed')
        print()
    except pymysql.err.OperationalError as oe:
        print('Credentials error:', oe)
    except pymysql.err.InternalError as ie:
        print('Database  error:', ie)
    except Exception as e:
        con.rollback()
        print('General  error:', e)
    finally:
        if con is not None:
            con.close()

def readAllData():
    select_sql =   "SELECT * FROM  EMP_TABLE"
    con = None
    try:
        con = createConnnection()
        cursor = con.cursor()
        cursor.execute(select_sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            age = row[1]
            sal = row[2]
            print("fname = ",fname, ",age = ",age,",sal = ",sal)
        print()
    except pymysql.err.OperationalError as oe:
        print('Credentials error:', oe)
    except pymysql.err.InternalError as ie:
        print('Database  error:', ie)
    except Exception as e:
        con.rollback()
        print('General  error:', e)
    finally:
        if con is not None:
            con.close()

def updateData():
    pass

if __name__ == '__main__':
    createTable()
    insertData()
    readAllData()
