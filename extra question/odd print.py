n=int(input("Enter a 5 digit number:-"))
while n>10000 and n<99999:
    digit=n%10
    n=digit
    if n%2!=0:
        print(n)
    else:
        print(n,"not a odd number")  