#We know we can use indexes to access elements of a string. We will see how to get multiple chars

statement = "Manchester United is a finished club"

#The first element stands for the starting index and the second one stands for the last index
first_five = statement[0:5]

#printing it
print("The first five chars of statement are ",first_five)

#lets select the last five
last_five = statement[-5:-1]

#printing the last five elements
print("The last five elements of statement are: ",last_five)
