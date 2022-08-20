def dessalavg(emp_lst,lst2):
    emp = []
    counter4 = 0
    while counter4 < len(lst2):
        for i in emp_lst:
            m = i['designation']
            if i['designation'] == lst2[counter4]:
                emp.append(i['salary'])
        print(f"\nAverage salary of a {lst2[counter4]} is {sum(emp)/len(emp)}")
        emp.clear()
        counter4 += 1