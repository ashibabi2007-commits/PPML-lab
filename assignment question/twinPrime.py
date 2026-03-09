#wap to print twin prime numbers between 1 to n
n=int(input("Enter the number:"))
for i in range(2,n):
    d=0
    for j in range(1,i+1):
        if i%j==0:
            d=d+1
    if d==2:
        d=0
        n=i+2
        for j in range(1,n+1):
            if n%j==0:
                d=d+1
    if d==2:
        print("(%d,%d)"%(i,n))