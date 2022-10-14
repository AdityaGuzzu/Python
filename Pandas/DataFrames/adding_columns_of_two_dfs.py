import pandas as pd

'''
This file contains the way to add two dataframes
'''

df1 = pd.DataFrame([[10,23,45,23,50],
                    [2,6,34,67,89],[20,21,45,67,89]],columns=['Aditya', 'Sravani', 'GVSSS', 'Narasimha', 'Mahathi'])

df2 = pd.DataFrame([[20,22,45,56,67],[34,45,67,89,100],[67,78,89,13,45]],columns=['Aditya','Sravani','GVSSS','Narasimha',
                                                                                 'Mahathi'])

'''
If any of the columns had strings, they would have been concatenated
'''

# #METHOD !
# print(df1)
# df1 += df2
# print(df1)

# #METHOD 2
# df1[['Aditya','Sravani','Mahathi','Narasimha','GVSSS']] += df2[['Aditya','Sravani','Mahathi','Narasimha','GVSSS']]
# print(df1)
