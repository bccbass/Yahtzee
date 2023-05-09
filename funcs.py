from PlayerClass import Player
import subprocess
import sys
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

def wrap_up_message(log, player_name):
    champion, all_time_high = log[0]['all_time_high']
    name, high_score, past_scores = log[1][player_name.lower()].values()
    subprocess.call(['tput', 'reset'])
    print(Fore.CYAN + f.renderText(f'YAHTZEE!'))
    if past_scores[-1] == all_time_high:
        subprocess.call(['tput', 'reset'])
        print(Fore.CYAN + f.renderText(f'{champion} is the NEW CHAMPION!'))
        print(f'Congratulations {champion}!! You have the all time high score of {all_time_high}!')
    elif past_scores[-1] == high_score and len(past_scores) > 1:
        print(f'Congratulations! You have a new high score of {high_score}!!')
    else:
        print(f'Your final score is {past_scores[-1]} points! Nice one, legend!')

def play_again_prompt(game):
    while True:
        again = input("Play again? (Y/n): ").lower()
        if again == 'y':
            break
        elif again == 'n':
            sys.exit(0)
        else:
            print('Sorry, I didn\'t understand your response!')
    game()

# GAME VARIABLE CONSTRUCTION
def create_user_instance():
    # functionality to accept multiple players for extended features
    players = []
    player_instances = []
    # to refactor for multiple players us while loop to seed players
    player = input('Who is playing? ') or 'Lil Champion' #request player name, if '' default is given
    players.append(player)
    for player in players:
        new_instance = Player(player)
        player_instances.append(new_instance)
    return player_instances[0]


def new_player_log(name): # Create a log dict to store user scores in JSON file 
   return {
    'name': name,
    'high_score': 0,
    'past_scores': []
    }

def player_from_log(log, target_player):
    try:    # find and return name if player is already in log.
        if log[1][target_player.name.lower()]:
            plyr = log[1][target_player.name.lower()]
            return plyr
    except:
        target_player.new() # invoke method to change is_new to True on player instance
        new_player = new_player_log(target_player.name) # create new log object for player 
        log[1][target_player.name.lower()] = new_player # creates new log on json dict
        return log[1][target_player.name.lower()] # returns current player


def log_final_score(player, log):
    # update players scores for log
    final_score = player.card.final_score
    all_time_high = log[0]["all_time_high"][1]
    player_log = log[1][player.name.lower()]
    player_log['past_scores'].append(final_score)
    if player_log['high_score'] < final_score:
        player_log['high_score'] = final_score
    if all_time_high < final_score:
        log[0]["all_time_high"] = [player.name, final_score]
        champion, all_time_high = log[0]["all_time_high"]
    return log

        

# GAMEPLAY/GAMEFLOW
def round(dice, player):
    chances = 2
    dice.new_roll()
    player.show_card    
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



def game(player, dice):
    # for i in range(len(player.card.game_board)):
    for i in range(2):
        subprocess.call(['tput', 'reset'])
        print(Fore.CYAN + f.renderText(f'Round {Player.round}'))
        if Player.round == 1:
            player.greet
        round(dice, player)
        Player.round +=1
    # caluclates final score and adds it to final score on card
    player.card.calc_score()

        
    
