n=input("Enter the bnumber:")
rev=0
while n>0:
    rev=(rev*10)+(n%10)
    n//=10
print("The reversed number is :",rev)