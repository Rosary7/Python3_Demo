"""
When Python runs the "source file" as the main program, it sets the special variable (__name__) to have a value ("__main__").
So,  if __name__== "__main__" ,allows you to run the Python files either as reusable modules or standalone programs.

"""
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

def main():
    emp = Employee("Peter");
    emp.show()

if __name__ == '__main__':
    main()