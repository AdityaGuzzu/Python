from calculator import *
z = ""
def calculator(z,x,y):
    if z == 1:
        sum(x,y)
    elif z == 2:
        mul(x,y)
    elif z == 3:
        div(x,y)
    elif z == 4:
        sub(x,y)
calculator(3,4,2)
