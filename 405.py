def fizzBuzz(n: int):
        s, x,f = "Fizz", "Buzz","FizzBuzz"
        d = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                d.append(f)
            elif i % 3 == 0:
                d.append(s)
            elif i % 5 == 0:
                d.append(x)                
            else:
                d.append(str(i))
        return d 
n = 15
print(fizzBuzz(n))
