"""
Static method Overriding.
"""
class Example:
    name = "test"  # static variable

    @staticmethod
    def static():
        print( Example.name)

class Spring1(Example):
    name = "spring1"

class Spring2(Example):
    name = "spring2"

    @staticmethod
    def static():
        print(Spring2.name)

Example.static()        #   test
Spring1.static()        #   test
Spring2.static()        #   spring2