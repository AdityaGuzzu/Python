from weather import temp
y = temp()
if y >= 40:
    print("It's really hot")
elif y >= 30:
    print("It is bearable")
elif y >= 20:
    print("It is pleasant")
elif y >= 10:
    print("It is cold")
elif y >= 0:
    print("Its really cold")
elif y < 0:
    print("ITS FREEZING!!!!")
