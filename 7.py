from os import system
system("cls")

def reverse(x: int) -> int:
        if x > ((2**30)-1) or 0 > ((2**30)-1):
            return 0
        elif x >= 0:
            son = str(x)[::-1]
            return int(son) 
        else:
            son = str(x)[:0:-1]
            y = int(son) * (-1)
            return y
d = 123
print(reverse(d))