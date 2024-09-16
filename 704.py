from os import system
system("cls")

def search(nums:list, target) -> int:
    if target in nums:
        return nums.index(target)
    return -1

v = [-1,0,3,5,9,12]
t = 2
n = search(v,t)
print(n,type(n))