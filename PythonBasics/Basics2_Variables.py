# Variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# A variable can even change type after they have been set,by re-assigning new value.
# To combine both text and a variable, Python uses the + character.

"""
Variable Names:
Must start with a letter or the underscore character
It cannot start with a number
It can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
It is ccase-sensitive .

There are three numeric types:
int
float
complex
"""

# VARIABLES

# String variable example
x = "hello"
y = "world"
print(x+y)

# Number variable example
x = 5
y = 10
print(x+y)

# Mixing operators between numbers and strings is not supported and will give you an error
x = "Hello"
y = 10
# print(x+y) # TypeError: must be str, not int

# NUMBER types - int , float, complex
x = 10      # int
y1 = 21.8   # float
y2 = 35e3   # float
z = 11j     # complex

print(x)
print(y1)
print(y2)
print(z)

# type() function is ued to verify the type of any object in Python:
print(type(x))   # <class 'int'>
print(type(y1))
print(type(z))

# Casting Variable Type:)
# Integer example
x = int(11)   # 11
y = int(24.8) # 24
z = int("2")  # 2
print(x)
print(y)
print(z)

# Float Example
x = float(15)     # 15.0
y = float(21.8)   # 21.8
z = float("5")    # 5
z1 = float("1.2")  # 1.2
print(x)
print(y)
print(z)
print(z1)

# String Example
x = str("a1")  #  's1'
y = str(21)    #  '21'
z = str(22.0)  #  "22.0'
print(x)
print(y)
print(z)

# OPERATORS
# Identity operators - used to compare the objects are equal based on contents and memory location.
x = ["employer", "epmloyee"]
y = ["employer", "epmloyee"]
z = x

print(x is z)   # returns True because z is the same object as x
print(x is y)   # returns False because x is not the same object as y, even if they have thew same content
print(x == y)   # returns True because x is equal to y

# Membership operators - used to test if a sequence is presented in an object.
x =  "ermployer1"
y = ["ermployer", "epmloyee"]
print(x in y)  # returns True because a sequence with the value "ermployer1" is in the list

# Assignments can be done on more than one variable "simultaneously"
a, b = 10, 20
print(a + b)