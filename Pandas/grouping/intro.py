import pandas as pd
'''
    Grouping the data is very essential in Data Analysis. Pandas provide a grouping function to the DataFrame objects
    which can be used to group a set of rows depending on a condition.
    We cannot but retrieve a DataFrame just by grouping, we need to perform some aggregation function like sum or mean etc
'''

world_df = pd.read_csv('E:/python/Data/parsed_country_data.csv')

#Now, we can group the countries by their region
print('\n----------------AVERAGE POPULATION---------------------------')
region_wise_df = world_df.groupby('Region')[['Population', 'Coastline', 'GDP', 'Area']].mean()
print(region_wise_df['Population'].sort_values(ascending=False),'\n -------------------AVERAGE GDP PER CAPITA------------------')
print(region_wise_df['GDP'].sort_values(ascending=False),'\n-------------AVERAGE COASTLINE-------------------------------')
print(region_wise_df['Coastline'].sort_values(ascending=False),'\n--------------AVERAGE AREA----------------------------')
print(region_wise_df['Area'].sort_values(ascending=False))



