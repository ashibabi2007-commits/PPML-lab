n=int(input("Enter the number:"))
original=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
if original==reverse:
    print(f"{n} is palindrome")
else:
    print(f"{n} is not a palidrome")