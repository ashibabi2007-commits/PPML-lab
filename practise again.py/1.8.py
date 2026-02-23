a=int(input("Enter the side:"))
b=int(input("Enter the side:"))
c=int(input("Enter the side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
perimeter=a+b+c
print("Area is",area)
print("perimeter is",perimeter)
