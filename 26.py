from os import system
system("cls")

def removeDuplicates(nums):
    
    n = list(set(nums))
    nums.clear()
    for i in n:
        nums.append(i)
    nums.sort()
    return len(nums)

n = [1,1,2]
print(removeDuplicates([1,1,2]))