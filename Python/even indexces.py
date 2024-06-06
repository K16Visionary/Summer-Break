#You are given a string str, you need to print its characters at even indices(index starts at 0)


def stringJumper(str):
    for i in range(len(str)): ## from 0 to length of str and skip 2
        if i % 2 == 0:
            print(str[i],end=" ") 
stringJumper("Heellooo")