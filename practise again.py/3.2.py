import math
a=int(input("Enter the coefficient:"))
b=int(input("Enter the coefficient:"))
c=int(input("Enter the coefficient:"))
d=((b*b)-4)*a*c
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("Two real roots:",r1,r2)
elif(d==0):
    r1=-b/(2*a)
    print("one root is:",r1)
else:
    print("no root found")