n=int(input("enter a number: "))
m=int(input("enter second number: "))
f=int(input("enter the third number: "))
def largest(a,b,c):
    if(a>b and a>c):
        print("the largest number is: ",a)
    elif(b>a and b>c):
        print("the largest number is: ",b)
    else:
        print("the largest number is: ",c)    
largest(n,m,f)