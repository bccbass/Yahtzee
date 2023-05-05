from random import randint

def die():
    return randint(1, 6)

def roll_dice(num_dice):
    hand_cache = []
    for _ in range(num_dice):
        hand_cache.append(die())
    return hand_cache

def remove_dice_fr_hand(bad_dice, hand):
    for die in bad_dice:
        hand.remove(die)
    return hand


def re_roll_dice(keeper_hand):
    re_roll_x = 5 - len(keeper_hand)
    new_dice = roll_dice(re_roll_x)
    return keeper_hand + new_dice



# hand = roll_dice(5)
# reroll = re_roll_dice([1,2,3])

# print(remove_dice_fr_hand([1,2,3], [1,2,3,4,5,6]))
# print('reroll: ', re_roll_dice([1]))
# print('reroll-> ', reroll)
# print('Yahtzee hand -> ', hand)

# reroll = input('Nice roll! What numbers would you like to re-roll? ')


# reroll = reroll.split(' ')
# print(reroll)



