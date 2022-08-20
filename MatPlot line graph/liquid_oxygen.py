"""plotting the graph of the ratio of isothermal compressibility and volume expansion vs temperature for liquid
 oxygen"""
import matplotlib.pyplot as plt
j=0
theta = [60,65,70,75,80,85,90]
beta = [3.48, 3.60, 3.75, 3.90, 4.07, 4.33, 4.60]
kappa = [0.95, 1.06, 1.20, 1.35, 1.54, 1.78, 2.06]
constant = []
while j<7:
    constant.append(beta[j]/kappa[j])
    print(constant[j])
    j+=1
plt.plot(theta,constant)
plt.xlabel('temperature in degrees')
plt.ylabel('the ratio of beta and kappa')
plt.title('The ratio of VE/ITC vs Temperature')
plt.legend()
plt.show()