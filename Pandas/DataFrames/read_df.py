import pandas as pd

'''
Reading a panda data frame.
A panda data frame containing the data of a CSV file is different from how we used to read data from 
traditional python or using the 'genfromtxt' function in matplotlib.
Pandas kind of stores the data like a structure of arrays. Ex:
data_df = [ 'c1 header:': [(r1,c1),(r2,c1)....]
            'c2 header': [(r1,c2),(r2,c2).....]
            'c3 header': [(r1,c3),(r2,c3).....]
            .
            .
            .
          ]
'''

pl_df = pd.read_csv('pl_stats.csv')

# #printing the whole column of Player Name
# print(pl_df['Player Name'])

#peinting the name of the third player:
print(pl_df['Player Name'][2])

#accessing a subset of data ir multiple columns
print(pl_df[['Player Name', 'Club']])

#Changes can be made to the data frame
pl_df.at[1, 'Player Name'] = 'Marcus Rashford'

print(pl_df)

