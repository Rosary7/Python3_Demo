# String Built-in Functions

str = "python code"
print(str.capitalize())     # output:  ****python code*****
print()

# center(width, fillchar) , where width is total width of output which includes input plus padded chars
print(str.center(20, '*'))  # output:  ****python code*****
print()

# Returns true if string contains only digits and false otherwise.
print(str.isdigit())        # output:  False
print()

# Returns true if string has at least one lower cased character
print(str.islower())        # output:  True
print()

# Converts all uppercase letters in string to lowercase.
print(str.lower())          # output:  python code
print()

# Strips char from the beginning and the end of the string
str = "*****Hello*****"
print (str.strip( '*' ))    # output:  Hello
print()

# Strips whitespace characters from the beginning and the end of the string
str = " Hello   "
print (str.strip())    # output:  Hello
print()
