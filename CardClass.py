import card
from DiceClass import Dice

class Card: 
    def __init__(self, name='player'):
        self.player = name
        # self.hand = Dice()

    
    def showhand(self):
         print(self.hand.hand())
         self.hand = self.hand.new_roll()
         print(self.hand.hand())