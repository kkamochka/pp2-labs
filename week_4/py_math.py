# Write a Python program to convert degree to radian.

print("Input degree: ", ) 
a = int(input())
print("Output radian: ", a*0.0174533 )




# Write a Python program to calculate the area of a trapezoid.

class Area():
    def _init_(self):
        pass
class Trapezoid(Area):
    def _init_(self, height, base1, base2):
        self.height = height
        self.base1 = base1
        self.base2 = base2
        
    def solving(self):
        print( (self.base1 + self.base2)/2 *self.height )

Data = Trapezoid(6, 5, 5)
Data.solving() 

# Write a Python program to calculate the area of regular polygon.
import math 

def calculate_polygon_area(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

sides = int(input())
length = float(input())

Area = calculate_polygon_area(sides, length)

print ("The area of the polygon is: ", Area)