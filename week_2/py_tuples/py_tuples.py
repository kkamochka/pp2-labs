Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)



Allow Duplicates
Since tuples are indexed, they can have items with the same value:

Example
Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)



Tuple Length
To determine how many items a tuple has, use the len() function:

Example
Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))



Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

Example
One item tuple, remember the comma:   !!!!!

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))



Tuple Items - Data Types
Tuple items can be of any data type:

Example
String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")       ('abc', 34, True, 40, 'male')


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))             <class 'tuple'>



The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.

Example
Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



Access Tuple Items











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