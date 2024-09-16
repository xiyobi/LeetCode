def canConstruct(s:str,r):
    dct = {}
    dct2 = {}
    for i in list(s):
        dct[i] = s.count(i)
    for j in list(r):
        dct2[j] = r.count(j)
    return dct==dct2
s = "a"
t = "b"
print(canConstruct(s,t))
