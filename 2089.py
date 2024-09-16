from os import system
system("cls")

def targetIndices(nums:list, target: int):
    n = []
    nums.sort()
    for i in range(len(nums)):
        if target == nums[i]:
            n.append(i)
    return n

n = [1,2,5,2,3]
y = 2
n = targetIndices(n,y)
print(n)