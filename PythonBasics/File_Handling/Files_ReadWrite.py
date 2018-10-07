
# Write to a File
try:
    # Syntax:  open(file_name [, access_mode][, buffering])
    myFileA = open('H:\\test1.txt', 'w')
    myFileA.write('Helo World')
finally:
    myFileA.close()

# ------------------------------------------------------------------

# Read from a Files
try:
    myFileB = open('H:\\test1.txt', 'r+')
    # Syntax: fileObject.read([count]) , if count is missing then reads from beginning
    x = myFileB.read()
    print(x)
    print()
finally:
    myFileB.close()

# ------------------------------------------------------------------

# Open a file
fileC = open("test2.txt", "r+")
dataRead = fileC.read(22)
print ("Read String is : ", dataRead)

# Check the current position using tell()
position = fileC.tell()
print ("Current file position is: ", position)

# Reposition pointer at the beginning once again using seek()
position = fileC.seek(0, 0)
str = fileC.read(7)
print ("Again read String is : ", str)

# Close opened file
fileC.close()
print()