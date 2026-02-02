def vowelcount(s):
    count=0
    for i in s:
        if i in['a','e','i','o','u','U','A','E','I','O']:
            count+=1
        return count
n=input("Enter a string:-")
print(f"{n} contains{vowelcount(n) }vowels")
