from CardClass import Card
import colorama
from colorama import Fore, Back
from pyfiglet import Figlet

colorama.init()
f = Figlet(font='slant', justify='center')


def remove_prompt():
    remove = input("What dice would you like to reroll? (Input position of dice to re-roll. Press enter to keep hand): ")
    parsed = [int(el) for el in remove if el.isdigit()]
    return parsed

def choose_category(evaluated_hand):
    print('What category would you like to apply hand to?:')
    cat_str = ' '.join([el for el in evaluated_hand])
    print(Fore.YELLOW + cat_str)        
    i = int(input())
    return i - 1

        


def round(dice, card):
    chances = 2
    dice.new_roll()
    dice.hand
    while chances > 0:   
        res = remove_prompt()
        if not len(res):
            break
        else:
            dice.update_hand(res)
            dice.hand
            chances -= 1
    valid_categories = card.check_hand(dice.list())
    formatted_categories = card.enum_categories(valid_categories)
    i = choose_category(formatted_categories)
    players_category_choice = valid_categories[i]
    card.update_round_points(players_category_choice, dice.list())
    print(card.card)


def game(card, dice):
    print(Fore.CYAN + f.renderText('Yahtzee!'))

    for i in range(len(card.card)):
        print(Fore.YELLOW + f'ROUND {i+1}\n!!')

        round(dice, card)
    

    # Print numbered elements on their own without brackets
        
    
