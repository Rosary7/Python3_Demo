# Exception Raise example
# Pre-defined -exception NameError -Raised when a local or global name is not found

try:
    raise NameError("This is Name Error")
except NameError:
    print("Handled NameError")