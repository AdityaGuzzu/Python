from temp2 import *
emp_lst = [{"name": "Aditya", "company": "TCS", "ID.No": 1526, "department": ["Sales", "Marketing", "HR"]},
           {"name": "Sridhar", "company": "Wipro", "ID.No": 24567, "department": ["Sales"]},
           {"name": "Akash", "company": "Infosys", "ID.No": 31209, "department": ["Production", "IT"]},
           {"name": "Nirmala", "company": "HCL", "ID.No": 873562, "department": ["Sales", "Maintenance"]},
           {"name": "Sruthi", "company": "Tech Mahindra", "ID.No": 7682935, "department": ["HR"]}]
z = ""
k = ""
for i in emp_lst:
    print(f"{i['name']} works at {i['company']}. His/Her ID number is {i['ID.No']}. He/She works in "
          f"{name_cat(i['department'])} department")