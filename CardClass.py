from card import three_kind, four_kind, full_house, sm_straight, lg_straight, yahtzee
from DiceClass import Dice

class Card: 
    def __init__(self, player='player'):
        self.player = player
        self.card = {
            'Three of a Kind': None,
            'Four of a Kind': None,
            'Full House': None,
            'Small Straight': None,
            'Large Straight': None,
            'Yahtzee!': None,
            'Chance': None
        }
    

        
        self.test_hand = [three_kind, four_kind, full_house, sm_straight, lg_straight, yahtzee]

    def enum_categories(self, categories):
        enum_list = []
        for i, el in enumerate(categories):
            enum_list.append(f'[{i+1}] {el}')
        return enum_list

    def check_hand(self, hand):
        res =[test(hand) for test in self.test_hand if test(hand)]
        res.append('Chance')
        return res
    

    # THIS WOULD BE AN IDEAL PLACE FOR EXCEPTION HANDLING WRT ONLY ONE VALUE PER CATEGORY - CHECK IF CAT IS FILLED THEN OPERATE
    def update_round_points(self, category, hand):
        match category:
            case 'Three of a Kind' | 'Four of a Kind' | 'Chance':
                self.card[category] = sum(hand)
            case 'Full House':
                self.card[category] = 25
            case 'Small Straight':
                self.card[category] = 30
            case 'Large Straight':
                self.card[category] = 40
            case 'Yahtzee!':
                if self.card[category] != None:
                    self.card[category] += 100
                else: self.card[category] = 50



                

# test = Card('Ben')
# check = test.check_hand([1,1,1,2,2])
# print(check)