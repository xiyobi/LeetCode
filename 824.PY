def toGoatLatin(s: str) -> str:
    z = ''
    count = 2
    Dm,Da = 'm','a'
    d = s.split()
    for i in d:
        if i == 'a' or i == 'i' or i == 'e' or i == 'u' or i == 'o' or i == 'A' or i == 'I' or i == 'E' or i == 'U' or i == 'O':
            z += i+Dm + Da*count +' '
            count += 1
        if not (i == 'a' or i == 'i' or i == 'e' or i == 'u' or i == 'o' or i == 'A' or i == 'I' or i == 'E' or i == 'U' or i == 'O' ):
            i = i[1:] + i[0]
            z += i+Dm + Da*count +' '
            count += 1
    return z[:-1]

print(toGoatLatin("The quick brown fox jumped over the lazy dog"))