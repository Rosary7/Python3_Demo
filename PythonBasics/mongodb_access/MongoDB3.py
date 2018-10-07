
# Access MongoDB using 'pymongo' module

import pymongo

# Update Collection,
# Limit the Result

try:
    myMongodbClient = pymongo.MongoClient("mongodb://localhost:27017/")
    myMongodb = myMongodbClient["mydatabase"]
    myCollection = myMongodb["customers"]

    # Update a document
    myQuery = {"address": "Chennai006"}
    newValue = {"$set": {"address": "Chennai0106"}}
    # If more than one document matches,then the first occurrence is updated
    myCollection.update_one(myQuery, newValue)
    # print "customers" after a Doc update:
    for x in myCollection.find():
        print(x)
    print()

    # Update all documents were the address starts with the letter "D":
    myQuery = {"address": {"$regex": "^B"}}
    newValues = {"$set": {"address": "Banglore"}}
    myUpdatedDocCout = myCollection.update_many(myQuery, newValues)
    print(myUpdatedDocCout.modified_count, "documents updated.")
    # print "customers" after all Docs update:
    for x in myCollection.find():
        print(x)
    print()

    # Limit the result to 2
    myResult = myCollection.find().limit(2)
    for x in myResult:
        print(x)
    print()

except pymongo.errors.DuplicateKeyError as dke:
    print("ERROR:")
    print(dke)
    print()