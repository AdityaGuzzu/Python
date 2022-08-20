from BusinessBoard.listchecker import *
from deptnames import *
def depsalavg(emp_lst,lst):
    print("Department wise average annual salary:")
    counter3 = 0
    dep_sal = []
    while counter3 < len(lst):
        for i in emp_lst:
            k = i['department']
            if check(k,lst[counter3]):
                dep_sal.append(i['salary'])
        print(f"{lst[counter3]}: {round(sum(dep_sal)/len(dep_sal))} rupees")
        counter3 += 1
        dep_sal.clear()
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
               , "designation": "Head HR, Hyderabad", "salary": 200000}
           ]
depsalavg(emp_lst, unqdepnames(emp_lst))