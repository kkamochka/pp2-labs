# Define a class which has at least two methods: getString: to get a string from console input 
# printString: to print the string in upper case.


class String:
    def __init__(self):   #__init__ — это специальная функция, которая вызывается при создании нового объекта класса.
        self.input_string = ""   #self — это ссылка на текущий экземпляр класса. Это способ обращения к атрибутам и методам класса изнутри самого класса.


    def getString(self): 
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())


task = String()
task.getString()
task.printString()


# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self) : #init function which takes a length as argument. !!!
        pass
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def Area(self):
        return self.length * self.length
   
   
Shape = Shape() 
print(Shape.Area())

Square = Square()
print(Square.Area())



# Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shape = Shape()
print(shape.area())

rectangle = Rectangle(input())
print(rectangle.area())




# Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
# Withdrawals may not exceed the available balance. 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print({amount}, {self.balance})

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print({amount}, {self.balance})
        else:
            print(nin)


