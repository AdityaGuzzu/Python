'''
We will use the split and strip functions to convert a string into an array of sub-strings.
Here, the strip function removes any leading or trailing whitespaces.
'''
print(" Hello, My name is Aditya, I am from Hyderabad".strip().split(','))

'''
These functions are particularly useful while working with CSV files and stuff
'''
with open('E:/python/CSV/web_download_and_numpy/climate.txt','r') as file:
    data = file.readlines()
    data2 = file.readline()


print(data[1])
print(data2)
print(data[0].strip().split(','))