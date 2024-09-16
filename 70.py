from os import system
system("cls")

def zinamazina(n:int)->int:
    one,two = 1,1
    for i in range(n-1):
        temp = one
        # print(one)
        # print(two)
        one  = one + two
        two = temp
    return one
n = 5
print(zinamazina(n))