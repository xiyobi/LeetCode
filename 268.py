from os import system
system("cls")
def  missingNumber(nums:list)->int:
    n = len(nums)
    x = n*(n+1)//2
    return x - sum(nums)

s = [0,1]
son = missingNumber(s)
print(son)