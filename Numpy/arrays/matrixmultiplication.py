'''
We will use the in-built matrix multiplication function of numpy module
'''
import numpy as np
arr = np.array([[1,2,3],[1,2,3],[1,2,3]])
arr2 = np.array([1,2,3])
arr3 = np.matmul(arr,arr2)
print(arr3)

'''
We can also use the following notation
'''
arr3 = arr @ arr2
print(arr3)