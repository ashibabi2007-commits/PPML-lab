#wap to create an integer list of 20 elements incerease the odd valued elements by 5
s=[]
x=int(input("Enmter the number of elements:"))
for i in range(x):
    if s[i]%2!=0:
        s[i]=s[i]+5
print(s)
        