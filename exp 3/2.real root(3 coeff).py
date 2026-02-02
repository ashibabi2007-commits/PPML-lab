import math
a=int(input("enter the number:-"))
b=int(input("enter the number:-"))
c=int(input("enter the number:-"))
d=b*b-4*a*c
if(d>0):
    r1=(-b + math.sqrt(d))/(2*a)
    r2=(-b - math.sqrt(d))/(2*a)
    print("the two real roots are:-",r1,r2)
elif(d==0):
    r=-b/(2*a)
    print("one root is:-",r)
else:
    print("no roots")