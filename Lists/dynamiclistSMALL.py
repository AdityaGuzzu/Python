numbers = []
ask = int(input("How many values do you want to print at once? "))
counter2 = 0
counter = 1
while counter2 <= 0:
    while counter <= ask:
        numbers.append(int(input("Enter the number of your choice ")))
        counter += 1
    ask2 = input("Do you want to continue printing? ")
    if ask2 == "yes":
        counter2 = 0
        counter = 1
    else:
        counter2 = 1

print(numbers)