
# Creating class demo
# Constructor and destructor
class Employee:
    organization = "xyz inc"             # Class or static Variable
    empCount = 0                         # Class or static Variable
    def __init__(self, empId, empName):  # Constructor or initialization method
        self.empId = empId               # Instance Variable
        self.empName = empName
        Employee.empCount += 1

    def showEmployee(self):
        print("empId :",self.empId, "empName :", self.empName)

    # Destroying Objects (Garbage Collection) using Destructor
    def __del__(self):
        className = self.__class__.__name__
        print(className, "is destroyed")

# Create an object
emp1 = Employee(2000, "Pio")
emp2 = Employee(2001, "Raj")

emp1.showEmployee()
# Accessing values
print(emp1.organization)
print(emp1.empId)
print(Employee.organization)
print("Employee count: ", Employee.empCount)

# Changing value
emp1.empName= "Amal"
print(emp1.empName)        # Accessing 'empName' attribute after changing it

# Delete objects
del emp1
del emp2

