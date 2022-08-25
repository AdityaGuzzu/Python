'''
A program to demonstrate the use of 'clear' method of the list class
'''
numbers = [1,2,3,4,5]
print(numbers.__len__())
print(numbers.__sizeof__())


numbers.clear()
print(numbers.__len__())
print(numbers.__sizeof__())

