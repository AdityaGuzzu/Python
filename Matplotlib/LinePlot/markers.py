
import matplotlib.pyplot as plt
'''
We can use Markers to now the values of the function in between two abscissas.
Lets do it for the Stephen's constant graph plotted earlier
'''
temp1 = [90,85,80,75,70,65,60,55,50,45]
MCG_def1 = [40,36,33,30,27,24,21,18,15,12]
i = 0
slope = 0
while(i < len(temp1)-1):
    slope += (temp1[i+1] - temp1[i])/(MCG_def1[i+1] - MCG_def1[i])
    i += 1
print("The average slope of T vs Theta graph is ", slope/len(temp1))

i = 0
slope = 0

time = [0,120,240,360,480,600,720,840,960]
MCG_def2 = [35,15,7,5,3,2,1.5,1,0.8]

while(i < len(time)-1):
    slope += (MCG_def2[i+1] - MCG_def2[i])/(time[i+1] - time[i])
    i += 1
print("The average slope of theta vs time is ", slope/len(temp1))

'''
We can use a variety of markers in Python like 'X' or 'O' etc. Can look up to the documentation for other markers
'''
plt.plot(time,MCG_def2,label="Theta vs time", marker = 'x')
plt.xlabel('time')
plt.ylabel('Theta')
plt.legend()
plt.show()