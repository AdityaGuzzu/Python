n1 = 1
n2 = n1
n3 = n1 % n2
counter = 0
while n1 <= 101:
    while n2 >= 1:
        n3 = n1 % n2
        n2 -= 1
        if n3 == 0:
            counter += 1
    if counter == 2:
        print(n1)
    n1 += 1
    n2 = n1
    counter = 0
