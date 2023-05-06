from DiceClass import Dice
# players = input("Who's playing? ")

Ben = Dice()

# Ben.hand 
# Ben.new_roll() 
# Ben.hand 

def remove_prompt():
    remove = input("What dice would you like to reroll? (Input position of dice to re-roll. Press enter to keep hand): ")
    parsed = [int(el) for el in remove if el.isdigit()]
    return parsed










Ben.new_roll()
Ben.hand
baddies = remove_prompt()
Ben.update_hand(baddies)
Ben.hand
baddies = remove_prompt()
Ben.update_hand(baddies)
Ben.hand


# round()