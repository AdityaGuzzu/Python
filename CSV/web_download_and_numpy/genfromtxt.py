import io

import numpy as np
import io
''''
We will use genfrom txt to input data into numpy arrays.
The genfromtxt takes one mandatory argument which is the source of the data we want to split into arrays
Every non empty line is split into columns each seperated by the specified delimiter (by default, its comma)

'''

word = "H,e,y, my name is aditya"
arr = np.genfromtxt(io.StringIO(word), delimiter=' ',dtype=str,autostrip=True)
print(arr)

num_arr = np.genfromtxt('climate.txt',delimiter=',',skip_header=1,dtype=float)
print(num_arr.dtype)
print(num_arr)
