from os import system
system("cls")
def getCommon(nums1:list, nums2:list):
    i, j = 0 , 0
    n , m = len(nums1), len(nums2)
    while i < n and j < m:
        if nums1[i] == nums2[j]:
            return nums1[i]
        if nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return -1 

n1 = [1,2,3]
n = [2,5]
n = getCommon(n1,n)
print(n)



""" for i in nums1:
        if i in nums2:
            return i
    return -1"""