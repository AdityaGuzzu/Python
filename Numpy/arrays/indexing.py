'''
NumPy extends Python's indexing and provides more intuitive and powerful indexing.
'''
import numpy as np
arr = np.array([[[1,2,3,4,5],
                 [6,7,8,9,10]],

                [[11,12,13,14,15],
                 [16,17,18,19,20]],

                [[21,22,23,24,25],
                 [26,27,28,29,30]]])

print(arr.shape)

#lets print the first element
print(arr[0,0,0])


'''
17 is in second row, second column, and the second element on the z axis.
So its indices are (1,1,1).
Lets verify the same
'''
print(arr[1,1,1])

#creating sub arrays:
print(arr[0,0:,0])  #should be getting 1,6

#Creating another sub array:
print(arr[2:,0,1:]) #should be getting [22,23,24,25]

#One more time
print(arr[0:2,1,2]) #should be getting [10,20]