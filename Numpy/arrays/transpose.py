import numpy as np

'''
This file contains the method to find the transpose of a matrix using the transpose function in numpy
'''

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr,'\n')
print("The shape of the array before transpose is: ",arr.shape,'\n')

#lets transpose the matrix
arr = np.transpose(arr)
print(arr,'\n')
print("The shape of the array after transpose is: ",arr.shape,'\n')

#The transpose function has no effect on single dimentsion arrays. EX:
arr = np.array([1,2,3,4,5])
print("The single dimension matrix is: ",arr)
print("The shape of the single dimension before after transpose is: ",arr.shape)

arr = np.transpose(arr)
print("The new array after transpose is: ",arr)
print("The shape of the single dimension array after transpose is: ",arr.shape)
