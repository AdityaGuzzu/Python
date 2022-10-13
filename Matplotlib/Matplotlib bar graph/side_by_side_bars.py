from matplotlib import pyplot as plt
import numpy as np
names = ['Aditya', 'Nikhil', 'Sirisha', 'Sruthi']
marks_sem_1 = [83, 80, 85, 90]
marks_sem_2 = [80, 87, 89, 76]
x_indexes = np.arange(len(names))
width = 0.20
plt.bar(x_indexes, marks_sem_1, width= width)
plt.bar(x_indexes - width, marks_sem_2, width= width)
plt.xlabel('Names')
plt.ylabel('Marks out of 100')
plt.xticks(ticks = x_indexes
, labels = names)
plt.tight_layout()

plt.show()