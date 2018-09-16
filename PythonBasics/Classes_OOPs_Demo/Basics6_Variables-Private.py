"""
A private variable is prefixed with two underscores eg: __empIds
A private Variable  cannot be accessed outside class.
But, it can be accessed using the  masked name of private variable, which can obtained
from class attributes ie: __dict__
"""

class Emp:
    def __init__(self):
        self.__empId= 2000

    def printVar(self):
        print(self.__empId)

x = Emp()
print(x.printVar())
print()
# Creates error, as a private variable  cannot be accessed outside class.
print(x.__empId)        # output: AttributeError: 'A' object has no attribute '__empId'

print(x.__dict__)
print()

# But, it can be accessed using the masked name of private variable, obtained from class attributes ie: __dict__
print(x._Emp__empId)
