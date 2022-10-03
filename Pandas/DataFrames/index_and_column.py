import pandas as pd

'''
We can label the columns and rows of a DataFrame using the index and column parameters.
This file contains an example of the same.
We can see the difference between how Python implicitly converts the passed csv file into a data frame vs how we can
explicitly mention the labels
'''

marks_df = pd.read_csv('marks.csv',skiprows=0)
print(marks_df)
marks_df = pd.DataFrame([[20,23,25],[22,18,23]
                         ,[18,10,24],[25,25,25],
                         [23,24,25],[20,19,28],
                         [23,24,19]],index=['Aditya','GVSS','Narasimha','Sravani','Mahathi','Josh','Nishant']
                        ,columns=['Math','Physics','CS'],dtype=int)
print(marks_df)