#elif statement is equivalent to 'else if' in C and C++. It is used to evaluate multiple conditions
# The next condition is evaluated only when the current condition returns false

number = int(input("Enter the number: "))

if number == 1:
    print("Number = 1")
elif number == 2:
    print("Number = 2")
elif number == 3:
    print("Number = 3")
elif number == 4:
    print("Number = 4")
elif number == 5:
    print("Number = 5")
else:
    print("Number > 5")
