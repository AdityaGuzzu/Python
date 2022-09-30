import pandas as pd

'''
We will use Pandas to convert an array into a tabular form
'''
array = pd.Series([1,2,3,4,5])
print(array.describe())

names = pd.Series(['Aditya', 'Narasimha', 'Sravani', 'Sravani', 'Sravani'])
print(names.describe())