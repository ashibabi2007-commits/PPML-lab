l=[]
n=int(input("enter numbers of elements:-"))
for i in range(n):
    l.append(int(input()))
l=list(set(l))
l.sort()

print("the list is:",l)