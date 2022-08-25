'''
We will see the difference between remove and __del
'''

numbers = [1,2,3,4,5]
numbers.remove(2)       #removes the number '2'
numbers.__delitem__(2)  #removes whatever is at the index 2
print(numbers)