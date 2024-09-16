from os import system
system("cls")
def removeElement(nums:list,n:int)->int:
    k = 0
    for i in range(len(nums)):
        if not n == nums[i]:
            nums[k] = nums[i]
            k += 1
    return k
n = [0,1,2,2,3,0,4,2]
x = 2

natija = removeElement(n,x)
print(natija)