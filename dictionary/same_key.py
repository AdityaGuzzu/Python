#A dictionary can have same value with different key but never the same key with different values
#example:
dict = {1: 'Aditya', 2: 'Nikhil'}
dict[3] = 'Aditya'
print(dict)
#now lets try to see what happens if we try to enter another value for the key 1
dict[1] = 'Sruthi'
print(dict)
#SO WE CAN NEVER HAVE THE SAME KEY REPRESENTING TWO VALUES. IF WE TRY TO ENTER IT, IT WILL CHANGE THE EXISTING VALUE.