p1 = "samaja"
p2 = "varagamana"
p4 = ""
counter = 1
while counter < 3:
    p1 += p2
    counter += 1
counter = 1
print(p1)
temp = len(p1)
while counter < temp - 1:
    counter2 = counter + 1
    while counter2 >= 5:
        p4 += p1[counter2]
        counter2 -= 1

    counter += 1
print(p4)









