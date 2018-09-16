
# Built-in functions to access attributes
class Employee:
    def __init__(self, empId, empName):  # Constructor or initialization method
        self.empId = empId               # Instance Variable
        self.empName = empName

    def showEmployee(self):
        print("empId :",self.empId, "empName :", self.empName)

# Create an object
emp1 = Employee(2000, "Pio")

# Accessing attributes with built-in functions
print(hasattr(emp1, 'organization'))    # check if 'organization' attribute exists
print(getattr(emp1, 'empName'))         # access 'empName' attribute
emp1, 'empName', "Kumar"
print(getattr(emp1, 'empName'))         # set an attribute.If attribute does not exist, then it would be created.
#delattr(emp1, 'empName')               # to delete 'empName' attribute.
#print(getattr(emp1, 'empName'))        # AttributeError: 'Employee' object has no attribute 'empName'






