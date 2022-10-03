import pandas as pd

'''
The first_valid_index method returns the index of the first non NaN element
'''
marks_df = pd.DataFrame([[20,25],[22,18,]
                         ,[18,10,24],[25,25,25],
                         [23,24,25],[20,19,21],
                         [23,24,19]]
                        ,columns=['Math','Physics','CS'],dtype=int)

print(marks_df)

#this prints the index of the first non NaN element of the CS column
print(marks_df.CS.first_valid_index())