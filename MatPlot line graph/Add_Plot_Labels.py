import matplotlib.pyplot as plt
age = [20, 23, 25, 27, 29]
salary = [23000, 25000, 40000, 33000, 200000]
python_salary = [42000, 54000, 60000, 54000, 332000]
plt.plot(age, salary, label='All developers') #This adds label to this graph
plt.plot(age, python_salary, label='Python') #same as above
plt.xlabel(' age ')
plt.ylabel('Salary per month in rupees')
plt.title('Age vs Salary graph')
plt.legend()  #THIS IS MANDATORY
plt.show()