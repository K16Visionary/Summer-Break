# we can find the maximum of two number in variour ways 

num1=2
num2=6
if num1>=num2:
    print("Num1 is greater than num2")
else:
    print("NUm2 is greater")

import math
num1=9
num2=6
max = max(num1,num2)
print(max," is Maximum")


#using ternary operator
a = 2
b = 8
print("A is greater" if a > b else "B is greater")


# using lambda function
a=2;b=4
maximum = lambda a,b:a if a > b else b
print(maximum)