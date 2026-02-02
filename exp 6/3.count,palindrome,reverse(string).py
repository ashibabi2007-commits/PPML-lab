i=input("enter a sentence:-")
list1=i.split()
print("\n elements of list1 with index are:-")
for i,w in enumerate(list1):
    print(i,w)
list2=list(range1, len(list1)+1)
list3=list(zip,(list1,list2))
print("\n combined list 3 using zip:-")
print(list3)
