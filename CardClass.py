from card import three_kind, four_kind, full_house, sm_straight, lg_straight, yahtzee
from DiceClass import Dice

class Card: 
    def __init__(self, player='player'):
        self.player = player
        self.card = {
            'three_kind': None,
            'four_kind': None,
            'full_house': None,
            'sm_straight': None,
            'lg_straight': None,
            'yahtzee': None,
            'chance': None
        }
        self.test_hand = [three_kind, four_kind, full_house, sm_straight, lg_straight, yahtzee]

    def check_hand(self, hand):
        res =[test(hand) for test in self.test_hand if test(hand)]
        res.append('Chance')
        return res

# test = Card('Ben')
# check = test.check_hand([1,1,1,2,2])
# print(check)