from temp2 import *
from BusinessBoard.listchecker import *
from CheckerHUGE import *
from deptsalary import*
from averagesalary import *
from dessalary import *
from desnames import *
emp_lst = [{"name": "Aditya", "company": "TCS", "ID.No": 1526, "department": ["Sales", "Marketing", "HR"]
            , "designation": "Performance Analyst", "salary": 3600000},
           {"name": "Sridhar", "company": "Wipro", "ID.No": 24567, "department": ["Sales"],
            "designation": "Sales Head, South India", "salary": 3000000},
           {"name": "Akash", "company": "Infosys", "ID.No": 31209, "department": ["Production", "IT", "Sales"]
            , "designation": "Performance Analyst", "salary": 3200000},
           {"name": "Nirmala", "company": "HCL", "ID.No": 873562, "department": ["Sales", "Maintenance"]
            , "designation": "Sales Head, South India", "salary": 3200000},
           {"name": "Sruthi", "company": "Tech Mahindra", "ID.No": 7682935, "department": ["HR", "IT"]
            , "designation": "Head HR, Hyderabad", "salary": 2600000},
           {"name": "Nikhil", "company": "Apple", "ID.No": 76842935, "department": ["HR"]
               , "designation": "Head HR, Hyderabad", "salary": 2000000}
           ]
counter = 1
for i in emp_lst:
    if counter >= 2:
        print(f"\nemployee number - {counter}")
    else:
        print(f"employee number - {counter}")
    print(f"name - {i['name']}")
    print(f"company - {i['company']}")
    print(f"ID Number - {i['ID.No']}")
    print(f"department/department - {name_cat(i['department'])}")
    print(f"salary - {i['salary']}")
    counter += 1
lst = []
counter2 = 0
for i in emp_lst:
    z = i['department']
    while counter2 < len(z):
        if not check(lst,z[counter2]):
            lst.append(z[counter2])
        counter2 += 1
    counter2 = 0
print(f"\nAll the departments are {name_cat(lst)}")
counter3 = 0
sal_lst = []
depsalavg(emp_lst,lst)
print(f"\naverage salary across all departments:")
print(f"{avgsal(emp_lst)} rupees")
for i in emp_lst:
    sal_lst.append(i['salary'])
sal_max = max(sal_lst)
sal_min = min(sal_lst)
print(f"\nThe maximum salary is {sal_max}")
print(f"\nThe minimum salary is {sal_min}")
print(unqdes(emp_lst))
lst2 = unqdes(emp_lst)
dessalavg(emp_lst,lst2)
print(max_len_des(lst2))
useful_lst = []
counter = 0
counter2 = 0
rand_lst = []
print("Average salary by department and designation")
useful_lst2 = []
while counter < len(lst):
    while counter2 < len(lst2):
        for i in emp_lst:
            if check(i['department'], lst[counter]) and i['designation'] == lst2[counter2]:
                useful_lst.append(i['salary'])
                rand_lst.append(lst2[counter2])
                useful_lst2.append(i['salary'])
        if len(useful_lst) > 0:
            beautiful = f'{rand_lst[0]} {lst[counter]} '
            imp = ":"
            print(f"|{rand_lst[0]}  {lst[counter]}{imp.zfill(40 - len(beautiful)).replace('0',' ')}  {sum(useful_lst)/len(useful_lst)}|")
        useful_lst.clear()
        rand_lst.clear()
        counter2 += 1
    counter2 = 0
    counter += 1
