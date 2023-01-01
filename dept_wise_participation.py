import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r'C:\Users\Ravi G\Downloads\Registration Nav Vishwas - Total.csv')

print(data['Course of study'])

'''
initialising array containing course of each registration
Initialising variablec containing the number of students in each stream
'''
course_array = []
sciences = 0
commerce = 0
management_and_arts = 0

'''
cleaning the data.
'''
for cell in data['Course of study']:
    cell = str(cell)
    cell = cell.lower()
    cell = cell.replace('.','')
    cell = cell.replace(' ','')
    cell = cell.replace('(','')
    cell = cell.replace(')','')
    course_array.append(cell)



for course in course_array:
    if(course.find('bcom') >= 0 or course.find('hba') > 0):
        commerce += 1

    elif(course.find('bsc') >=0  or course.find('mecs')>=0 or course.find('btmbc')>=0 ):
        sciences += 1

    elif(course.find('ba') >= 0 or course.find('bba')>=0):
        management_and_arts += 1


'''
Plotting the data
'''
plot_labels=["Sciences","commerce","Management and arts"]
participation_array = [sciences,commerce,management_and_arts]
plt.pie(participation_array,labels=plot_labels,autopct='%1.1f%%')
plt.title('Pie chart of Nav Vishwas registrations out of 235 registrations')
plt.show()
