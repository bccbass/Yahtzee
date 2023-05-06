from random import randint
from diceArt import dice_art, print_hand

class Dice:
    def __init__(self):
        self.__hand = self.roll(5)
        self.art = dice_art 

    @property
    def hand(self):
        print_hand(self.__hand)

    def new_roll(self):
        self.__hand = self.roll(5)

    def update_hand(self, baddies):
        for die in baddies:
            self.__hand.remove(die)
        re_roll_x = len(baddies)
        new_dice = self.roll(re_roll_x)
        self.__hand += new_dice
        
        
        

    

    @classmethod
    def die(cls, ):
        return randint(1, 6)
    @classmethod
    def roll(cls, num_dice):
        hand_cache = []
        for _ in range(num_dice):
            hand_cache.append(cls.die())
        return hand_cache
    @classmethod
    def remove(cls, bad_dice, hand):
        for die in bad_dice:
            hand.remove(die)
        return hand

    @classmethod
    def re_roll(cls, keeper_hand):
        re_roll_x = 5 - len(keeper_hand)
        new_dice = cls.roll(re_roll_x)
        return keeper_hand + new_dice

# print(Dice.die())
# print(Dice.roll(5))
# print(Dice.remove([1,2,3], [1,2,3,4,5,6]))
# print(Dice.re_roll([1]))
