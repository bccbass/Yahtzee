from CardClass import Card

class Player: 
    def __init__(self, name='player'):
        self.is_new = False
        self.name = name
        self.high_score = 0
        self.card = Card()
    def new(self):
        self.is_new = True
    @property
    def greet(self):
        if not self.is_new:
            print(f'Welcome back {self.name}!')
        else:
            print(f'Welcome to Yahtzee!')