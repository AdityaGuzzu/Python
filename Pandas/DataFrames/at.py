import pandas as pd

'''
The at function is an alternate way to retrieve a particular element by specifying the row/column pair
'''

data_df = pd.read_csv('pl_stats.csv')

#To the at function, we need to pass in the row and column label/number as the arguments
print(data_df.at[2, 'Player Name'])
