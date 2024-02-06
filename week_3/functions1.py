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
    return [num for num in numbers if prime(num)]


numbers = int(input())
prime_numbers = filtered_num = (numbers)

print(numbers, "was filtered into", prime_numbers)

