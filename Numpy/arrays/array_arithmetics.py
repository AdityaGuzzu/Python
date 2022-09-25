'''
We will see how we can use the *,+,-,/,%  operators on arrays
'''
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

#element wise multiplication
print(arr1*arr2)


#multiplying every element with a scalar
print(arr1*10)


#element wise addition
print(arr1 + arr2)


#adding a scalar to every element
print(arr1 + 10)


#using multiple operations
print(arr1*10 + arr2)


#dividing each element with a scalar
print(arr1/10)


#subracting a scalar from each element
print(arr2-10)

#using the modulus operator
print(arr2%5)
