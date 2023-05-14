from card import three_kind, four_kind, full_house, sm_straight, lg_straight, yahtzee
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
                print(Fore.YELLOW + ' ' + dice_art[die][i], end=Fore.RESET+'   ')
            print(' ')
        position_string = ''
        for key in self.__hand.keys():
            position_string += f'    Die {str(key)}      '
        print(Fore.YELLOW + position_string)
        print(Fore.RESET)
        
    @classmethod
    def die(cls):
        return randint(1, 6)
 

class Player: 
    round = 1
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
            print(f'\nWelcome back, {self.name}!')
        else:
            print(f'\nWelcome to Yahtzee, {self.name}!')

    @property
    def show_card(self):
        def calc_space(rule, str):
            res = ' '*(rule - len(str))
            return res 
        space = ' '*22
        plyr_rule = 14
        k_rule = 16
        v_rule = 6
        round = (
'┌────────────────────────────┐',
f'│       ***Round {self.round}***        │ ',     
f'│       {self.name}\'s Card{calc_space(plyr_rule, self.name)}│',     
'│────────────────────────────│')          
        for line in round:
            print(space + line)
        for k,v in self.card.game_board.items():
            print(
            space + f'│ *{k}*{calc_space(k_rule, k)}│  {v}{calc_space(v_rule, str(v))}│'
            )
        print(space + '└────────────────────────────┘\n\n')


class Card:
    def __init__(self):
        self.game_board = {
            'Three of a Kind': None,
            'Four of a Kind': None,
            'Full House': None,
            'Small Straight': None,
            'Large Straight': None,
            'Yahtzee!': None,
            'Chance': None
        }
        self.test_hand = [three_kind, four_kind, full_house, sm_straight, lg_straight, yahtzee]
        self.final_score = 0

# Calulates final score. This should only be called once, or else it will keep adding same card to final score.
    def calc_score(self):
        for k, v in self.game_board.items():
            if isinstance(v, int):
                self.final_score += v
        return self.final_score
            
    # takes a list and returns a numbered list: eg. [A,B,C] ->['[1] A', '[2] B', '[3] C']
    def enum_categories(self, categories):
        enum_list = []
        for i, el in enumerate(categories):
            enum_list.append(f'[{i+1}] {el}')
        return enum_list
    
    # Checks a hand against all categories to return any possible match.
    def check_hand(self, hand):
        res =[test(hand) for test in self.test_hand if test(hand)]
        res.append('Chance')
        return res

    def update_round_points(self, category, hand):
        match category:
            case 'Three of a Kind' | 'Four of a Kind' | 'Chance':
                self.game_board[category] = sum(hand)
            case 'Full House':
                self.game_board[category] = 25
            case 'Small Straight':
                self.game_board[category] = 30
            case 'Large Straight':
                self.game_board[category] = 40
            case 'Yahtzee!':
                if self.game_board[category] != None:
                    self.game_board[category] += 100
                else: self.game_board[category] = 50






