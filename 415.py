from os import system
system("cls")

def toHex(s:int):
    d = ''
    if s < 0:
        s = (s**32) + s
    if s == 0: 
        return "0"
    while s!= 0:
        if s % 16 == 10:
            d += 'a'
        elif s % 16 == 11:
            d += 'b'
        elif s % 16 == 12:
            d += 'c'
        elif s % 16 == 13:
            d += 'd'
        elif s % 16 == 14:
            d += 'e'
        elif s % 16 == 15:
            d += 'f'
        else:
            x = s % 16
            d += str(x)
        s //= 16
    return d[::-1]
d = -2
print(toHex(d))
