#  User Defined Exception Example
"""
When  we  define  our own exception, we should extend  Exception class or one of its subclasses,
and not from BaseException.
"""

class SmallValueError(Exception):
    def __init__(self, arg):
        self.arg = arg

try:
    x = int(input('Enter a number > 10'))
    if x < 10:
        raise SmallValueError('Invalid input')
    print("Entered number is :" , x)
except SmallValueError as sve:
    print("Entered number is < 10 ", sve)