import pandas as pd

'''
We can copy a data frame into another data frame using the copy method
'''
df_1 = pd.DataFrame([[1,2,3,4,5],[2,3,1,4,5]], dtype=int, columns=['Aditya', 'Pranati', 'Adi', 'Sravani', 'Simham'], index=['Sem 1 Rank', 'Sem 2 rank'])
df_2 = df_1.copy()
print(df_2)