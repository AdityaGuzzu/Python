def check_odd(n1):
    n2 = n1
    y = False
    counter = 0
    while n2 >= 1:
        n3 = n1 % n2
        n2 -= 1
        if n3 == 0:
            counter += 1
    if counter == 2:
        y = True
    else:
        y = False
    return y

