import pandas as pd

'''
We will use the querying methods discussed in boolean_series.py to carry out complex operations
'''

world_df = pd.read_csv('E:/python/Data/parsed_country_data.csv')

'''
Let's find the countries with net positive population growth
'''

more_people_die = world_df[world_df.Birthrate - world_df.Deathrate < 0]
print(more_people_die)

'''
We can add a column to a DataFrame.
This is when again the dictionary picture of the dataframes come into the picture.
Think of the syntax as adding a new key to the dict and a series as an argument
'''

high_literacy_rate = world_df.Literacy > 90
world_df['high_literacy'] = high_literacy_rate

low_income = world_df.GDP < 1086
world_df['low_income'] = low_income

'''
Now lets find the countries with low income and high literacy
Turns out Tajikistan is the only country with high literacy rate and low income
'''

poor_but_literate = world_df[world_df.low_income & world_df.high_literacy]
print("The literacy rate of ",poor_but_literate['Country'],"is: ",poor_but_literate['Literacy'])
print("The GDP per capita of ",poor_but_literate['Country'], "is: ",poor_but_literate['GDP'])

'''
Now that we found the countries which are poor but have high literacy rate, we don;t need the columns
high_literacy_rate and low_income anymore. Lets delete them
'''

world_df.drop(columns = ['high_literacy','low_income'],inplace=True)
print(world_df)
