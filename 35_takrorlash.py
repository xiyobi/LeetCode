from os import system 
system("cls")

def searchInsert(nums: list, target: int):
    if target in nums:
        return nums.index(target)
    for i in range(len(nums)):
        if target < nums[i]:
            return i
n = [1,3,6]
print(searchInsert(n,2))