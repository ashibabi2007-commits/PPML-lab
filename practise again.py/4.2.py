a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
c=int(input("enter the number 3:"))
while b!=0:
    temp=a
    a=b
    b=temp%b
while c!=0:
    temp=a
    a=c
    c=temp%c
print("gcd is",a)