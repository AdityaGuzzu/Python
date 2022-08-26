'''
Implementing classes in Python
'''
class test:
    '''
    No access specifiers.
    No member function definitions.
    THIS SUCKS
    '''
    def hello(self):    #syntax
        print("Hello Welcome to the class")
    def num(self,number):   #self is mandatory
        print(number)

object = test()
object.num(100)
object.hello()

obj2 = test()   #object declaration

'''
Create member variables for different objects. Example
'''
obj2.x = 200
object.y = 400

print(f"x in obj2 = {obj2.x}")
print(f"y in obj2 = {obj2.y}")      #error. Only object has y