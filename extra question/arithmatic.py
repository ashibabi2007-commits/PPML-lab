n=int(input("Enter a number:"))
n1=int(input("Enter another number:"))

def arithmatic(a,b):
    sum=a+b
    sub=a-b
    mult=a*b
    div=a/b
    flor=a//b
    rem=a%b
    print("The sum is:",sum)
    print("The sub is:",sub)
    print("The mult is:",mult)
    print("The div is:",div)
    print("The flor is:",flor)
    print("The rem is:",rem)
arithmatic(n,n1)
