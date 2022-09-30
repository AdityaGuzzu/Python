import pandas as pd

'''
We will use the shape member variable to get the dimensions of the created data frame
'''

array = pd.Series([1,2,4,5,7])
print(array.shape)

file_df = pd.read_csv(r'C:\Users\Ravi G\Desktop\Aditya\BusinessSimulation\data\one_game_net_trans.csv')
print(file_df.shape)