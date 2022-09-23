'''
We will see how to use the concatenate function of the numpy library
'''
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
c = np.array([[5,6]])

'''
We have something called 'axis' in NumPy which determine where the arrays should be concatenated.
So, We will experiment and find out what happens
'''
print("concatenating to the 1st axis")
res = np.concatenate((a, b), axis=1)
print(res)
print(res.shape)

print("Now concatenating to the 0th axis")
res = np.concatenate((a,c),axis=0)
print(res)
print(res.shape)