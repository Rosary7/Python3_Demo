
# ARRAYS
# Note: Python does not have built-in support for Arrays, but Python lists can be used instead.

# ---------------------------------------------------------------------------------------------

"""
Collections (Arrays)
There are four collection data types-
List is a collection       - ordered,changeable,allows duplicate. Syntax:  square brackets []
Tuple is a collection      - ordered,unchangeable,allows duplicate. Syntax: round brackets ()
Set is a collection        - unordered,unindexed,no duplicate . Syntax: curly brackets {}
Dictionary is a collection - unordered,changeable,indexed,no duplicate.Syntax: curly brackets {} and they have keys and values.
"""

# LIST
# Syntax: square brackets []
langlist = ["java", "c#", "python"]
print(langlist)
print(langlist[0])
print()

# Change List Item Value
langlist[1] = "Angular"
print(langlist)
print()

# Loop Through a List
""" 
Note: 
1) colon (:) at FOR loop ending
2) Indentation for the next statement  ( If no indentation, we will get "IndentationError") """
langlist = ["java", "c#", "python"]
for x in langlist:
    print(x)

# List Length
langlist = ["java", "c#", "python"]
print()
print(len(langlist))
print()

# Add , remove items in list
langlist = ["java", "c#", "python"]
langlist.insert(1,"VB.NET")
print(langlist)   # ['java', 'VB.NET', 'c#', 'python']
langlist.remove('python')
print(langlist)    #  ['java', 'VB.NET', 'c#']
print()

# pop item in list
# removes the specified index, (or the last item if index is not specified)
langlist = ["java", "c#", "python"]
langlist.pop()
print(langlist)   # ['java', 'c#']
langlist = ["java", "c#", "python"]
langlist.pop(0)
print(langlist)  #  ['c#', 'python']
print()

# clear method empties the list
langlist = ["java", "c#", "python"]
langlist.clear();
print(langlist)   # []
print()

# del keyword can also delete the list completely
langlist = ["java", "c#", "python"]
del langlist

# list() Constructor
# Note:  syntax: double round-brackets
countrylist = list(("India", "UK", "US"))
print(countrylist)
print()

# ---------------------------------------------------------------------------------------------

# TUPLES
# Syntax: round brackets ()
langtuples = ("java", "c#", "python")
print(langtuples)  # ('java', 'c#', 'python')
print()

# Access Tuple Items
langtuples = ("java", "c#", "python")
print(langtuples[2])  # python
print()

# Loop Through a Tuple
langtuples = ("java", "c#", "python")
for x in langtuples:
    print(x)

# del keyword can delete the tuple completely
# After deleting, if we try to access it, we will get error as tuple not defined
langtuples = ("java", "c#", "python")
del langtuples
# print(langtuples)  # NameError: name 'langtuples' is not defined


# Note:  Tuples are unchangeable. We cannot add/remove items
langtuples = ("java", "c#", "python")
#langtuples[2] = "VB"   # TypeError: 'tuple' object does not support item assignment
#print(langtuples[2])  # python

# ----------------------------------------------------------------------------------------
# SET
# Syntax: curly brackets {}
# Sets are unordered, so the items will appear in a random orde
print()
langset = {"java", "c#", "python"}
print(langset)   # {'c#', 'java', 'python'}

# add() vs update()
# add() - To add one item to tuple
# update() - To add multiples items to tuple
print()
langset = {"java", "c#", "python"}
langset.add("VB")
print(langset)  # {'VB', 'c#', 'python', 'java'}
langset.update(["ExtJS","HTML5"])  # {'VB', 'c#', 'Angular', 'java', 'ExtJS', 'HTML5', 'python'}
print(langset)

# remove() vs discard()
# remove() - If the item to remove does not exist, remove() will raise an error.
# discard() - If the item to remove does not exist, discard() will NOT raise an error.
print()
langset = {"java", "c#", "python"}
#langset.remove("VB")  # AttributeError: 'set' object has no attribute 'reemove' . KeyError: 'VB'
print(langset)  # {'VB', 'c#', 'python', 'java'}
langset.discard("VB")  # No error raised
print(langset)

# clear() method empties the Set
print()
langset = {"java", "c#", "python"}
langset.clear()
print(langset)   # set()

# del keyword will delete the set completely
print()
langset = {"java", "c#", "python"}
del langset
# print(langset) # NameError: name 'langset' is not defined

# set() Constructor
# It is also possible to use the set() constructor to make a set.
# Syntax: Note the double round-brackets
langset = set(("java", "c#", "python"))
print(langset)  # {'python', 'java', 'c#'}
print()

# ----------------------------------------------------------------------------------------
# DICTIONARY
""" 
In Python dictionaries are written with {} curly brackets and they have keys and values.
A dictionary is a collection which is unordered, changeable and indexed. I
"""

# Create a dictionary and print
pythonDict = {
    "conceived" : "1980",
    "implemneted" : "1989",
    "author" : "Guido van Rossum",
    "dynamically-typed" : "yes",
    "OOPs"  : "Yes",
    "latest-version" : "3.6"
}

# Print dictionary
print(pythonDict)       # {'conceived': '1980', 'implemneted': '1985', 'dynamically-typed': 'yes', 'OOPs': 'Yes', 'latest-version': '3.x'}
print()

# Get the value of the "latest-version" key:
print(pythonDict["latest-version"])            #  3.x
print()
# Get the value of the "latest-version" key: using get()
print(pythonDict.get("latest-version"))        #  3.x
print()

# change the value of a specific item by referring to its key name
pythonDict["latest-version"] = "3.6.4"
print(pythonDict)
print()

# Loop and Print key adn value
# Note : FOR loop syntax requirws colon (:) at ends
for x in pythonDict:
    print(x + "=" + pythonDict[x])

# Loop through both keys and values, by using the items()
print()
for x,y in pythonDict.items():
    print(x,y)

# Adding Items to dictionary
print()
pythonDict["supports-database-access"] = "yes"
print(pythonDict)
print()

# del keyword removes the item with the specified key name
del pythonDict["supports-database-access"]
print(pythonDict)
print()

# pop() method removes the item with the specified key name
# popitem() method removes the last item
pythonDict.pop("author")
pythonDict.popitem()
print(pythonDict)
print()

# del keyword can also delete the dictionary completely
#del pythonDict
#print(pythonDict)  # NameError: name 'pythonDict' is not defined

# dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary
mobileDict = dict(apple = "ios", google = "android")  # {'apple': 'ios', 'google': 'android'}
print(mobileDict)