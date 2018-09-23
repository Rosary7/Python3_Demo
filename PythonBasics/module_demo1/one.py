# Example for __name__  attribute of module, when a module is not imported
"""
Unlike other languages, there's no main() function that gets run automatically - the main() function is
implicitly all the code at the top level.

Every module in python has a special attribute called __name__ .
The value of __name__  attribute is set to '__main__'  when module run as main program.
Otherwise the value of __name__  is set to contain the name of the module.
"""

# file one.py print()
def func():
    print("func() in one.py")
    print()

print("top-level in one.py")
print()

# When module one gets loaded, its __name__ equals "one" instead of "__main__"
if __name__ == "__main__":
    print("one.py is being run directly")
    print("__name__ == '__main__' : " , (__name__ == "__main__"))
    print()
else:
    print("one.py is being imported into another module")
    print()

"""
output:
top-level in one.py
one.py is being run directly
__name__ == '__main__' :  True
"""