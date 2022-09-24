'''
The reshape method can be invoked to resize an array.
The original array will remain the same though.
'''

import numpy as np

arr = np.zeros([3,3],dtype=int)

#The arr array has 3 rows and 3 columns. SO its 9 elements in total. We can resize it to any array of size 9
arr2 = arr.reshape(9)
print(arr2)
print(arr)