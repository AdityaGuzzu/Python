'''
Use constructors in this bloody language
'''
class Test:
    def __init__(self,visits):
        self.visits = visits

    def print_(self):
        self.visits += 1
        print("Hello\n" + "Welcome to Python")



obj = Test(5)    #sets the value of visits to 0
obj.print_()
print(f"Number of visits: {obj.visits}")


