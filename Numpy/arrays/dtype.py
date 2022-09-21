'''
For the purpose of efficiency, all the data types of a numpy array MUST BE THE SAME
(This is something on the lines of C,C++)
'''

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype)

#lets convert the data type to float
arr = np.array([1,2,3,4,5],dtype=float)
print(arr.dtype)

#Now, lets try putting heyterogeneous elements and see what error gets thrown
arr = np.array([1,2,"Hello"])
print(arr.dtype)

#lets try converting the previous array to chars
arr = np.array([1,2,"Hello"],dtype=str)
print(arr.dtype)

#Implicit type conversion occurs when we have a heterogeneous mix of integers and floats
arr = np.array([1,2,3,6.7,2,3])
print(arr.dtype)
