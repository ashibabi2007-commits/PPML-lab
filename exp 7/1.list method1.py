m=int(input("enter m:"))
n=-int(input("enter n:"))
lst=[]
for i in range(m,n+1):
    lst.append(i)
print("list:",lst)
print("sum:",sum(lst))
print("average:",sum(lst)/len(lst))
print("largest:",max(lst))
print("smallest",min(lst))