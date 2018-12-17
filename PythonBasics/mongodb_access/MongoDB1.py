
# Access MongoDB using 'pymongo' module
"""
MongoDB Basics:
    Mongo DB is a document oriented database and uses JSON documents to store data.
    It is an open source product, developed and supported by a company named 10gen.

    If an '_id' field is not provided,then MongoDB will create an '_id' field and assign a unique _id for each document(s)
    NoSQL database doesn't use tables for storing data.
    It is generally used to store big data and real-time web applications.
    MonoDB data-types: String,Integer,Boolean,Double,Min/Max Keys,Arrays,Object,Null,Symbol,Date

    In MongoDB, db.createCollection(name, options) is used to create collection (called Row in RDBMS)s.
    But usually you don?t need to create collection. MongoDB creates collection automatically when you insert some documents.

    Comparing MongoDB and RDBMS Objects:-
    RDBMS	        MongoDB
    ------          --------
    Database	    Database
    Table	        Collection
    Tuple/Row	    Document
    column	        Field
    Table Join	    Embedded Documents
    Primary Key	    Primary Key (Default key _id is provided by mongodb)

"PyMongo“ Driver:
    In this demo we will use the MongoDB driver "PyMongo“
    We can use PIP to install "PyMongo“ driver:
    E.g.: C:\Python\Python36-32\Scripts> python -m pip install pymongo
 
To access with IP for MongoDB4 server version:
steps: (open 2 consoles and type)
C:\Program Files\MongoDB\Server\4.0\bin>mongod --bind_ip <IP address>
C:\Program Files\MongoDB\Server\4.0\bin>mongo


"""

import pymongo

"""
# Insert  one document
try:
    # First create a MongoDB Client
    myMongodbClient = pymongo.MongoClient("mongodb://localhost:27017/")
    # Create a database named "mydatabase"
    myMongodb = myMongodbClient["mydatabase"]
    # Create a collection named "customers"
    myCollection = myMongodb["customers"]
    # If an '_id' field is not provided,then MongoDB will assign a unique _id for each document(s)
    myDictionary = { "_id": 3, "name": "Dinesh3", "address": "Bengaluru3" }

    # Insert a document
    myInsertedId = myCollection.insert_one(myDictionary)
    print("unique id: ",myInsertedId.inserted_id)
    print()
except pymongo.errors.DuplicateKeyError as dke:
    print("ERROR:")
    print(dke)
    print()
"""

# -----------------------------------------------------------

# Insert many documents
try:
    myMongodbClient = pymongo.MongoClient("mongodb://localhost:27017/")
    #myMongodbClient = pymongo.MongoClient("mongodb://<IP Address>:27017/")
    myMongodb = myMongodbClient["mydatabase"]
    myCollection = myMongodb["customers"]
    # If an '_id' field is not provided,then MongoDB will assign a unique _id for each document(s)

    mylist = [
        {"_id": 11, "name": "Dinesh4", "address": "Chennai1"},
        {"_id": 21, "name": "Dinesh5", "address": "Bengaluru25"},
        {"_id": 31, "name": "Dinesh6", "address": "Chennai31"}
        ]

    myInsertedIds = myCollection.insert_many(mylist)
    print("unique ids: ",myInsertedIds.inserted_ids)
    print()
except pymongo.errors.DuplicateKeyError as dke:
    print("ERROR:")
    print(dke)
    print()
except pymongo.errors.ServerSelectionTimeoutError as bwe:
    print("ERROR:")
    print(bwe)
    print()
except pymongo.errors.BulkWriteError as bwe:
    print("ERROR:")
    # For duplicate ids
    print(bwe)
    print()
except pymongo.errors.ServerSelectionTimeoutError as sste:
    print("ERROR:")
    print(sste)
    print()

