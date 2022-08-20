from matplotlib import pyplot as plt
names = ['Aditya', 'Nikhil', 'Sirisha', 'Sruthi']
marks_sem_1 = [83, 80, 85, 90]
marks_sem_2 = [80, 87, 89, 76]

# to just plot one graph we use plt.bar
#if we plot two bar graphs like we did with line plots, it won't plot them side by side
plt.bar(names,marks_sem_1)
plt.bar(names,marks_sem_2)
plt.xlabel = 'Names'
plt.ylabel = 'Marks out of 100'
plt.show()