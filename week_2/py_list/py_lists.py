

# # Python Lists


# # mylist = ["apple", "banana", "cherry"]

# # thislist = ["apple", "banana", "cherry"]    "apple", "banana", "cherry"
# # print(thislist)

# # thislist = ["apple", "banana", "cherry", "apple", "cherry"]       "apple", "banana", "cherry", "apple", "cherry"
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # print(len(thislist))  3

# # list1 = ["apple", "banana", "cherry"]
# # list2 = [1, 5, 7, 9, 3]
# # list3 = [True, False, False]


# # list1 = ["abc", 34, True, 40, "male"]


# # mylist = ["apple", "banana", "cherry"]           <class 'list'>
# # print(type(mylist))  

# # thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# # print(thislist)

# # -------------------------------------------------------

# # Python - Access List Items

# # hislist = ["apple", "banana", "cherry"]
# # print(thislist[1])     banana

# # thislist = ["apple", "banana", "cherry"]
# # print(thislist[1])

# # thislist = ["apple", "banana", "cherry"]
# # print(thislist[-1])

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[2:5])

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[:4])

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[2:])

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[-4:-1])

# # thislist = ["apple", "banana", "cherry"]
# # if "apple" in thislist:
# #   print("Yes, 'apple' is in the fruits list")

# # ---------------------------------------------------------------------------------
# Python - Change List Items

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
# # ---------------------------------------------------------------------------------
# Add List Items

# Using the append() method to append an item:

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# Insert an item as the second position:

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# Add the elements of tropical to thislist:

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# Add elements of a tuple to a list:

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# # ---------------------------------------------------------------------------------

# Remove List Items

# Remove "banana":

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# Remove the first occurance of "banana":

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# Remove the second item:

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)                 ["apple", "cherry"]


# Remove the last item:

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)        ["apple", "banana"]

# Remove the first item:

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)      ['banana', 'cherry']

# Delete the entire list:

# thislist = ["apple", "banana", "cherry"]
# del thislist

# Clear the list content:

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# # ---------------------------------------------------------------------------------
# Loop Lists

# Print all items in the list, one by one:

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
  
# Print all items by referring to their index number:

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])
  
  
# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

# Example
# Print all items, using a while loop to go through all the index numbers

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1
  
  
# A short hand for loop that will print all items in a list:

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]
# # ---------------------------------------------------------------------------------

# List Comprehension

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# Condition
# The condition is like a filter that only accepts the items that valuate to True.

# Example
# Only accept items that are not "apple":

# newlist = [x for x in fruits if x != "apple"]


# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

# The condition is optional and can be omitted:

# Example
# With no if statement:

# newlist = [x for x in fruits]



# You can use the range() function to create an iterable:

# newlist = [x for x in range(10)]



# Accept only numbers lower than 5:

# newlist = [x for x in range(10) if x < 5]



# Set the values in the new list to upper case:

# newlist = [x.upper() for x in fruits]

# Set all values in the new list to 'hello':

# newlist = ['hello' for x in fruits]


# Return "orange" instead of "banana":

# newlist = [x if x != "banana" else "orange" for x in fruits]

# ---------------------------------------------------------------------------------
# Sort Lists

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:


# Sort the list alphabetically:

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)



# Sort the list numerically:

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)



# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# Example
# Sort the list descending:

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)


# Sort the list descending:

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)


# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):

# Example
# Sort the list based on how close the number is to 50:

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Example
# Case sensitive sorting can give an unexpected result:

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


# Example
# Perform a case-insensitive sort of the list:

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


# Reverse the order of the list items:

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# ---------------------------------------------------------------------------------
# Copy Lists

# Make a copy of a list with the copy() method:

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# Make a copy of a list with the list() method:

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# ---------------------------------------------------------------------------------
# Join Lists

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)


# Use the extend() method to add list2 at the end of list1:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)


# ---------------------------------------------------------------------------------
# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] ="kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))