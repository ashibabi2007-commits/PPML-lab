m1=float(input("Enter the mark:"))
m2=float(input("Enter the mark:"))
m3=float(input("Enter the mark:"))
m4=float(input("Enter the mark:"))
m5=float(input("Enter the mark:"))
p=((m1+m2+m3+m4+m5)/500)*100
print("the percentage is:",p)
if p>=90 and p<=100:
    print("grade is:O")
elif p>=80 and p<=90:
    print("grade is:E")
elif p>=70 and p<=80:
    print("grade is:A")
elif p>=80 and p<=70:
    print("grade is:B")
elif p>=70 and p<=60:
    print("grade is:C")
elif p>=60 and p<=50:
    print("grade is:D")
else:
    print("fail")