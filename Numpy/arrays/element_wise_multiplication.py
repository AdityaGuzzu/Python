'''
NumPy arrays have a poweful feature of carrying out element wise multiplications
'''

import numpy as np
arr_1 = np.array([1,2,3,4,5])
arr_2 = np.array([1,2,3,4,5])
print(arr_1*arr_2)

'''
We can also now get the dot product by calling the sum methdod
'''

mul_arr = arr_1*arr_2
print("The dot product of arr_1 and arr_2 is: ",mul_arr.sum())