import matplotlib.pyplot as plt
import seaborn as sns
y_arr = [2000,-10000,23000,0,800,2999,48299,120000,25000,60000,-45000,-20000,5000,20000,600,700,-20000,
         700,-9000,0,2000,200,2500,-2400,3000,-6000,600,900,1000,-4000,9000,800,3000,-2700,800,700]
x_arr = ["Start", "England", "Iraq", "Waterways", "UNO", "France", "Iran", "Satellite", "Egypt", "Resort", "Canada",
           "Germany", "Airways", "Customs duty", "Switzerland", "Brazil", "Chance", "Italy", "Party House", "Japan",
           "USA", "Travelling Duty", "Roadways", "Mexico", "Hong Kong", "UNO", "Australia", "Jail", "India", "Chance",
           "Saudi Arabia", "Petroleum", "China", "Railways", "Malaysia", "Singapore"]
print(len(y_arr))
sns.set_style("whitegrid")
plt.bar(x_arr,y_arr,width=0.5)
plt.show()
