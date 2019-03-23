# FUNCTIONS WITH DATA TYPE FOR PARAM

"""
Python variables are pointing to objects, which know their type. (they are not variables as other language)

However, one interesting thing has changed with the implementation of PEP 3107 (implemented in Python 3).
We can now specify function with parameter type and return type.
PEP 3107  improves code readability.
https://www.python.org/dev/peps/pep-3107/

"""

# Function with parameter type and return type
def add(a: int, b: int) -> int:
    return a + b

print(add(2,3))
#print(add(2,"helo"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(add("4","1"))    # 23
print(add(3.2,3))      # 6.2

def show(emp_list: list):
     for var in emp_list:
         print(var)

new_list = ["kumar","peter"]
show(new_list)
print()
show("helo")
print()
show("24")
print()
#show(31)     # TypeError: 'int' object is not iterable