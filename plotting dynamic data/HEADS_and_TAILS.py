import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
plt.style.use('fivethirtyeight')
x_axis = []
y_axis = []
counter = 0
def random_toss(number_of_times):
    counter = 0
    x_axis = ['Heads', 'Tails']
    y_axis = [0, 0]
    while counter < number_of_times:
        random_throw = random.choice(x_axis)
        plt.style.use('fivethirtyeight')
        if random_throw == 'Heads':
            y_axis[0] += 1
        else:
            y_axis[1] += 1
        plt.cla()
        plt.bar(x_axis, y_axis, width= 0.2)
        counter += 1
simulate = FuncAnimation(plt.gcf(), random_toss, interval= 1000)
plt.xlabel('heads and tails')
plt.ylabel('Number of times it has turned up')
plt.tight_layout()
plt.show()