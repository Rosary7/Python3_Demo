
"""
Python does not support Method Overloading.(But can be achieved in different way)
We may overload the methods but can only use the latest defined method.
"""
def show( id):
    print("show  :",  id)

def show( id,name):
    print("show  :",  id)

# We get error : TypeError: show() missing 1 required positional argument: 'name'
show(10)
show(10,'Peter')