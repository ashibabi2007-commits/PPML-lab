#wap to print the second largest and smallest element in the list of 10 integers witohut sort
arr=[]
x=int(input("Enter the number of elements:"))
for i in range(x):
    m=int(input("Enter the element:"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("the sorted array is:")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("Second largest element is:",second_largest)
print("Second smallest element is:",second_smallest)
