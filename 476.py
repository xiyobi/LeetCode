from os import system
system("cls")

def findComplement(num: int):
    x = ''
    d = bin(num)[2:]
    for i in list(d):
        if i == "0":
            x += "1"
        else:
            x += "0"
    return int(x,2)

n = 5
print(findComplement(n))