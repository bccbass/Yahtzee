def remove_prompt():
    remove = input("What dice would you like to reroll? (Input position of dice to re-roll. Press enter to keep hand): ")
    parsed = [int(el) for el in remove if el.isdigit()]
    return parsed

def round(player):
    chances = 2
    player.hand.new_roll()
    player.hand.hand
    while chances > 0:   
        res = remove_prompt()
        if res == '':
            break
        else:
            player.hand.update_hand(res)
            player.hand.hand
            chances -= 1
