'''
We will implement inheritance
'''

class Player:
    def __int__(self,name):
        self.name = name
        print(f"Player name is {self.name}")


class Bowler(Player):
    def __int__(self, wickets):
        self.wickets = wickets
        print(f"The number of wickets are: {self.wickets}")


player = Player("Kohli")

bowler = Bowler(20)
