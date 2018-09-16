
# Built-In Class Attributes
class Employee:
    'Employee class demo'
    def __init__(self, empId, empName):  # Constructor or initialization method
        self.empId = empId               # Instance Variable
        self.empName = empName

    def showEmployee(self):
        print("empId :",self.empId, "empName :", self.empName)

# Create an object
emp1 = Employee(2000, "Pio")

# Accessing with built-in Class Attributes
print(Employee.__doc__)     #  Class documentation string or none, if undefined.
print(Employee.__name__)    # − Class name
print(Employee.__module__)  # Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print(Employee.__bases__)   # set an attribute.If attribute does not exist, then it would be created.
print(Employee.__dict__)    # Dictionary containing the class's namespace.






