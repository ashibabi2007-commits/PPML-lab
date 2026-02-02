a=0
b=1
l=1000
sum_even=0
print(f"Fibonacci series up to {l}:")
while a<l:
    print(a, end=" ")
    a, b = b, a + b
for i in range(1000):
    if a>1000:
        break
    print(a,end="")
    if a%2==0:
        sum_even+=a
    c=a+b
    a=b
    b=c
print("/nsum of even valued terms are:-",sum_even)