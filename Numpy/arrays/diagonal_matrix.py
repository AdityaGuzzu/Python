'''
We will look at creating a diagonal matrix in various ways
'''

import numpy as np

'''
The eye function takes 4 arguments:
    ---> The number of rows (M)
    ---> The number of columns (N)
    ---> The diagonal number whose elements should be 1 (k). 
            ---> k=0 is the principal diagonal
            ---> k<0 is the |k|th lower diagonal
            ---> k>0 is the kth upper diagonal
    ---> dtype is the type of data the array should contain
'''

#create a diagonal matrix. This function only accepts one argument which specifies the number of rows and columns
arr = np.eye(3,k=0,dtype=int)
print(arr,'\n')

#create a upper diagonal matrix
arr = np.eye(5,k=1,dtype=int)
print(arr,'\n')

#create a lower diagonal matrix
arr = np.eye(5,k=-1,dtype=int)
print(arr,'\n')

#create a diagonal matrix of uneven dimensions
arr = np.eye(M=2,N=3,dtype=int)
print(arr,'\n')