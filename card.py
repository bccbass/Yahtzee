def valid_hand(hand):
    check_ints = [el for el in hand if type(el) == int] # filter for only ints
    return len(check_ints) == 5 # ensure there are exactly 5 ints in hand

def lrg_straight(hand):
    return len(set(hand)) == 5 and 1 and 6 not in hand

def sm_straight(hand):
    if len(set(hand)) == 4:
        sorted = list(set(hand))


def four_kind(hand):
    if len(set(hand)) == 2:
        hand.sort()
        return hand[0] != hand[1] or hand[3] != hand[4]

def full_house(hand):
    if len(set(hand)) == 2:
        hand.sort()
        return hand[0] == hand[1] and hand[3] == hand[4]
        



def yahtzee(hand):
    return len(set(hand)) == 1 


x = [9,5,4,3,6,1,67,3,55,6,55]
y = list(set(x))
y.sort()
print(y)
