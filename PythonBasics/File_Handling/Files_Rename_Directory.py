
#  File - Renaming and Deleting
# Syntax:  os.rename(current_file_name, new_file_name)
# Syntax:  os.remove(current_file_name, new_file_name)

import os

try:
    os.rename("test1.txt", "test1a.txt")
    print(" test1.txt renamed to test1a.txt")
except FileNotFoundError as fnfe:
    print("File test1.txt not found")
    print()

# ------------------------------------------------------------------

try:
    os.remove("test1.txt")
    print(" test1.txt deleted")
except FileNotFoundError as fnfe:
    print("File test1.txt not found")
    print()

# ------------------------------------------------------------------
# Directory manipulation

# Create a directory in the current directory

try:
    os.mkdir("testdir")
except FileExistsError as fee:
    print("testdir directory already exists")
    print()

# displays the current working directory
print(os.getcwd())
print()

# rmdir() deletes directory
# Syntax: os.rmdir('dirname')