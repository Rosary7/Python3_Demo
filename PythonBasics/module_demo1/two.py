# Example for __name__  attribute of module, when a module is imported

# file two.py
import one

print("top-level in two.py")
print()
one.func()

# When module one gets loaded, its __name__  is not equals to  "one" instead of "__main__"
if __name__ == "__main__":
    print("two.py is being run directly")
    print("__name__ == '__main__' : " , (__name__ == "__main__"))
    print()
else:
    print("two.py is being imported into another module")
    print()

"""
output:
top-level in one.py
one.py is being imported into another module
top-level in two.py
func() in one.py
two.py is being run directly
__name__ == '__main__' :  True
"""