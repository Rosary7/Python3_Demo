# Exception handling
# try - except - else

a = [1,2,3]
try:
    something = a[2]
except:
    print("out of bounds exception")
else:
    print(something)

"""
Without using 'else':

a = [1,2,3]
try:
    something = a[2]
except:
    print("out of bounds")s

if "something" in locals():
    print(something)
"""