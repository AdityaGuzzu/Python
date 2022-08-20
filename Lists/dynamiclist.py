numbers = []
counter = 0
while counter < 1:
    counter2 = 1
    ask = int(input("How many values do you want to add to the list? "))
    while counter2 <= ask:
        numbers.append(int(input("type the number you want to add to the list ")))
        counter2 += 1
    ask2 = input("Do you want to continue adding? ")
    if ask2 == "Yes":
        counter = 0
    else:
        counter += 1
print(numbers)


