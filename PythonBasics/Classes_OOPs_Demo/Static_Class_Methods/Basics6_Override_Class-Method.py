"""
Class method Overriding.
The difference between class method and static method in Python is, that class method recieves one mandatory argument (ie: cls)– a class name it was called from.
"""
class Example:
    name = "test"  # static variable

    @classmethod
    def static(cls):
        print( cls.name)

class Spring1(Example):
    name = "spring1"

class Spring2(Example):
    name = "spring2"

    @classmethod
    def static(cls):
        print(cls.name)

Example.static()        #   test
Spring1.static()        #   spring1
Spring2.static()        #   spring2