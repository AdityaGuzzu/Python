from calculator2 import *
test = False
x = int(input("Number 1 "))
y = int(input("Number 2 "))
z = input("enter operator ")
while z != "add" and z != "sub" and z != "mul" and z != "div":
    print("You can only enter add/sub/mul/div")
    z = input("enter operator")
print(calulator(z,x,y))
