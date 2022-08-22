#we will use the 'in' operator to check if a string or a char exists in another string

full_name = "Gujju Aditya"
surname = "Gujju"

#in returns a boolean unlike find which returns the index of the position of the passed char or string
if surname in full_name:
    print("yeah the name is valid")