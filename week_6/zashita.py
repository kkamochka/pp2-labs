# 1. вытащиь все 2значные числа 
# 10 20 21 30 31 32 40 41 42 43 50 51 52 53 54 60 61 62 63 64 65 70 7
# for i in range (0, 100):
#     if i%10 < i//10:
#         print (i, end = " ") 
        
class MyNumbers:
    def __init__(self, N):
        self.N = N   # указываем до какого числа дойти
    
    def __iter__(self):
        self.num = 10    
        return self

    def __next__(self):
        if self.num <= self.N:   # проверка до какого числа 
            x = ""
            if self.num % 10 < self.num//10: 
                x = self.num
            self.num +=1  # продвигаем число дальше
            return x
        else:
          raise StopIteration


Class = MyNumbers(99)  
iterator = iter(Class) 

for i in iterator:
   if i != "":
       print(i, end =" ") 
    
        

print()
# # 2. dir(lecture, txt)
# yes or no типо если или нет в этой папке этот файл

import os 
def dir(path):
    if os.access(path, os.F_OK):    #F_OK - существует ли в папке файл 
        print ("YES")
    else:
        print("NO")


direct = os.getcwd()
check1 = os.path.join(direct, "proverka.txt")
check2 = os.path.join(direct, "proverka2.txt") 
dir(check1)
dir(check2)

