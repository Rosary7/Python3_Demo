# local vs global variables
"""
Global variables are the one that are defined and declared inside a function
Global variables are the one that are defined and declared outside a function
We use global keyword to access global variable inside a function when there is ambiguity
"""

print("Default global variable :")
def funA():
    print(s)
s = "Java developer"    # global variable
funA()
print()
# output: Java developer

# ---------------------------------------------------------------------------------------------

def funB():
    s = "Python developer"   # local variable
    print(s)

s = "Java developer"     # global variable
print("local vs global variable:")
funB()
print(s)        #  It will refer global variable  's'
# output: Python developer
#         Java developer
print()

# ---------------------------------------------------------------------------------------------

print("local variable 's' referenced in funC() before assignment which will throw error:")
def funC():
    #print(s)        #  It will throw an error
    s = "Python developer"   # local variable
    print(s)

s = "Java developer"     # global variable
funC()
print(s)
print()
# output: UnboundLocalError: local variable 's' referenced before assignment

# ---------------------------------------------------------------------------------------------

print("keyword 'global' usage to resolve ambiguity :")
def funC():
    global s
    print(s)        #  It will refer global variable  's'
    s = "Python developer"   # local variable
    print(s)        #  It will refer local variable  's'

s = "Java developer"     # global variable
funC()
print(s)
print()
# output: UnboundLocalError: local variable 's' referenced before assignment


# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
