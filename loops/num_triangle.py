'''
    Lets print the following pattern using while loop:
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
'''
row = 1
column = 1
temp_str = ""
while row <=5:
    while column <= row:
      temp_str += f" {row}"
      column += 1
    row += 1
    column = 1
    print (temp_str)
    temp_str=""



