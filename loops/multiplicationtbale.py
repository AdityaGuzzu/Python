multiplicand = 1
multiplicant = 1
while multiplicand <= 5:
    print(f"multiplication table of {multiplicand}")
    while multiplicant <= 10:
        print(f"{multiplicand} * {multiplicant} = {multiplicand*multiplicant}")
        multiplicant += 1
    multiplicant = 1
    multiplicand += 1

