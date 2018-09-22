# The built-in function dir() is used to find out which names a module defines.
import math
import builtins
import sys

# list the names of built-in math modules
print(dir(math))
print()
# list the names of built-in functions and variables
print(dir(builtins))

print()
# list the names of built-in functions and variables
print(sys.path)