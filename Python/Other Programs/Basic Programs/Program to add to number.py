# There are many ways we can add two number

a = 1
b = 3
c = a+b
print(c)
print(a+b)
a,b=3,3
print(a+b)


a=int(input("Enter num 1 : "))
b = int(input("Enter num 2 : "))
sum = a+b
print(sum)
print(a+b)

def sumofnumber(a,b):
    print(a+b)
sumofnumber(2,2)

import operator
a = 2
b = 32
result = operator.add(a,b)
print(result)


# using lambda function
new = lambda x,y:x+y
num1 = 2
num2 =6
result = new(num1,num2)
print(result)