import matplotlib.pyplot as plt
import numpy as np
player_names = ['Haaland','Mitrovic','Harry Kane','Toney','Mac Allister']
goals = [11,6,6,5,4]
ypos = np.arange(len(goals))

#Will replace the value of the ypos array with corresponding index of the player_names array
plt.xticks(ypos,player_names)
plt.bar(ypos,goals)
plt.title('PL top goalscorers till matchday 6')
plt.legend()
plt.show()