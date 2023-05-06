from CardClass import Card

def remove_prompt():
    remove = input("What dice would you like to reroll? (Input position of dice to re-roll. Press enter to keep hand): ")
    parsed = [int(el) for el in remove if el.isdigit()]
    return parsed

def round(dice, card):
    chances = 2
    dice.new_roll()
    dice.hand
    while chances > 0:   
        res = remove_prompt()
        if res == '':
            break
        else:
            dice.update_hand(res)
            dice.hand
            chances -= 1
        print(card.check_hand(dice.list()))
        
    
