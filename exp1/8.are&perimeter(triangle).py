a=int(input("enter the height"))
b=int(input("enter the breadth"))
c=int(input("enter the width"))
s=(a+b+c)/2
print("the perimeter=",a+b+c)
print("the area=",(s*(s-a)*(s-b)*(s-c)**0.5))