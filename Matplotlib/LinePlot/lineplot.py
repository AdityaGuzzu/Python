import matplotlib.pyplot as plt

''''
Matplotlib is a common library used for plotting graphs in Python.
Line plot is one common method to do so. Line plot is basically a line between two data points on a graph.
This file contains the steps to plot a line graph using matplotlib using two lists
'''

goals = [5,5,5,4,4]
players = ['Haaland', 'Pierrot', 'Orsic', 'Traore', 'Sane']

#FIrst arguments passes ticks on the x axis and the second arg is the corresponding values on y axis
plt.plot(players, goals)

#We can use labels to give information about which axis represents what
plt.xlabel("Player Name")
plt.ylabel("Goals Scored till GW 3")
plt.title('UCL Top Goalscorers till GW 3')
plt.show()