#wap to create a function that takes list as argument and returns the even values if the list.print the new list with even values.
def even_len(n):
    s=[]
    for i in n:
        if i%2==0:
            s.append(i)
    return s
x=input("Enter the list elements:")
n=[int(i)for  i in x.split(",")]
s=even_len(n)
print(s)
