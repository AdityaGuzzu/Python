import numpy as np

'''
In this file, we will take the business data into an array and flip the data such that
we get the details of a ticket in a column rather than a row.
(In mathematical terms, we want to find the transpose of the matrix)
'''
data = np.genfromtxt(r'C:\Users\Ravi G\Desktop\Aditya\BusinessSimulation\data\one_game_net_trans.csv',
                     autostrip=True, dtype=str, delimiter=',',skip_header=1)

print(data.transpose())
