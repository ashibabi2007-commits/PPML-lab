import numpy as np
ones_array = np.ones((2,3))
zeros_array = np.zeros((2,3))
empty_array = np.empty((2,3))
print("Ones :\n", ones_array)
print("Zeros :\n", zeros_array)
print("Empty :\n", empty_array)

arr = np.array([[1,2,3],[4,5,6]])
print("Shaped of array :", arr.shape)

reshaped = arr.reshape(3,2)
print("Reshaped array :\n", reshaped)

arr1 = np.array([1,2,3])
copy_arr1 = arr1.copy()
view_arr1 = arr1.view()
print("Original :", arr1)
print("Copy :", copy_arr1)
print("View :", view_arr1)

arr2 = np.array([1,2])
arr3 = np.array([3,4])

concatenated = np.concatenate((arr2, arr3))
print("Concatenated array :", concatenated)

arr4 = np.array([5,2,9,1])
print("Sorted array :", np.sort(arr4))