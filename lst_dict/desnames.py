from BusinessBoard.listchecker import *
def unqdes(emp_lst):
    lst2 = []
    counter2 = 0
    for i in emp_lst:
        z = i['designation']
        if not check(lst2,z):
            lst2.append(z)
            counter2 += 1
        counter2 = 0
    return lst2
def max_len_des(lst):
    counter = []
    for i in lst:
        counter.append(len(i))
    return max(counter)