import pandas as pd

'''
We use the head method of extract the first few lines of the data frame
'''

df = pd.DataFrame([[1,2,3,4,5],[2,3,1,4,5],[2,4,5,1,3]], dtype=int, columns=['Aditya', 'Pranati', 'Adi', 'Sravani', 'Simham'],
                    index=['Sem 1 Rank', 'Sem 2 rank','Sem 3 rank'])

#first two rows
print(df.head(2))

#last two rows
print(df.tail(2))