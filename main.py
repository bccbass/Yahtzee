from DiceClass import Dice

Ben = Dice()

Ben.hand 
# Ben.new_roll() 
# Ben.hand 

def remove_prompt():
    remove = input("Remove: ")
    parsed = [int(el) for el in remove.split(' ') if len(el) == 1]
    return parsed

baddies = remove_prompt()


print(baddies)

Ben.update_hand(baddies)

Ben.hand
