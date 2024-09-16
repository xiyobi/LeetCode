from os import system
system("cls")

def thirdMax(nums:list):
    g = list(set(nums))
    if len(g) < 3:
        return max(g)
    else:
        g.sort(reverse=True)
        return g[2]
n = [2,2,3,1]
print(thirdMax(n))