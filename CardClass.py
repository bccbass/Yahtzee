from card import three_kind, four_kind, full_house, sm_straight, lg_straight, yahtzee
from DiceClass import Dice

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
    
    # Checks a hand against all categories to return any possible match. This needs to accound for excluding already filled categories. 
    def check_hand(self, hand):
        res =[test(hand) for test in self.test_hand if test(hand)]
        res.append('Chance')
        return res
    

    # THIS WOULD BE AN IDEAL PLACE FOR EXCEPTION HANDLING WRT ONLY ONE VALUE PER CATEGORY - CHECK IF CAT IS FILLED THEN OPERATE
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



                

# test = Card('Ben')
# check = test.check_hand([1,1,1,2,2])
# print(check)