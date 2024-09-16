from os import system
system("cls")

def countSegments( s: str) -> int:
    
    return (len(s.split()))
v = "Hello, my name is John"
print(countSegments(v))