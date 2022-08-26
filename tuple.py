'''
A tuple is like a list but we can't change or add or delete the elements of a tuple
'''

numbers = (1,2,3,4,5)
'''
A code like: 
    numbers[1] = 5
will throw an error  
'''

'''
Lets see tuple unpacking
'''

a,b,c,d,e = numbers #This is called unpacking
print(a,b,c,d,e)

print(numbers)  #We see tuple is still existing