import pandas as pd

'''
We can use the sample method to retrieve required number of random rows form the DataFrame
'''

marks_df = pd.DataFrame([[20,23,25],[22,18,23]
                         ,[18,10,24],[25,25,25],
                         [23,24,25],[20,19,28],
                         [23,24,19],[21,223,12],[21,10,9]]
                        ,columns=['Math','Physics','CS'],dtype=int)

#printing 2 random rows
print(marks_df.sample(2))