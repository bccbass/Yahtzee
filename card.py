#Logic to test hands for valid categories from Yahtzee Card

def sm_straight(hand):
    hand.sort()
    if hand[-1]-1 != hand[-2]:
        hand = hand[:-1]    
    elif hand[0]+1 != hand[1]:
        hand = hand[1:]
    hand = set(hand)    
    hand_str = ''.join([str(num) for num in hand])
    if hand_str in '123456' and len(hand) in [4, 5]:
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
