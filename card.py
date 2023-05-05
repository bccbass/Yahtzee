def valid_hand(hand):
    check_ints = [el for el in hand if type(el) == int] # filter for only ints
    return len(check_ints) == 5 # ensure there are exactly 5 ints in hand

def lrg_straight(hand):
    if valid_hand(hand):
        return len(set(hand)) == 5 and 1 and 6 not in hand

def four_kind(hand):
    if valid_hand(hand):
        if len(set(hand)) == 2:
            hand.sort()
            return hand[0] != hand[1] or hand[3] != hand[4]


def yahtzee(hand):
    if valid_hand(hand):
        return len(set(hand)) == 1 


print(lrg_straight([1,2,3, 4.5, 'j', True]))