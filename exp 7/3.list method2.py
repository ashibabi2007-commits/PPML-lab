para=input("enter paragraph:")
words=para.split()
print("words count:",len(words))
pal_count=0
for w in words:
    if w==w[::-1]:
        pal_count+=1
print("palindrome count:",pal_count)
for w in words:
    print(w[::-1])