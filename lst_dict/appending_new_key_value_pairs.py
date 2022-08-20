emp_lst = [{"name": "Aditya", "company": "TCS", "ID.No": 1526}, {"name": "Sridhar", "company": "Wipro", "ID.No": 24567},
           {"name": "Akash", "company": "Infosys", "ID.No": 31209}, {"name": "Nirmala", "company": "HCL",
           "ID.No": 873562},{"name": "Sruthi", "company": "Tech Mahindra", "ID.No": 7682935}]
for i in emp_lst:
    i["department"] = input(f"which department is {i['name']} in? ")
print(emp_lst)