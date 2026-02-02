n=int(input("enter the number:-"))
if n<0:
    print("factorial not defined") 
else:
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    print("factorial is",fact)