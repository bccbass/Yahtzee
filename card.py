def check_hand(self, hand):
    res =[test(hand) for test in self.test_hand if test(hand)]
    res.append('Chance')
    return res


def valid_hand(hand):
    check_ints = [el for el in hand if type(el) == int] # filter for only ints
    return len(check_ints) == 5 # ensure there are exactly 5 ints in hand

# def sm_straight(hand):
#     hand.sort()
#     if hand[-1]-1 != hand[-2]:
#         hand = hand[:-1]    
#     elif hand[0]+1 != hand[1]:
#         hand = hand[1:]
#     hand = set(hand)    
#     hand_str = ''.join([str(num) for num in hand])
#     if hand_str in '123456' and len(hand) in [4, 5]:
#         return 'Small Straight'

def sm_straight(hand):
    hand = list(set(hand))
    if len(hand) in [4, 5]:
        if hand[-1]-1 != hand[-2]:
            hand = hand[:-1]    
        elif hand[0]+1 != hand[1]:
            hand = hand[1:]
        hand_str = ''.join([str(num) for num in hand])
        if hand_str in '123456':
            return 'Small Straight'

def lg_straight(hand):
    if len(set(hand)) == 5:
        if 1 in hand and 6 not in hand or 6 in hand and 1 not in hand:
            return 'Large Straight'



def three_kind(hand):
    if len(set(hand)) in [2, 3]:
        hand.sort()
        if hand[0] == hand[2] or hand[-1] == hand[-3] or hand[1] == hand[3]:
            return 'Three of a Kind'



def four_kind(hand):
    if len(set(hand)) == 2:
        hand.sort()
        if hand[0] != hand[1] or hand[3] != hand[4]:
            return 'Four of a Kind'

def full_house(hand):
    if len(set(hand)) == 2:
        hand.sort()
        if hand[0] == hand[1] and hand[3] == hand[4]:
            return 'Full House'

def yahtzee(hand):
    if len(set(hand)) == 1:
        return 'Yahtzee!'





# functions for refactor - creating a dictionary and dict values from hand for all funcs to use
# These should maybe all be moved as methods of the Card class
# Could also implement logic sorting by length of set() before sending to tests

# def mk_hand_dict(hand):
#     hand_dict = {}
#     for key in hand:
#         if key not in hand_dict:
#             hand_dict[key] = 1
#         else:
#             hand_dict[key] +=1
#     return hand_dict

# def three_kind(hand):
#     d_hand = mk_hand_dict(hand)
#     d_vals = d_hand.values()
#     if len(set(hand)) in [2, 3]:
#         if 3 in d_vals or 4 in d_vals:
#             return 'Three of a Kind'
