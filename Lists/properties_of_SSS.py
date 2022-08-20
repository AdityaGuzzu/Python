numbers = [11,22,33,44,55,66,77,88,99,111,222,333,444,555,666,777,888,999]
print(numbers[-1:5:-1]) #Note that 77 was printed because we were gpoing from BACK and 5 was counyted from the front
print(numbers[:2]) #leaving the first block blank implies start = 0
print(numbers[2:]) #leaving second block empty implies stop = -1
print(numbers[:2:2]) #This statement implies - print all values starting from 0 to 1 by skipping every two values in between
print(numbers[:2:4]) #---Same as above--
print(numbers[5:-1])#this statement implies we want to print every value from 5th to the penultimate last value