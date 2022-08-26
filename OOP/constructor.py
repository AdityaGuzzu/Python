'''
Use constructors in this bloody language
'''
class Test:
    def print_(self):
        self.visits += 1
        print("Hello\n" + "Welcome to Python")

    def __init__(self):
        self.visits = 0

obj = Test()    #sets the value of visits to 0
obj.print_()
print(f"Number of visits: {obj.visits}")


