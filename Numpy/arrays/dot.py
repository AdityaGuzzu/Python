'''

We can compute dot products of two numpy arrays.
This is a built-in feature of NumPy because we require this often.

'''
import numpy as np
array_one = np.array([1,2,3,4,5])
array_two = np.array([1,2,3,4,5])

#returns the dot product
print(np.dot(array_two,array_one))