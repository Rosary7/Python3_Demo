
"""
*args and **kwargs in python explained.

*args : variable length of arguments to a function.
**kwargs: allows to pass keyworded variable length of arguments to a function.

"""

# Usage of *args
def test_var_args( *argv):
    for arg in argv:
        print(arg)

test_var_args('Perl','python','nodejs','scala')
print()

# Usage of **kwargs
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(key, "=", value)

greet_me(name1="Peter",name2="Kumar")

