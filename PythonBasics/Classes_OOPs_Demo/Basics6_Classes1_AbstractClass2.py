"""
An abstract method can have an implementation in the abstract class
Even if they are implemented, users of subclasses will be forced to override the implementation.
The abstract method can be invoked with super() from sub-class
"""

from abc import ABC,abstractmethod

# An abstract method can have an implementation in the abstract class
class Polygon(ABC):
    # abstract method
    @abstractmethod
    def noofsides(self):
        print("Some implementation from Polygon!")

# overriding abstract method
class Triangle(Polygon):
    def noofsides(self):
        super().noofsides()
        print("I have 3 sides from Triangle")

t = Triangle()
t.noofsides()

"""
Some implementation from Polygon!
I have 3 sides from Triangle
"""


