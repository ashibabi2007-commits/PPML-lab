s=input("Enter a string:")
print(s[::-1])
rev=''.join(reversed(s))
print(rev)
vowecount=0
conso=0
for i in s:
        if i in 'aeiouAEIOU':
                vowecount=vowecount+1
        else:
                conso=conso+1
print("The vowels are :",vowecount)
print("the consonent are:",conso)   

    