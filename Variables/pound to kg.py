#We will ask the user for his weight in pounds and display it in KGs

pound_weight = int(input("Enter you weight in pounds: "))
kilo_weight = 0.453592*pound_weight
print("\nYour weight in KG is ",kilo_weight, " kgs")