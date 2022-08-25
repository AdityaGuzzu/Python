'''
We will see the use of insert method under list class
'''

numbers = [1,2,3,4,5]
numbers.insert(0,0)             #inserts 0 at 0th index
numbers.insert(5,[6,7,8,9,10])  #inserts the list [6,7,8,9,10] at the 6th index
print(numbers)