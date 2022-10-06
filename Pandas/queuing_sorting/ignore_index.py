import pandas as pd

'''

The ignore index parameter of the sort_values method of the DataFrames class will rename the indices of the 
resultant Dataframe from 0 to (n-1) where n is the number of elements in the sorted 

'''
world_df = pd.read_csv('E:/python/Data/parsed_country_data.csv')
highest_literacy_df = world_df.sort_values('Literacy',ignore_index=True).head(10)
print(highest_literacy_df[['Country','Literacy']])

#WE can see the indices of highest_literacy_df and world_df don't match
print(world_df)
