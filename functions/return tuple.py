'''
A program to show how we can return multiple values as a tuple
'''
import random


def throw():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2  #returns a tuple containing dice1 and dice2


print(throw())
throw_tuple = throw()   #asigning the tuple to a variable
print(throw_tuple[0])