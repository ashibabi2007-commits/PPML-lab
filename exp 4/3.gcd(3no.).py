a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
while b!=0:
    temp=a
    a=b
    b=temp%b
while c!=0:
    temp=a
    a=c
    c=temp%c
print("GCD is :-",a)