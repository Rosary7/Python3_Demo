"""
Python pickle module is used for serializing and de-serializing a Python object structure.
Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
Later on, this character stream can then be retrieved and de-serialized back to a Python object.

Following can be pickled: Booleans,Integers,Floats,Complex numbers,Strings,Tuples,Lists,Sets, and Dictionaries that ontain picklable objects.

Pickling means Serialization
Unpickling means De-serialization
"""
import pickle

# Pickle in Python: Object Serialization
def storeData():
    # initializing data to be stored in db
    emp1 = {'id': '100', 'name': 'Peter'}
    emp2 = {'id': '101', 'name': 'Kumar'}

    # Emp database
    emp_db = {}
    emp_db['emp1'] = emp1
    emp_db['emp2'] = emp2

    # Open file in binary mode
    emp_db_file = open('examplePickle', 'ab')

    # Serialize with dump() by passing source, destination
    pickle.dump(emp_db, emp_db_file)
    emp_db_file.close()

def loadData():
    # Read in binary mode
    emp_db_file = open('examplePickle', 'rb')
    # De-serialize it with load()
    db = pickle.load(emp_db_file)
    for keys in db:
        print(keys, '=>', db[keys])
    emp_db_file.close()


if __name__ == '__main__':
    storeData()
    loadData()


