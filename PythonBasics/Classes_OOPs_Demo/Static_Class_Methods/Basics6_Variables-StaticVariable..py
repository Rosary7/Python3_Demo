"""
Variables declared inside the class definition, but not inside a method/constructor are called class or static variables.
"""

# We can have two different variables in a class under the same name (one static and one ordinary).
class Example:
    static_variable = 5        # static variable

# Access through class
print(Example.static_variable)       #  5   (static variable)

# Access through an instance
my_instance = Example()
print(my_instance.static_variable)    # 5    (ordinary variable)

# Change within an instance
my_instance.static_variable = 6
print(my_instance.static_variable)    # 6
print(Example.static_variable)        # 5

# Change through class
Example.static_variable = 7
print(my_instance.static_variable)    # still 6
print(Example.static_variable)        # now 7