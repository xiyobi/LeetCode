from os import system
system("cls")
def firstUniqChar(s:str):
   for i in s:
        if s.count(i)==1:
             return s.index(i)
        if not s.count(i)==1:
            return -1
s = "leet"
print(firstUniqChar(s))
