from PlayerClass import Player
import subprocess
import sys
import json
import colorama
from colorama import Fore, Back
from pyfiglet import Figlet


colorama.init()
f = Figlet(font='slant', justify='center')

# Version Check:
def check_py_version():
    py_v_major = int(sys.version_info[0])
    py_v_minor = int(sys.version_info[1])
    if py_v_major < 3 and py_v_minor < 10:
        print('Yahtzee requires Python version 3.10 or higher\nVisit https://www.python.org/downloads/ for more information')
        sys.exit(1)



# PROMPTS:
def space(num):
    return ' ' * num


# THIS IS ONLY WORKING WITH SINGLE LETTERS, NOT FULL WORD RESET OR HELP OR QUIT
# INPUT HANDLER WITH SAME LOGIC IS WORKING. DONT KNOW WHY
def input_filter(input_res):
    parsed_input = input_res.strip().lower()
    if parsed_input == 'reset':
        return 'r'
    if parsed_input in ['q', 'quit'] or 'quit' in parsed_input:
        return 'q'
    elif parsed_input in ['h', 'help']:
        return 'h'
    else:
        return False

def match_request(req_key):
    match req_key:
        case 'r':
            subprocess.call('./clear-score-log.sh')
            print(Fore.GREEN + 'Game history cleared!' + Fore.YELLOW)
        case 'h':
            help()
        case 'q':
            quit_game()

def quit_game():
    res = None
    while res != 'y':
        res = input('Quit game? (Y/n) ').lower()
        if 'y' in res:
            sys.exit(0)
        if 'n' in res:
            break

def init_log_file():
    try:
        with open('score-log.json', 'r') as f: # open json file and set contents to var log
            log = json.load(f)
    except:
        res = None
        while res != 'r':
            res = input('Whoops!! Cannot find \'scores-log.json\'. Would you like to [R]eset Game Log or [Q]uit? ' ).strip().lower()
            if res == 'r': 
                reset_game_history()
                with open('score-log.json', 'r') as f: # open json file and set contents to var log
                    log = json.load(f)
            if res.lower() == 'q':
                    quit_game()
            else:
                print('Please enter a valid input ([Q]uit or [R]eset)')
    return log

def reset_game_history():
    subprocess.call('./clear-score-log.sh')
    print(Fore.GREEN + 'Game history cleared!' + Fore.YELLOW)

def input_handler(input_res):
    parsed_input = input_res.strip().lower()
    if parsed_input == 'reset':
        reset_game_history()
    if parsed_input in ['q', 'quit'] or 'quit' in parsed_input:
        quit_game()
    elif parsed_input in ['h', 'help']:
        help()


# def remove_prompt():
#     remove = input("What dice would you like to re-roll? (Input position of dice to re-roll and press <ENTER> OR just press <Enter> to keep hand): ")
#     while True:
#         remove = input("What dice would you like to re-roll? (Input position of dice to re-roll and press <ENTER> OR just press <Enter> to keep hand): ")
#         input_handler(remove)
#         for el in remove:
#             if el not in '12345':
#                 print("Please enter valid dice numbers only")
#         else:
#             parsed = [int(el) for el in remove if el.isdigit() and 0 < int(el) < 6]
#             return parsed

# def is_valid_die(dice_str):
#     if type(dice_str) == 'string':
#         try:
#             for die in dice_str:
#                 if 0 < int(die) < 6:
#                     continue
#         except ValueError("Please enter valid die numbers"):
#             return False
#         return True
#     else:
#         return False
def is_valid_die(dice_str):
    if type(dice_str) == str:
        for die in dice_str:
            if die.isdigit() and 0 < int(die) < 6:
                continue
            else: 
                return False
        return True



def remove_prompt():
    dice = 'No dice'
    while not is_valid_die(dice):
        dice = input(Fore.RESET + "What dice would you like to re-roll? (Enter input position of dice to re-roll (1-5) and press <ENTER> OR just press <Enter> to keep hand): ")
        filter_res = input_filter(dice)
        if filter_res: 
            match_request(filter_res)
        elif not is_valid_die(dice):
            print("Enter valid die numbers (1-5)")
        else:
            parsed_dice = [int(die) for die in dice]
            return parsed_dice

# def remove_prompt():
#     remove = input("What dice would you like to re-roll? (Input position of dice to re-roll and press <ENTER> OR just press <Enter> to keep hand): ")
#     input_handler(remove)
#     parsed = [int(el) for el in remove if el.isdigit() and 0 < int(el) < 6]
#     return parsed

def choose_category(evaluated_hand):
    cat_str = ' '.join([el for el in evaluated_hand])
    valid_choice = [1]
    for el in evaluated_hand:
        valid_choice.append(valid_choice[-1]+1)
    while True:
        try:
            print('What category would you like to apply hand to?:')
            print(Fore.YELLOW + cat_str + Fore.RESET)
            i = input()
            input_handler(i)
            i = int(i)
            if i in valid_choice:
                break
            else:
                raise ValueError('Please choose valid a valid number')
        except ValueError:
            print('Please choose valid a valid number')

    return i - 1

def wrap_up_message(log, player):
    champion, all_time_high = log[0]['all_time_high']
    name, high_score, past_scores = log[1][player.name.lower()].values()
    subprocess.call(['tput', 'reset'])
    space = ' ' * 16
    next_screen = None
    is_champion = False
    while next_screen == None:
        print(Fore.CYAN + f.renderText(f'Game Over!'))
        player.show_card
        if past_scores[-1] == all_time_high:
            is_champion = player.name
            # subprocess.call(['tput', 'reset'])
            # print(Fore.CYAN + f.renderText(f'{champion} is the NEW CHAMPION!'))
            print(space + f'Congratulations {champion}!! You have the all time high score of {all_time_high}!')
        elif past_scores[-1] == high_score and len(past_scores) > 1:
            print(space + f'Congratulations! You have a new high score of {high_score}!!')
        else:
            print(space + f'Your final score is {past_scores[-1]} points! Nice one!')
        next_screen = input('\nPress <ENTER> to continue...')
    print_champions(log, is_champion)

def play_again_prompt(game):
    while True:
        again = input('\nPlay again? (Y/n) ').lower()
        input_handler(again)
        if again == 'y':
            break
        elif again == 'n':
            print('\nBye!\n')
            sys.exit(0)
    game()

def print_big_yahtzee():
    print(Fore.CYAN + f.renderText('-------------'))
    print(Fore.RED+f.renderText('Yahtzee!'), end='')
    print(Fore.CYAN + f.renderText('-------------'))


# GAME VARIABLE CONSTRUCTION

def create_user_instance():
    # functionality to accept multiple players for extended features
    players = []
    player_instances = []
    # to refactor for multiple players us while loop to seed players
    player = input('Who is playing? ') or 'Lil Champion' #request player name, if '' default is given
    input_handler(player)
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

def find_champions(log):
    player_tuples = [(log[1][el]['name'], log[1][el]['high_score']) for el in log[1]]
    high_scores = [el[1] for el in player_tuples]
    high_scores.sort(reverse=True)
    top_three = high_scores[:3]
    champions = []
    for num in top_three:
        for plyr in player_tuples:
            if num == plyr[1]:
                champions.append(plyr)
    return champions 

def print_champions(log, champion):
    subprocess.call(['tput', 'reset'])
    if champion:
        print(Fore.CYAN + f.renderText(f'{champion} is the NEW CHAMPION!'))
    else:
        print_big_yahtzee()
    champions = find_champions(log)
    def calc_space(rule, str):
        res = ' '*(rule - len(str))
        return res 
        
    k_rule = 12
    v_rule = 12
    space = ' '*22
    round = (
space +'✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯',
space +'✯   ✯✯✯ALL TIME CHAMPIONS✯✯✯   ✯',     
space +'✯                              ✯',     
space +'✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯')          
    for line in round:
        print(line)
    for k,v in champions:
        print(
       space + f'✯   {k.upper()}{calc_space(k_rule, k)}   {v}{calc_space(v_rule, str(v))}✯'
        )
    print(space +'✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯\n\n')

def help():
    justify = space(8)
    msg = [
        '\n',
        '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯'*3,
        justify*3 + '     ✯      Welcome to Yahtzee!     ✯',
        '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯'*3,
        '● Enter [Q]uit or [H]elp at any time.',
        '● To clear the Game Log history type RESET and press <enter>',
        '● The goal of the game is to get all categories of hands and earn the highest score.',
        '● You can only check off one category per game, so choose wisely.',
        '● If you cannot or do not want to fill a category in a round you can choose to take 0 points.',
        '● Highest score wins!! Have fun!!',
        # '**********PRESS ANY KEY TO CONTINUE**********',
        '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯'*3
    ]
    for line in msg:
        print(Fore.CYAN + justify + line)
        print(Fore.YELLOW)
    res = None
    while res == None:
        res = input(space(43) + 'Press <ENTER> to continue\n')



# GAMEPLAY/GAMEFLOW
def print_round(dice, player, chances):
    subprocess.call(['tput', 'reset'])
    print(Fore.CYAN + f.renderText(f'Round {Player.round}\n'))
    player.show_card
    print(Fore.YELLOW + space(28) + f'***Roll {chances} of 3***')
    dice.hand

def round(dice, player):
    chances =  1
    dice.new_roll()
    print_round(dice, player, chances)
    
    while chances < 3:
        res = remove_prompt()
        if not len(res):
            break
        else:
            dice.update_hand(res)
            chances += 1
            print_round(dice, player, chances)
           

    valid_categories = player.card.check_hand(dice.list())
    formatted_categories = player.card.enum_categories(valid_categories)
    i = choose_category(formatted_categories)
    players_category_choice = valid_categories[i]
    player.card.update_round_points(players_category_choice, dice.list())

def game(player, dice):
    for i in range(len(player.card.game_board)):
    # for i in range(2):
        subprocess.call(['tput', 'reset'])
        print(Fore.CYAN + f.renderText(f'Round {Player.round}\n'))
        if Player.round == 1:
            player.greet
        round(dice, player)
        Player.round +=1
    Player.round = 1
    # caluclates final score and adds it to final score on card
    player.card.calc_score()

        
    
