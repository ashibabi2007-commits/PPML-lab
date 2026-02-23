import math
n=int(input("Enter the number:"))
if n<=1:
    print("not a prime number")
else:
    i=2
    while i<=math.sqrt(n):
        if n%i==0:
            print(f"{n} is not prime")
            break
        i=i+1
    else:
        print(f"{n} is a prime")