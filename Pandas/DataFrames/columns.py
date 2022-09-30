import pandas as pd

'''
The columns method allows us to get a list of column names of the DataFrame
'''
file_df = pd.read_csv(r'C:\Users\Ravi G\Desktop\Aditya\BusinessSimulation\data\one_game_net_trans.csv')
print(file_df.columns)

