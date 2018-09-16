#  Class Inheritance
"""
Syntax:
class SubClassName (ParentClass1[, ParentClass2, ...]):
"""
class Vehicle:
    def __init__(self, name, color):
        self.__name = name  # __name is private to Vehicle class
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getName(self):
        return self.__name

class Car(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)       # call parent constructor to set name and color
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"

c = Car("Ford Figo", "red", "RT350")
print(c.getDescription())
print(c.getName())

# issubclass(sub, sup)  : returns True, if the given subclass 'Child' is a subclass of the superclass 'Parent'
print(issubclass(Car, Vehicle))
# Syntax: isinstance(object, class_type)
print(isinstance(c, Car))         # returns True
print(isinstance(c, Vehicle))        # returns True
