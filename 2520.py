def countDigits(num: int) -> int:
    tem = num
    if num < 10:
        return 1
    d = list(set(map(lambda num: int(num), str(num))))
    count = 0
    for j in d:
        if tem % j == 0:
            count += 1                
    return count

x = 54
print(countDigits(x))