from DiceClass import Dice
# players = input("Who's playing? ")

Ben = Dice()

# Ben.hand 
# Ben.new_roll() 
# Ben.hand 

def remove_prompt():
    remove = input("What dice would you like to reroll? (Press enter to keep hand): ")
    parsed = [int(el) for el in remove if el.isdigit()]
    return parsed


# def round():
#     Ben.new_roll()
#     chances = 2
#     Ben.hand
#     baddies = remove_prompt()
#     if baddies == 0:
#         return 

#     while chances > 2:
#         Ben.hand
#         baddies = remove_prompt()
#         Ben.update_hand(baddies)
#         chances -=1
#     Ben.hand






Ben.new_roll()
Ben.hand
baddies = remove_prompt()
Ben.update_hand(baddies)
Ben.hand
baddies = remove_prompt()
Ben.update_hand(baddies)
Ben.hand


# round()