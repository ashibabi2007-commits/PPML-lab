#wap to check whether the stringf is symmetrical or palindrome...................................................................................................
x=input("Enter a string:")
z=(str(str(x)[::-11]))
if x==z:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
    