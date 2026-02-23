import math
def prime(a):
    if i<=1:
        print("not a prime number")
    else:
        i=2
        while i<=math.sqrt(a):
            if a%i==0:
                print(f"{a} is not prime")
                break
            i=i+1
        else:
            print(f"{a} is a prime")
prime(34)