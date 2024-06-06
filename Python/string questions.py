#You are given a string, 'S'. You need to write a function called 'gfg' that takes 'S' as input and checks if the string starts and ends with the substring 'gfg'.

def gfg(S):
    b = S.lower()
    if(b[0:3]=="gfg" and b[-3:]=="gfg"):  
        print ("Yes")
    else:
        print ("No")

gfg("gfgevilgfg")