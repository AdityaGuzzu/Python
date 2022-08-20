from BusinessBoard.listchecker import *

def unqdepnames(emp_lst):
    lst = []
    counter2 = 0
    for i in emp_lst:
        z = i['Department']
        while counter2 < len(z):
            if not check(lst,z[counter2]):
                lst.append(z[counter2])
            counter2 += 1
        counter2 = 0
    return lst

def unqdepnames2(emp_lst):
    lst = []
    counter2 = 0
    for i in emp_lst:
        if not check(lst,i['Department']):
            lst.append(i['Department'])
    return lst
