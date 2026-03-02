def print_fibo(n,a=0,b=1):
    if n==0:
        return
    print(a,end=" ")
    print_fibo(n-1,b,a+b)
print_fibo(6)