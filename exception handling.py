'''
Exception Handling in python is different from that in C++.
In Python, we can only catch exceptions related to a certain error type.
example:
'''
try:
    x = int(input("Enter Numerator:" ))
    y = int(input("Enter Denominator: "))
    print(x/y)
except ZeroDivisionError:
    print("0 tho division avvadamma")
