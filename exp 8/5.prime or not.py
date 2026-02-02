def primecheck(a):
    for i in range(2,a):
        if a%1==0:
            return "not"
        return ''
a=int(input("Enter anumber:-"))
print(f"{a} is {primecheck (a)} a primenumber")
                
        