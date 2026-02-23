n=int(input("Enter a number:"))
a=0
b=1
count=0
while count<n:
    print(a,end="")
    temp=a
    a=b
    b=temp+b
    count+=1
    