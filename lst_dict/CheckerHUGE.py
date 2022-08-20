from BusinessBoard.listchecker import *
def checker_big(lst1,lst2):
    statement = False
    counter = 0
    while counter < len(lst1):
        if check(lst2,lst1[counter]):
            statement = True
        counter += 1
    return statement
lst1 = [2, 6, 9, 0]
lst2 = [4, 7, 8]
def checker_lst(lst1,lst2):
    counter = 0
    res_lst = []
    while counter < len(lst1):
        if check(lst2, lst1[counter]):
            res_lst.append(lst1[counter])
        counter += 1
    return res_lst
lst1 = [2,5,6,8,9]
lst2 = [2,5,9,10,11,17]
print(checker_lst(lst1,lst2))