'''
We will implement inheritance
'''


class Player:
    def __int__(self, name):
        self.name = name
        print(f"\nPlayer name is {self.name}")


class Bowler(Player):
    def __int__(self, name, wickets):
        Player.__init__(self, name)
        self.wickets = wickets
        print(f"The number of wickets of {self.name} are: {self.wickets}")


pl_name = "Kohli"
# player = Player(name)
bowler = Bowler()
print(bowler.name)

