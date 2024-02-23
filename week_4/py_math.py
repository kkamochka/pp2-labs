
print("Input degree: ", a = int(input())) 
print("Output radian: ", a*0.0174533 )

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