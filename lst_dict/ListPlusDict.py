emp_lst = [{"name": "Aditya", "company": "TCS", "ID.No": 1526, "department": ["Sales", "Marketing", "HR"]},
           {"name": "Sridhar", "company": "Wipro", "ID.No": 24567, "department": ["Sales"]},
           {"name": "Akash", "company": "Infosys", "ID.No": 31209, "department": ["Production", "IT"]},
           {"name": "Nirmala", "company": "HCL", "ID.No": 873562, "department": ["Sales", "Maintenance"]},
           {"name": "Sruthi", "company": "Tech Mahindra", "ID.No": 7682935, "department": ["HR"]}]
'''
counter = 0
while counter < len(emp_lst):
    z = emp_lst[counter]
    print(z["name"])
    counter += 1
'''
# Use single quote for key here because a set of "double quotes" are denoting start and end end of formatted string
for i in emp_lst:
    print(f"{i['name']} works at {i['company']}")
