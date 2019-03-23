
"""
Python does not support Method Overloading.(But can be achieved in different way as belows)
"""
class HeloWorld:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')

obj = HeloWorld()

# Call the method with no param
obj.sayHello()

# Call the method with a param
obj.sayHello('Peter')