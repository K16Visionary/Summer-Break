#Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).


def printIncreasingPower(x):
    start = 1
    while start < x:
        n = start*start
        if n >= x:
            break
        print(n, end=" ")
        start += 1

printIncreasingPower(10)
