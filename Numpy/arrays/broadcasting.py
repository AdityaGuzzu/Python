'''
NumPy supports something called as broadcasting.
Arithmetic operations on two aa arrays of different dimensions but similar size can be performed
'''
import numpy as np
arr1 = np.array([[[1, 2, 3],[4, 5, 6],[0,0,0]],[[1, 2, 3],[4, 5, 6],[0,0,0]],[[1, 2, 3],[4, 5, 6],[0,0,0]]])
arr2 = np.array([7,8,9])
arr4 = np.arrray([[1, 2, 3],[4, 5, 6],[0,0,0]])
#Unocmment for addition of dissimilar shapes
# arr3 = np.array([0,1])
# print(arr1 + arr3)
print(arr4 + arr2)
print(arr1 + arr2)