# Create a generator that generates the squares of numbers up to some number N.

class MyNumbers:
    def __init__(self, N):
        self.N = N
    
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= self.N:
          x = self.num * self.num
          self.num += 1
          return x
        else:
          raise StopIteration


Class = MyNumbers(10)
iterator = iter(Class)

for i in iterator:
   print(i)
   
   
# Write a program using generator to print the even numbers between 0
# and n in comma separated form where n is input from console.

class MyNumbers:
    def __init__(self, num):
        self.n = num

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
         if self.num <= self.n:
            x = self.num
            self.num += 2
            return ", " * bool(x) + str(x)
         else:
            raise StopIteration


num = int(input())
Class = MyNumbers(num)
iterator = iter(Class)

for i in iterator:
    print(i, end="")
    
    
    
# Define a function with a generator which can iterate the numbers,
# which are divisible by 3 and 4, between a given range 0 and n.

class MyNumbers:
    def __init__(self, num):
        self.n = num

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
         if self.num <= self.n:
            x = self.num
            self.num += 1
            if x % 4 == 0 or x % 3 == 0:
                return ", " * bool(x) + str(x)
            else:
                return ""
         else:
            raise StopIteration


num = int(input())
Class = MyNumbers(num)
iterator = iter(Class)

for i in iterator:
    print(i, end="")
    


# Implement a generator called squares to yield the square of all numbers from (a) to (b).
# Test it with a "for" loop and print each of the yielded values.

def square_y(a, b):
    for i in range(a, b + 1):
        yield i * i


a, b = map(int, input().split())

list = square_y(a, b)
print(*list)


for i in range(a, b + 1):
    print(i * i, end=" ")
    
    
# Implement a generator that returns all numbers from (n) down to 0.

def implementor(n):
    for i in range(n, -1, -1):
        yield i


n = int(input())
list = implementor(n)
print(*list)
    
    
    
    