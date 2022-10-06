import pandas as pd
'''
We will look at the inplace parameter of the pandas.DataFrame.drop class
'''
df = pd.DataFrame([[1,2,3,4,5],[1,2,3,4,5]], columns=["Aditya","Narasimha","GVSS","Sravani","Mahathi"])

#inpalce = False returns a copy of the changes
print(df.drop(columns='Mahathi',inplace=False))
print(df)

#inplace = True makes the changes inplace and they are reflected in the original DataFrame
df.drop(columns='Mahathi',inplace=True)
print(df)
