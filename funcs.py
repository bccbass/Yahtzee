from random import randint

def die():
    return randint(1, 6)

def roll_dice(num_dice):
    hand_cache = []
    for die in range(num_dice):
        x = die()
        hand_cache.append(x)
    return hand_cache

def remove_dice_fr_hand(bad_dice, hand):
    for die in bad_dice:
        hand.remove(die)
    return hand


def re_roll_dice(keeper_hand):
    re_roll_x_times = 5 - len(keeper_hand)
    for i in range(re_roll_x_times):
        keeper_hand.append(keeper_hand)
    # re_roll = roll_dice(re_roll_x_times)
    # for die in re_roll:
    #     keeper_hand.append(die)
    return keeper_hand



print(die())
print(roll_dice(5))

# hand = roll_dice(5)
# reroll = re_roll_dice([1,2,3])

# print(remove_dice_fr_hand([1,2,3], [1,2,3,4,5,6]))
# print('reroll-> ', reroll)
# print('Yahtzee hand -> ', hand)

# reroll = input('Nice roll! What numbers would you like to re-roll? ')


# reroll = reroll.split(' ')
# print(reroll)