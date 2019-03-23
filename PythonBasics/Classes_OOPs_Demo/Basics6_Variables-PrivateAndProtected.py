"""
public, private and protected Access Modifiers:
All members in a Python class are "public" by default.
A "private" variable is prefixed with two underscores eg: __empId
A "protected" variable is prefixed with one underscores eg: _empId (It is only a convention and still we can access)

A private Variable  cannot be accessed outside class.
But, it can be accessed using the  masked name of private variable, which can obtained from class attributes ie: __dict__

Python doesn't have any mechanism that effectively restricts access to any instance variable or method.

Python prescribes a convention of prefixing the name of the variable/method with single or double underscore
to emulate the behaviour of protected and private access specifiers and programmer must follow this convention.
"""

# private and protected variables
class Emp:
    def __init__(self):
        self.__empId= 2000       # private variable
        self._empName = "Peter"  # protected variable

    def printVar(self):
        print(self.__empId)
        print(self._empName)

x = Emp()
x.printVar()
print()

# Creates error, as a private variable  cannot be accessed outside class.
#print(x.__empId)        # output: AttributeError: 'A' object has no attribute '__empId'

#print(x.__dict__)
print()

# But, private variable can be accessed using the masked name of private variable, obtained from class attributes ie: __dict__
#print(x._Emp__empId)
