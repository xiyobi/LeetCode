def convertDateToBinary(date: str) -> str:
    s = date.split("-")
    d  = ''
    for i in s:
        b = (bin(int(i)))[2:]
        d += str(b) + "-"
    return d[:-1]
k = "2080-02-29"
print(convertDateToBinary(k))