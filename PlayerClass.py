from CardClass import Card

class Player: 
    def __init__(self, name='player'):
        self.name = name
        self.high_score = 0
        self.card = Card()

    @property
    def greet(self):
        if self.name != 'player':
            print(f'Welcome back {self.name}!')
        if self.high_score > 0:
            print(f'Your highest score on record is {self.high_score}')