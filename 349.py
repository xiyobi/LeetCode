from os import system
system("cls")

def intersection(nums1:list,nums2:list):
    return set(nums1).intersection(set(nums2))
s = [1,2,2,3]
d = [2,2]
print(intersection(s,d))