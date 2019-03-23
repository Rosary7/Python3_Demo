"""
Instance Methods:
Through the self parameter, instance methods can freely access attributes and other methods on the same object
It takes self parameter as mandatory
Class  Methods:
Marked with @classmethod decorator, to flag it as a class method
It take a cls (we can use any variable instead of cls) parameter that points to the class.
Because the class method only has access to this cls argument, it can’t modify object instance state. That
would require access to self. However, class methods can still modify class state that applies across all
instances of the class.

Static Methods:
Marked with @staticmethod decorator, to flag it as a class method
Behind the scenes Python simply enforces the access restrictions by not passing in the self or the cls
argument when a static method gets called using the dot syntax.
Therefore a static method can neither modify object state nor class state.

Key Takeaways
Instance methods need a class instance and can access the instance through self.
Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.

"""

# Instance, Class, and Static Methods
class MyClass:
    def instance_method(self):
        return 'instance method called', self

    # Known as decorator
    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'

my_class = MyClass()
print(my_class.instance_method())
print(my_class.class_method())
print(my_class.static_method())
print()

print(MyClass.class_method())
print(MyClass.static_method())

"""
('instance method called', <__main__.MyClass object at 0x00000000027EE1D0>)
('class method called', <class '__main__.MyClass'>)
static method called

('class method called', <class '__main__.MyClass'>)
static method called
"""
