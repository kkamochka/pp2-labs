# Create a Tuple:

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)



# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# Example
# Tuples allow duplicate values:

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)



# Tuple Length
# To determine how many items a tuple has, use the len() function:

# Example
# Print the number of items in the tuple:

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))



# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example
# One item tuple, remember the comma:   !!!!!

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))



# Tuple Items - Data Types
# Tuple items can be of any data type:

# Example
# String, int and boolean data types:

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)


# A tuple with strings, integers and boolean values:

# tuple1 = ("abc", 34, True, 40, "male")       ('abc', 34, True, 40, 'male')


# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))             <class 'tuple'>



# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

# Example
# Using the tuple() method to make a tuple:

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)


# ---------------------------------------------------------------------------------
# Access Tuple Items

# Print the second item in the tuple:

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])


# Print the last item of the tuple:

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])



# Return the third, fourth, and fifth item:

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])



# This example returns the items from the beginning to, but NOT included, "kiwi":

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])


# This example returns the items from index -4 (included) to index -1 (excluded)

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])



# Check if "apple" is present in the tuple:

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")
# ---------------------------------------------------------------------------------
# Update Tuples

# Convert the tuple into a list to be able to change it:

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)


# Convert the tuple into a list, add "orange", and convert it back into a tuple:

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)


# Create a new tuple with the value "orange", and add that tuple:

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)



# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# Example
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)



# The del keyword can delete the tuple completely:

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)
# ---------------------------------------------------------------------------------
# Unpack Tuples

# Packing a tuple:

# fruits = ("apple", "banana", "cherry")


# Unpacking a tuple:

# fruits = ("apple", "banana", "cherry")       apple
# (green, yellow, red) = fruits                banana
#                                              cherry
# print(green)
# print(yellow)
# print(red)



# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example
# Assign the rest of the values as a list called "red":

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)



# Add a list of values the "tropic" variable:

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# # ---------------------------------------------------------------------------------
# Loop Tuples

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

# Example
# Iterate through the items and print the values:

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)
  
  
  
#   You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

# Example
# Print all items by referring to their index number:

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])
  
  
  
# Print all items, using a while loop to go through all the index numbers:

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1
# ---------------------------------------------------------------------------------
# Join Tuples

# Join two tuples:

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)


# Multiply the fruits tuple by 2:

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# ---------------------------------------------------------------------------------

# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
# ---------------------------------------------------------------------------------

  


# Use the correct syntax to print the first item in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(fruits[0])

# Use the correct syntax to print the number of items in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Use negative indexing to print the last item in the tuple.

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# Use a range of indexes to print the third, fourth, and fifth item in the tuple.

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])