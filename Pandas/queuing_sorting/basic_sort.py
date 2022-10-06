import pandas as pd
'''

The sort_values method of DataFrame class is used to sort the values of the DataFrame in multiple ways
Unless specified, the method uses quicksort as its default.
We can also use other methods like heap sort, mergesort, stable sort

NOTE: By default, inplace is set to False
'''

#This gives us the top 10 countries with the highest population
world_df = pd.read_csv('E:/python/Data/parsed_country_data.csv')
highest_pop_df = world_df.sort_values('Population', ascending=False).head(10)
print(highest_pop_df[['Country', 'Population']])

#Now, lets get the top 10 countries with the lowest population
lowest_pop_df = world_df.sort_values('Population', ascending=True).head(10)
print(lowest_pop_df[['Country','Population']])

