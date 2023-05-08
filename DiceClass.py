from random import randint
from diceArt import dice_art
import colorama
from colorama import Fore
colorama.init()

class Dice:
    def __init__(self):
        self.__hand = None
        self.art = dice_art 

    @property
    def hand(self):
        # hand_values = self.__hand.values()
        self.print_hand()

    def list(self):
        return list(self.__hand.values())
    def fresh_hand(self):
        self.hand = self.new_roll()

    def new_roll(self):
            self.__hand = {
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
        
    @classmethod
    def die(cls):
        return randint(1, 6)
 
 