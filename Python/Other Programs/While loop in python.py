#This is a function problem. You need to complete the printInDecreasing() function and print the x from x to 0 in a single line.

def printInDecreasing(x):
    # Complete the code below
    while(x >= 0):
        print(x,end=" ")        
        x -= 1
printInDecreasing(4)