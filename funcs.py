from PlayerClass import Player
import subprocess
import colorama
from colorama import Fore, Back
from pyfiglet import Figlet

colorama.init()
f = Figlet(font='slant', justify='center')

# PROMPTS:
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


def create_user_instance():
    # functionality to accept multiple players for extended features
    players = []
    player_instances = []
    # to refactor for multiple players us while loop to seed players
    player = input('Who is playing? ')
    players.append(player)
    for player in players:
        new_instance = Player(player)
        player_instances.append(new_instance)
    return player_instances[0]

        

# GAMEPLAY/GAMEFLOW
def round(dice, player):
    chances = 2
    dice.new_roll()
    print(player.card.game_board)
    dice.hand

    while chances > 0:   
        res = remove_prompt()
        if not len(res):
            break
        else:
            dice.update_hand(res)
            dice.hand
            chances -= 1
    valid_categories = player.card.check_hand(dice.list())
    formatted_categories = player.card.enum_categories(valid_categories)
    i = choose_category(formatted_categories)
    players_category_choice = valid_categories[i]
    player.card.update_round_points(players_category_choice, dice.list())
    print(player.card.game_board)
    subprocess.call(['tput', 'reset'])



def game(player, dice):
    player.greet
    subprocess.call(['tput', 'reset'])

    # for i in range(len(player.card.game_board)):
    for i in range(2):
        print(Fore.CYAN + f.renderText('Yahtzee!'))
        print(Fore.YELLOW + f'┌─────────┐\n│ ROUND {i+1} │\n└─────────┘')

        round(dice, player)
    # caluclates final score and adds it to final score on card
    player.card.calc_score()

    # Print numbered elements on their own without brackets
        
    
