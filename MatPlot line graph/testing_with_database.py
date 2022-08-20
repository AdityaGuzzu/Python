import matplotlib.pyplot as plt
from lst_dict.empdb import *
from BusinessBoard.listchecker import *
from lst_dict.deptnames import *
salary_lst = []
dept_lst = []
emp_lst = emp_db()
def sumsal(lst1,lst2):
    emp = []
    sum_lst = []
    counter4 = 0
    while counter4 < len(lst2):
        for i in lst1:
            m = i['Department']
            if i['Department'] == lst2[counter4]:
                emp.append(i['Salary'])
        sum_lst.append(sum(emp)/len(emp))
        emp.clear()
        counter4 += 1
    return sum_lst
unq_dpt_lst = unqdepnames2(emp_lst)
salary_lst = sumsal(emp_lst,unq_dpt_lst)
plt.plot(unq_dpt_lst,salary_lst, label='average salary dept wise')
plt.xlabel('Department Name')
plt.ylabel('Average Salary')
def num_(lst1,lst2):
    emp = 0
    sum_lst = []
    counter4 = 0
    while counter4 < len(lst2):
        for i in lst1:
            m = i['Department']
            if i['Department'] == lst2[counter4]:
                emp += 100
        sum_lst.append(emp)
        emp = 0
        counter4 += 1
    return sum_lst
emp_dept_num_lst = num_(emp_lst,unq_dpt_lst)
plt.plot(unq_dpt_lst,emp_dept_num_lst, label='Number of employees * 100')
plt.legend()
plt.show()