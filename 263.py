from os import system 
system("cls")

def isUgly(s):
    if s <= 0:
        return 0
    for i in [2,3,5]:
        while s % i == 0:
            s //= i
    return s == 1
    
print(isUgly(6))