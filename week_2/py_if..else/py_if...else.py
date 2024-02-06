# If ... Else

# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

# If statement:

# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")
  
  
# If statement, without indentation (will raise an error):

# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error


# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# Example
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
  
  
  
# Else
# The else keyword catches anything which isn't caught by the preceding conditions.

# Example
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
  
  
# Example
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")
  
  
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

# Example
# One line if statement:

# if a > b: print("a is greater than b")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# Example
# One line if else statement:

# a = 2
# b = 330
# print("A") if a > b else print("B")


# Example
# One line if else statement, with 3 conditions:

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")


# And
# The and keyword is a logical operator, and is used to combine conditional statements:

# Example
# Test if a is greater than b, AND if c is greater than a:

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
  
  
  
# Or
# The or keyword is a logical operator, and is used to combine conditional statements:

# Example
# Test if a is greater than b, OR if a is greater than c:

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")
  
  
# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

# Example
# Test if a is NOT greater than b:

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")
  



# Nested If
# You can have if statements inside if statements, this is called nested if statements.

# Example
# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")
    
    
    
# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

# Example
# a = 33
# b = 200

# if b > a:
#   pass



    



# Print "Hello World" if a is greater than b.

a = 50
b = 10
if a > b:
    print("Hello World")
    
# Print "Hello World" if a is not equal to b.

a = 50
b = 10
if a != b:
    print("Hello World")
    
# Print "Yes" if a is equal to b, otherwise print "No".


a = 50
b = 10
if a == b:
    print("Yes")
else:
  print("No")
  
# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".


a = 50
b = 10
if a == b:
    print("1")
elif a > b:
  print("2")
else:
  print("3")
  
# Print "Hello" if a is equal to b, and c is equal to d.

c = 10
d = 20

if a == b and c == d:
  print("Hello")
  
# Complete the code block, print "YES" if 5 is larger than 2.
# Hint: remember the indentation.


if 5 > 2:
    print("YES")
    
# Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").

a = 2
b = 5
print("YES") if a==b else print("NO")

# Use an if statement to print "YES" if either a or b is equal to c.


a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")
  
  