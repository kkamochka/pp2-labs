Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.


Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.


# Duplicate values will be ignored:

# thisset = {"apple", "banana", "cherry", "apple"} !!!!!!!!!

# print(thisset)


# True and 1 is considered the same value:

# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)



# False and 0 is considered the same value:

# thisset = {"apple", "banana", "cherry", False, True, 0}

# print(thisset)



# Get the Length of a Set
# To determine how many items a set has, use the len() function.

# Example
# Get the number of items in a set:

# thisset = {"apple", "banana", "cherry"}

# print(len(thisset))



# Set Items - Data Types
# Set items can be of any data type:

# Example
# String, int and boolean data types:

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}



# A set with strings, integers and boolean values:

# set1 = {"abc", 34, True, 40, "male"}


# What is the data type of a set?

# myset = {"apple", "banana", "cherry"}
# print(type(myset))


# Using the set() constructor to make a set:

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# --------------------------------------------------------------------------------
# Access Set Items

# Loop through the set, and print the values:

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
  
  
# Check if "banana" is present in the set:

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

# # ----------------------------------------------------------------------------

# Add Set Items

# Add an item to a set, using the add() method:

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)



# Add elements from tropical into thisset:

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)


# Add elements of a list to at set:

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

# # --------------------------------------------------------------------------------
# Remove Set Items

# Remove "banana" by using the remove() method:

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)



# Remove "banana" by using the discard() method:

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

# Example
# Remove a random item by using the pop() method:

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)


# The clear() method empties the set:

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()

# print(thisset)



# The del keyword will delete the set completely:

# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset)

# # -------------------------------------------------------------------------------
# Loop Sets

# Loop through the set, and print the values:

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
# # -------------------------------------------------------------------------------

# Join Sets

# The union() method returns a new set with all items from both sets:

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)


# The update() method inserts the items in set2 into set1:

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)


# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.

# Example
# Keep the items that exist in both set x, and set y:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.

# Example
# Return a set that contains the items that exist in both set x, and set y:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)


# Keep the items that are not present in both sets:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)

# !!!The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.!!!

# Return a set that contains all items from both sets, except items that are present in both:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)

# print(z)

# True and 1 is considered the same value:

# x = {"apple", "banana", "cherry", True}
# y = {"google", 1, "apple", 2}

# z = x.symmetric_difference(y)

# print(z)


# Set Methods

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others





# Check if "apple" is present in the fruits set.


fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
# Use the add method to add "orange" to the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# Use the correct method to add multiple items (more_fruits) to the fruits set.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# Use the remove method to remove "banana" from the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# Use the discard method to remove "banana" from the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")