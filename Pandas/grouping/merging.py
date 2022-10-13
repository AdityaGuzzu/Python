import pandas as pd
'''
Merge function of the pandas class merges one DataFrame into another. We can do this in multiple ways but here,
    we've done this on indices
'''
df1 = pd.DataFrame([[21,20,19,15], [25,25,23,22], [22,24,20,13]], index=['Maths','Physics','CS'], columns=['Aditya', 'Vamsi',
                                                                                                           'Nikhil', 'Sruthi'])

#Now lets create another df of marks of other students
df2 = pd.DataFrame([[24,20,19,18], [22,18,17,20], [18,19,23,22]], index=['Maths', 'Physics', 'CS'], columns=['Sharvari', 'Pranati',
                                                                                                             'Rufus', 'Josh'])

print(df2)
df = pd.merge(df1,df2, left_index=True, right_index=True)
print(df)
