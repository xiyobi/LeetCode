from os import system
system("cls")

def maximumProduct(nums:list) -> int:
    d = 1
    count = 1
    nums.sort(reverse=True)
    for i in nums:
        d *= i
        print(d)
        if count == 3:
            return d
        count += 1
s = [-100,-98,-1,2,3,4]
maximumProduct(s)