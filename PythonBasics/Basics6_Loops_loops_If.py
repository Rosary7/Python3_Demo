
# IF - Elif - else

x = 20
y = 120
if x > y:
    print("x is highest")
elif y > x:
    print("y is highest")
else:
    print("x and y are equal")

# ----------------------------------------------------------------------------------------

# Short Hand If
print()
if y > x : print("y is highest")

# ----------------------------------------------------------------------------------------
# Short Hand If ... Else
print()
print("x is highest") if x > y else print("y is highest")

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# For Loops
"""
Syntax: for iterator_var in sequence:

For example: traversing a list or string or array etc. 
It can be used to iterate over iterators and  range

"""
# Print each item from list
print()
swLang = ["java", "c#", "python"]
for x in swLang:
    print(x)

# ----------------------------------------------------------------------------------------
# strings are iterable objects, they contain a sequence of characters
# prints each char in the string
print()
for x in "python":
    print(x)

# ----------------------------------------------------------------------------------------
# range() returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default) and ends at a specified number.
# Syntax:
""" 
range(stop)
s
Returns a sequence of numbers starting from 0 to stop - 1
Returns an empty sequence if stop is negative or 0.

range([start], stop[, step])

start: Starting number of the sequence.
stop: Generate numbers up to, but not including this number.
step: Difference between each number in the sequence.

Note that:
All parameters must be integers.
All parameters can be positive or negative.
range() in Python in general is 0-index based
"""
print()
for x in range(4):
    print(x)  # range(4) prints 0 - 3

# ----------------------------------------------------------------------------------------
print()
# range(2,5) prints values 2 to 5 (but not including 5)
# defaults to increment the sequence by 1
print('range(2,5)')
for x in range(2,5):
    print(x)

# ----------------------------------------------------------------------------------------
# range(2,10,3) prints values 2, 5,8
# third parameter stands for increment .(default is 1)
print()
print('range(2,10,3)')
for x in range(2,10,3):
    print(x)  #  2  5  8

# ----------------------------------------------------------------------------------------
# Else in For Loop
# The Else block is executed when the loop is finished
# Note: 1) Indentation 2) colon (:) in FOR and ELSE
print()
print('range(3)')
for x in range(3):
    print(x)
else:
    print("loop ends")
"""
Output:
0
1
2
loop ends
"""

# ----------------------------------------------------------------------------------------
# Nested Loops
platform = ["JEE", "Dot Net"]
features = ["web", "enterprise"]
print()
for x in platform:
    for y in features:
        print(x,y)

# ----------------------------------------------------------------------------------------
# break Statement
# Exit the loop when x is "python"
print()
swLang = ["java", "C#","python","Angular"]
for x in swLang:
    print(x)           # java C# python
    if x == "python":
        break

# ----------------------------------------------------------------------------------------
# break Statement
# Exit the loop when x is "python" , before printing
# Note: Indentation is important
print()
swLang = ["java", "C#","python","Angular"]
for x in swLang:
    if x == "python":
        break
        #print(x)
    print(x)     # java  c##

# ----------------------------------------------------------------------------------------
# Continue statement we can stop the current iteration of the loop, and continue with the next
print()
swLang = ["java", "C#","python","Angular"]
for x in swLang:
    if x == "python":
        continue
    print(x)     # java sC# Angular

# ----------------------------------------------------------------------------------------
# Python Program to display the powers of 2 using anonymous function
print()
#terms = 5

#  to take number of terms from user as input
terms = int(input("How many terms? "))

# display the result
print("The total terms is:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",2**i)

""" output:
The total terms is: 5
2 raised to power 0 is 1
2 raised to power 1 is 2
2 raised to power 2 is 4
2 raised to power 3 is 8
2 raised to power 4 is 16
"""

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# while Loop
# Syntax: while expression:

print()
x = 1
while x < 5:
    print(x)   # 1 2 3 4
    x += 1