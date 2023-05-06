from random import randint
from diceArt import dice_art
import colorama
from colorama import Fore
colorama.init()

class Dice:
    def __init__(self):
        self.__hand = self.new_roll()
        self.art = dice_art 

    @property
    def hand(self):
        # hand_values = self.__hand.values()
        self.print_hand()

    def new_roll(self):
            return {
            1: self.die(),
            2: self.die(),
            3: self.die(),
            4: self.die(),
            5: self.die(),
        }

    def update_hand(self, baddies):
        for key in baddies:
            self.__hand[key] = self.die()

    def print_hand(self):
        for i in range(5):
            for die in self.__hand.values():
                print(Fore.YELLOW + dice_art[die][i], end=Fore.RESET+'   ')
            print(' ')
        position_string = ''
        for key in self.__hand.keys():
            position_string += f'   Die {str(key)}      '
        print(Fore.YELLOW + position_string)
        print(Fore.RESET)

# for Hand as LIST:
    # def update_hand(self, baddies):
    #     for die in baddies:
    #         self.__hand.remove(die)
    #     re_roll_x = len(baddies)
    #     new_dice = self.roll(re_roll_x)
    #     self.__hand += new_dice



        
        
        

    

    @classmethod
    def die(cls):
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

