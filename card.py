def valid_hand(hand):
    check_ints = [el for el in hand if type(el) == int] # filter for only ints
    return len(check_ints) == 5 # ensure there are exactly 5 ints in hand

def lrg_straight(hand):
    return len(set(hand)) == 5 and 1 and 6 not in hand

def sm_straight(hand):
    hand.sort()
    if hand[-1]-1 != hand[-2]:
        hand = hand[:-1]    
    elif hand[0]+1 != hand[1]:
        hand = hand[1:]
    hand = set(hand)    
    hand_str = ''.join([str(num) for num in hand])
    return hand_str in '123456'
def three_kind(hand):
    if len(set(hand)) in [2, 3]:
        hand.sort()
        if hand[0] == hand[2] or hand[-1] == hand[-3]:
            return True

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


x = [1,2,3,4,5]
print(sm_straight(x))
