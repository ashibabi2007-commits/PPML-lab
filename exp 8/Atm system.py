r=int(input("Enter what amount is in the account: "))
c=int(input("Enter what transaction you want to do: \n 1.Deposit \n 2.Withdrawl \n 3.Balance \n***********************************************************\n"))
if c==1:
    a=int(input("Enter what amount to be deposit in the account: "))
    def deposit(d,s):
        e=s+d
        print("The amount has been deposited in your account.")
        print("The current account balance is: ",e)   
        print("***********************************************************")
    deposit(a,r)
elif c==2:
    b=int(input("Enter what amount to be withdrawl from the account: "))
    def withdraw(w,m):
        if w<r:
            f=m-w
            print("The amount has been withdrawl from your account.")
            print("The current account balance is: ",f)
            print("***********************************************************")
        else:
            print("XXXX The account has low balnce XXXX \n Hence the transaction has been declined.")
            print("***********************************************************")
    withdraw(b,r)
elif c==3:
    print("Your current balance is: ",r)
    print("***********************************************************")
else:
    print("The transaction has been declined for some technical issue.")
    print("***********************************************************")

print("\n\n:)Thank you:)")
print("***********************************************************")
print("***********************************************************")