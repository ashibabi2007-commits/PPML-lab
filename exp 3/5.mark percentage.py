m=int(input("enter the mark of subject 1:-"))
n=int(input("enter the mark of subject 2:-"))
o=int(input("enter the mark of subject 3:-"))
p=int(input("enter the mark of subject 4:-"))
q=int(input("enter the mark of subject 5:-"))
per=((m+n+o+p+q)/250)*100
print("the percentage is:-",per)
if(per>=90 and per<=100):
    print("the grade is O")
elif(per>=80 and per<90):
    print("the grade is E")
elif(per>=70 and per<80):
    print("the grade is A")
elif(per>=60 and per<70):
    print("the grade is B")
elif(per>=50 and per<60):
    print("the grade is C")
elif(per>=0 and per<50):
    print("fail")
else:
    print("invalid")