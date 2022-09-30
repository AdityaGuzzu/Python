import pandas as pd

'''

Data Frames are an in-built data structure in pandas module.
They are used to create tabular data out of arrays, dictionaries , strings.

'''
file_df = pd.read_csv(r'C:\Users\Ravi G\Desktop\Aditya\BusinessSimulation\data\one_game_net_trans.csv')

#The info method provides basic info about the data frame
file_df.info()

'''
The describe function gives some more insights. For all the numerical columns, it provides with information like
max, min, top and bottom percentile cut-offs.

For a column of strings it provides with data like the most frequent value etc.

For a file containing both numerical and string values in columns, it chooses the numerical columns unless specified.
'''
print(file_df.describe())



