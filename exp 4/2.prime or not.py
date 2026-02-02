import math
n=int(input("enter the number :-"))
if n<=1:
    print(f"{n} is a prime number")
else:
    i=2
    while i<=math.sqrt(n):
        if n%i==0:
            print("not a prime number")
            break
        i+=1
    else:
        print(f"{n} is a prime")