# FUNCTIONS

"""
A function is defined using the "def" keyword.
A function can have parameter, default parameter, return value
"""

# Define
def show_functionA():
    print("Hello World")

# call a function
print("show_functionA() :s")
show_functionA()
print()

# ----------------------------------------------------------------------------------------

# default parameter
""" Note: non-default argument must first default argument must be second. If non-default argument is given first, 
    then we get below error-
    fintaxError: non-default argument follows default argument
"""
def show_functionB(empName,salutation = "Mr/Ms"):
    print(salutation + "." + empName)

show_functionB("Kumar")
show_functionB("Mr.Mani")
print()

# ----------------------------------------------------------------------------------------
# Return Values
def show_functionC(x):
    return x * 10

print("show_functionC() return vale: ", show_functionC(2))
print()

# ----------------------------------------------------------------------------------------

""" 
 The map() function in Python takes in a function and a list, as arguments
 map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
 Syntax: map(fun, iter)
 where,
    fun : It is a function to which map passes each element of given iterable.
    iter :It is a iterable which is to be mapped.
"""


# Python program to demonstrate working of map().
# Return multiplication of n
def multiply(n):
    return n * n

# We multiply all numbers using map()
numbers = (7, 2, 3, 4)
result = map(multiply, numbers)
print("Python program to demonstrate working of map():")
print(list(result))     # [49, 4, 9, 16]
print()

# filter() example
# Syntax:  filter(function, sequence) 
alphabetsList = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# function that filters vowels
def filterVowelsFunction(alphabet):
    vowelsList = ['a', 'e', 'i', 'o', 'u']

    if (alphabet in vowelsList):
        return True
    else:
        return False

filteredVowels = filter(filterVowelsFunction, alphabetsList)
print('The filtered vowels using filter():')
for vowel in filteredVowels:
    print(vowel)

# ----------------------------------------------------------------------------------------
#                                           LAMBDA
# ----------------------------------------------------------------------------------------

# LAMBDAs
"""
A lambda function  is an anonymous function.
In Python anonymous functions are defined using the lambda keyword.
A lambda function can take many arguments, but can only have one expression.
It cannot contain any statements and it returns a function object which can be assigned to any variable.
 
Syntax:
lambda arguments : expression

Why Use Lambda Functions?
It  is useful when we use Lambda as an anonymous function inside another function.
In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
Lambda functions are used along with built-in functions like filter(), map() etc.
"""
# Lambda example
x = lambda y : y + 10
print("Lambda example:s")
print(x(2))      # 12
print()

# ----------------------------------------------------------------------------------------

# Convert a function  into a lambda function
# Define function with "def" keyword
print("Convert a function  into a lambda function")
def multiply(a,b):
    return a * b

print(multiply(5,10))
print()

# Now we convert above function  into a lambda function
x = lambda y, z : y * z
print("Now we convert above function  into a lambda function:")
print(x(5,10))      # 50
print()
# ----------------------------------------------------------------------------------------

# No need to assign lambda function to a variable.
print(" No need to assign lambda function to a variable:")
print((lambda x, y: x * y)(3,4))
print()

# ----------------------------------------------------------------------------------------
# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))     # [5, 7, 9]
print()

# ----------------------------------------------------------------------------------------
# Lamda  use with filter()
# The filter() function takes in a function and a list as arguments
# filter() creates a list of elements for which a function returns true.

# Program to filter out only the even items from a list
print("rogram to filter out only the even items from a list")
my_list = [11, 2, 6, 12, 24, 55]
new_list = list(filter(lambda x : (x % 2 == 0), my_list))
print(new_list)   # [2, 6, 12, 24]
print()

# ----------------------------------------------------------------------------------------
# Lamda  use with map()
""" 
 The map() function in Python takes in a function and a list
 map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
 Syntax: map(fun, iter)
 where,
    fun : It is a function to which map passes each element of given iterable.
    iter :It is a iterable which is to be mapped.
"""

# Program to square items from a list without lambda
print("Program to square items from a list without lambda")
my_list = [5, 2, 6, 8]
even_list = []
for x in my_list:
    even_list.append(x * x)
print(even_list)   # [25, 4, 36, 64]
print()

# Program to square items from a list with lambda
print("Program to square items from a list with lambda")
my_list = [5, 2, 6, 8]
new_list = list(map(lambda x : x * x, my_list))
print(new_list)   # [25, 4, 36, 64]
print()

# ----------------------------------------------------------------------------------------

# Python Program to display the powers of 2 using lambda and map() function

# Change this value for a different result
terms = 5

# Uncomment to take number of terms from user
#terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

# display the result
print("Python Program to display the powers of 2 using lambda and map() function")
print("The total terms is:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])

""" Output:
The total terms is: 5
2 raised to power 0 is 1
2 raised to power 1 is 2
2 raised to power 2 is 4
2 raised to power 3 is 8
2 raised to power 4 is 16
"""

# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
