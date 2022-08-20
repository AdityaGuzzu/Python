def avgsal(emp_lst):
    salary_counter = 0
    for i in emp_lst:
        salary_counter += i['salary']
    return round(salary_counter/len(emp_lst))