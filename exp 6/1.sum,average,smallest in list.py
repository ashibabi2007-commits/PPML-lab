l=["apple","banana","mango"]
print("fruits displayed from last to first indx with their lengthsL:-")
for i in l[::-1]:
    print(i,"-length:",len(i))
print("\n list containing reverse of each fruit name:-")
rev=[]
for fruit in l:
    rev.append(fruit[::-1])
print(rev )