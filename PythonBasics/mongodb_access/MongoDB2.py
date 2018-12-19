
# Access MongoDB using 'pymongo' module

import pymongo

# find one document
# find  all or selected document
# Sort, delete
try:
    myMongodbClient = pymongo.MongoClient("mongodb://localhost:27017/")
    myMongodb = myMongodbClient["mydatabase"]
    myCollection = myMongodb["customers"]

    # Find the first document in the customers collection
    print()
    print('Find the first document in the customers collection')
    x = myCollection.find_one()
    print(x)
    print()

    # Loop all customers collection
    print('Loop all customers collection')
    for x in myCollection.find():
        print(x)

    # Return all except 'ids'
    print()
    print('FReturn all except ids')
    for x in myCollection.find({},{ "_id": 0, "name": 1, "address": 1 }):
        print(x)

    # Find document(s) with the address starts with the char "C" or higher (alphabetically):
    myQuery = { "address": { "$gt": "C" } }
    myDocument = myCollection.find(myQuery)
    print()
    print('Find document(s) with the address starts with the char "C"')
    for x in myDocument:
      print(x)

    # Sort
    # sort("name", 1)  - ascending
    # sort("name", -1) - descending
    myDocument = myCollection.find().sort("name", 1)
    print()
    print('Sort by name:')
    for x in myDocument:
        print(x)

    # Delete a Doc
    myQuery = {"address": "Bengaluru4"}
    myCollection.delete_one(myQuery)
    print()
    print("Printing after deletion: ")
    for x in myCollection.find():
        print(x)

    # Delete all documents
    print()
    if(myCollection.count() == 0):
        print('No documents available for deletion')
    else:
        print()
        # myDeletedCount = myCollection.delete_many({})
        #print("All documents deleted. Deleted Count:", myDeletedCount.deleted_count)

    # Delete Collection
    #myCollection.drop()

except pymongo.errors.DuplicateKeyError as dke:
    print("ERROR:")
    print(dke)
    print()
