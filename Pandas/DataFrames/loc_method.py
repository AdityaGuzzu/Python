import pandas as pd
'''
We can use the loc indexing and pass in the row number to receive the row elements
'''

df = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],dtype=int,index=['Aditya', 'Pranati', 'Adi', 'Sravani'])
print(df.loc['Pranati'])


#We can create another dataframe with the elements of df.loc['Pranati']
df2 = df.loc['Pranati']

#Lets print the first two rows
print(df.loc[['Aditya', 'Pranati']])


