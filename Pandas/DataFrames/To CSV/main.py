import pandas as pd

'''
This file contains writing into a CSV file. Especially ignoring the annoying row names 
'''
sample_df = pd.read_csv('data.csv')
print(sample_df)
sample_df['Sravani'] += 10
sample_df.to_csv('data.csv', index=False, index_label=False)
sample_df = pd.read_csv('data.csv')
print(sample_df)


