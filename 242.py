def isAnagram(s:str, t:str):
    dcS = {}
    for i in list(s):
        dcS[i] = s.count(i)    
    dcT = {}
    for i in list(t):
        dcT[i] = t.count(i)
    return dcS == dcT
   
s = "anagram"
t = "nagaram"
print(isAnagram(s,t))