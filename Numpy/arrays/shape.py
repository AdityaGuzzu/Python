'''
We will use the shape method of the numpy arrays to find mare about the axes of different matrices
'''

import numpy as np
THREE_D_trans = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(THREE_D_trans.shape)

TWO_D_trans = np.array([[1,2],[1,2]])
print(TWO_D_trans.shape)

rand_matrix = np.array([[1,23],[1,2,3,4]])
print(rand_matrix.shape)