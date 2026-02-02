def largest(a,b,c):
    return a if (a>=b and a>=c) else b if (b>=c) else c
a=int(input("Enter first number:-"))
b=int(input("Enter second number:-"))
c=int(input("Enter second number:-"))
print("Largest among these three numbers is",largest(a,b,c))