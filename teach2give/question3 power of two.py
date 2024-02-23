#Write a program that takes an integer as input and returns true if the input is a power of two.

import math
i=int(input("enter the integer :"))
def power2():
    return i>0 and math.log2(i).is_integer() 
print(power2())    