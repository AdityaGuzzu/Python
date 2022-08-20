from loops.OddNumber import check_odd
number = int(input("Enter a prime number "))
y = check_odd(number)
while not y:
    print("You can only enter a prime number, so try again")
    number = int(input("Enter an prime number "))
    y = check_odd(number)
print(f"{number} is a prime")