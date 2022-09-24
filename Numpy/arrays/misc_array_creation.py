'''
We will see the miscellaneous ways of creating a NumPy array.
'''

import numpy as np

#create a null amtrix
arr = np.zeros([2, 2])
print(arr, '\n')

#create a identity matrix
arr = np.ones([3, 3])
print(arr, '\n')

#creating an array with all its elements being a given number
arr = np.full([2, 3], 6)
print(arr, '\n')

#create an array of random numbers between 0 and 1
arr = np.random.rand(2, 3)
print(arr, '\n')

#creating the same using randn which generates random numbers based on Gaussian distribution
arr = np.random.randn(2, 3)
print(arr,'\n')

'''
    arange function generates a linear array with elements from START to STOP and skips the (STEP-1) number of elements 
    in between
'''
arr = np.arange(10, 100, 2)
print(arr, '\n')

#Using linspace to get equally spaced numbers within a range
arr = np.linspace(5,50,5,dtype=int)
print(arr,'\n')
