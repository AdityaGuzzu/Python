'''
We will look at the efficiency (both time and space) of the numpy array as opposed to the classic
Python list
'''
import numpy as np
import time
import sys

'''
First lets look at the space efficiency
'''
num = 10000

#space consumed by a list
x = range(0,num)
print(sys.getsizeof(7)*len(x))

#space consumed by a NumPy array
y = np.arange(0,num)
print(y.size*y.itemsize)

'''
Speed efficiency:
'''


m1  = range(num)
m2 = range(num)
start = time.time()
res = [(z+l) for z,l in zip(m1,m2)]
print("The Python list took ",(time.time()-start)*1000,"seconds")



k1 = np.arange(num)
k2 = np.arange(num)
start = time.time()
res = [(z+l) for z,l in zip(k1,k2)]
print("The NumPy array took ", (time.time()-start)*1000,"seconds")

'''
I don;t know why but NumPy arrays are slower on my device
'''





