from matplotlib import pyplot as plt
#Previously we worked with plotting line graphs. Now lets work on Bar graphs
names = ['Aditya', 'Nikhil', 'Sirisha', 'Sruthi']
marks = [83, 80, 85, 90]
# to just plot one graph we use plt.bar
plt.bar(names,marks)
plt.xlabel = 'Names'
plt.ylabel = 'Marks out of 100'
plt.show()
