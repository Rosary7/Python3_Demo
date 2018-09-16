
#  Finalizer (Destroying Objects / Garbage Collection / Destructor)
"""
Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space.
Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero.
An object's reference count changes as the number of aliases that point to it changes.
An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary).
The object's reference count decreases when it is deleted with del, its reference is reassigned, or its reference goes out of scope.
sWhen an object's reference count reaches zero, Python collects it automatically.
"""
class Employee:
    def __init__(self, empId):  # Constructor or initialization method
        self.empId = empId               # Instance Variable

    def showEmployee(self):
        print("empId :",self.empId)

    # Destroying Objects (Garbage Collection) using Destructor known as finalizer
    def __del__(self):
        className = self.__class__.__name__
        print(className, "is destroyed")

# Create an object
emp1 = Employee(2000)
emp2 = emp1     # Increase ref. count  of <emp1>

del emp1        # Decrease ref. count  of <emp1>

