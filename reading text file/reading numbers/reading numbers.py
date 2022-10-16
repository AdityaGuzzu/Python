'''
Reading numbers from a text file
'''

with open('numbers.txt') as file:
    numbers = file.readline()

    #since numbers  is a string, if we want to perform arithmetic operations on any of its elements, we need
    # to type convert them explicitly

    #here, numbers[0] is a string 1 and by converting it to an int, and adding 1, we will get 2 as the output.
    print(int(numbers[0]) + 1)

