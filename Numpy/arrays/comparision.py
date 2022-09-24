'''
In numpy, we can compare two arrays. The resultant is an array containing respective booleans
'''
import numpy as np
arr1 = np.array([[1,2,3],[1,2,3],[1,2,3]])
arr2 = np.array([[1,2,3],[2,3,4],[5,6,7]])


print("equality:\n",arr1 == arr2)
print("greater than or equal to: \n",arr1 >= arr2)
print("Less than or equal to: \n",arr1<=arr2)
print("Greater than: \n",arr1>arr2)
print("Less than: \n",arr1<arr2)
