# A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. 
# Create a function to convert grams to ounces. ounces = 28.3495231 * grams

grams = int(input("введите граммаж: "))
def ounces_to_grams(grams):
    ounces = 28.3495231 * grams
    return ounces
ounces = ounces_to_grams(grams)
print(ounces)


# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)

F = float(input())

def F_to_C(F):
    C = (5/9) * (F - 32)
    return C

C = F_to_C(F)
print(C)

# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2 * chickens + 4 * rabbits == legs:
            return chickens, rabbits
    return None

heads, legs = 35, 94
solution = solve(heads, legs)

if solution:
    chickens, rabbits = solution
    print({chickens}, {rabbits})
else:
    print("No solution found.")


# You are given list of numbers separated by spaces. 
# Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtered_num(numbers):
    return [num for num in numbers if prime(num)] #квадратные скобки - список -> если это число простое, то выполняем


numbers = int(input())
prime_numbers = filtered_num = (numbers)

print(numbers, "was filtered into", prime_numbers)




# Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations  #itertools - библиотека функций; permutations - перестановки

def print_permutations(input_string):
    perms = permutations(input_string) # лист????

    for perm in perms:
        print(perm, end = " ") #для вывода через пробел разные значения
        
        
user_input = input("Enter a string: ")

print("All Permutations:")
print_permutations(user_input)

    
#Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

from itertools import permutations

def print_permutations(input_string):
    perms = permutations(input_string)
    
    
    
    
    
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] and nums[i] == 3:
            return True
    return False

has_33([1, 3, 3]) # True
has_33([1, 3, 1, 3]) # False
has_33([3, 1, 3]) # False


# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            for j in range(i + 1, n):
                if nums[j] == 0:
                    for h in range(j + 1, n):
                        if nums[h] == 7:
                            return True
    return False

spy_game([1,2,4,0,0,7,5]) # --> True
spy_game([1,0,2,4,0,5,7]) # --> True
spy_game([1,7,2,0,4,5,0]) # --> False


# Write a function that computes the volume of a sphere given its radius.

def fvolume(r):
    volume = 4/3 * 3,14 * r ** 3
    return volume
r = int(input())
Volume = fvolume(r)
print (Volume)

# Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:

def histogram(nums):
    for i in nums:
        print('*' * i) 
        
        
# Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:

def vsedelatsrazu():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess.")
    
