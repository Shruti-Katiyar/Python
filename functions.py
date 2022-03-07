


# categories of function
# 1. built-in
# 2.modules
# 3.user-defined

                   #Modules  

# math
# random
# string

import math
print(math.pi)


import math as m
print(m.pi)
print(m.cos(3.14))

from math import cos
print(cos(3.14))

from math import cos,sin #only cos or sin are define

print(cos(3.14))
print(sin(3.14))

                  #To import all the function use *
from math import *
print(cos(3.14))
print(pi)



                   #user define fun

def solve():
    print('welcome')

solve() 
solve()    

#parameters
def solve1(name):
    print('good mrng ', name)

solve1("shruti")    

def solve2(name ,dish):
    print('good mrng ', name)
    print('plz eat ',dish)

solve2("shruti" ,"pasta")    

#optional arrgument
def a(name ,dish="piza"):
    print('good mrng ', name)
    print('plz eat ',dish)

a("shruti")   


              #returning the function
def sum_list(x):
    print("calculating...........")
    
    return sum(x)

marks=[33,55,77,11,22]
y=sum_list(marks)

print(y)



def greetings(names):
    for name in names:
        print("hello" , name)


names=["shruti" ,"shivu "," rashi"]
greetings(names)        




