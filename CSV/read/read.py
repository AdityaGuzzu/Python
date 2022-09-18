'''
This file contains the introduction to reading CSV files using Python.
Firstly, we need to import the CSV module
'''

#importing the CSV module
import csv

'''
The following method is equivalent to creating a file object of fstream in C++ with std::ios::out as the second argument
'''
with open('data.csv', 'r') as data:
    #reading all the data of the data.csv file and storing it in data_reader
    data_reader = csv.reader(data)

    #Printing the data
    for i in data_reader:
        print(i)
