"""
 Python by default, it is not able to provide abstract classes, but it comes up with a
 ABC module which provides the base for defining Abstract Base classes(ABC).
 Abstract class can contain both concrete methods as well as abstract methods.
 It can have constructor
 The ABC module was added in Python 2.6 as defined by PEP 3119.
"""

from abc import ABC,abstractmethod

# Abstract class using ABC module
class Polygon(ABC):
    # abstract method
    @abstractmethod
    def noofsides(self):
        pass

    def show(self):             # can have concrete method
        print("helo")

# overriding abstract method
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")

# overriding abstract method not mandatory but instantiation gives errors
class Pentagon(Polygon):
    pass

#pl = Polygon()
#pl.show()              # TypeError: Can't instantiate abstract class Polygon with abstract methods noofsides

t = Triangle()
t.noofsides()
t.show()
print()

# pnt = Pentagon()    # TypeError: Can't instantiate abstract class Pentagon with abstract methods noofsides

