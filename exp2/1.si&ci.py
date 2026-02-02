p=int(input("enter principal value:"))
t=int(input("enter time period value:"))
r=int(input("enter rate of interest value:"))
si=(p*t*r)/100
print("the simple interest is:",si)
n=int(input("enter the no. of times the interest is being compounded: "))
ci=p*(1+(r/n)**(n*t))
print("the compound interest is:",ci)
