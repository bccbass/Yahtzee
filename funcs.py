import subprocess
import sys
import json

import colorama
from colorama import Fore
from pyfiglet import Figlet

from Classes import Player


colorama.init()
f = Figlet(font='slant', justify='center')


# Version Check:
def check_py_version():
    py_v_major = int(sys.version_info[0])
    py_v_minor = int(sys.version_info[1])
    if py_v_major < 3 and py_v_minor < 10:
        print('Yahtzee requires Python version 3.10 or higher')
        print('Visit https://www.python.org/downloads/ for more information')
        sys.exit(1)


# Utility functions
def space(num):
    return ' ' * num


def quit_game():
    res = None
    while res != 'y':
        res = input('Quit game? (Y/n) ').lower()
        if 'y' in res:
            sys.exit(0)
        if 'n' in res:
            break


def new_player_log(name):  # Create a log dict to store user scores in JSON file
    return {
        'name': name,
        'high_score': 0,
        'past_scores': []
    }


# Input verification functions:
def input_filter(input_res):
    parsed_input = input_res.strip()
    if parsed_input == 'RESET':
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
            reset_game_history()
        case 'h':
            show_help()
        case 'q':
            quit_game()


def is_valid_die(dice_str):
    if type(dice_str) == str:
        for die in dice_str:
            if die.isdigit() and 0 < int(die) < 6:
                continue
            else:
                return False
        return True


# FILE HANDLING:
def init_log_file():
    try:
        with open('score-log.json', 'r') as f:  # open json file and set contents to var log
            log = json.load(f)
    except:
        res = None
        while res != 'r':
            res = input('Whoops!! Cannot find \'scores-log.json\'. Would you like to [R]eset Game Log or [Q]uit? ').strip().lower()
            if res == 'r':
                reset_game_history()
                with open('score-log.json', 'r') as f:  # open json file and set contents to var log
                    log = json.load(f)
            if res.lower() == 'q':
                    quit_game()
            else:
                print('Please enter a valid input ([Q]uit or [R]eset)')
    return log


def player_from_log(log, target_player):
    try:    # find and return name if player is already in log.
        if log[1][target_player.name.lower()]:
            plyr = log[1][target_player.name.lower()]
            return plyr
    except:
        target_player.new()  # invoke method to change is_new to True on player instance
        new_player = new_player_log(target_player.name)  # create new log object for player
        log[1][target_player.name.lower()] = new_player  # creates new log on json dict
        return log[1][target_player.name.lower()]  # returns current player


def reset_game_history():
    subprocess.call('./clear-score-log.sh')
    print(Fore.GREEN + 'Game history cleared!' + Fore.RESET)


# Constructs new game history entry and updates/returns new log for JSON file.
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


# UI/PROMPTS:
def remove_prompt():
    dice = 'No dice'
    while not is_valid_die(dice):
        dice = input(Fore.RESET + "What dice would you like to re-roll? (Enter input position of dice to re-roll (1-5) and press <ENTER> or press <ENTER> to keep hand): ")
        filter_res = input_filter(dice)
        if filter_res:
            match_request(filter_res)
        elif not is_valid_die(dice):
            print("Enter valid die numbers (1-5)")
        else:
            parsed_dice = [int(die) for die in dice]
            return parsed_dice


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
            req_filter = input_filter(i)
            if req_filter:
                match_request(req_filter)
            elif int(i) not in valid_choice:
                raise ValueError('Please choose valid a valid number')
            else:
                return int(i) - 1
        except ValueError:
            print('Please choose valid a valid number')


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
        input_req = input_filter(again)
        match_request(input_req)
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
    print(Fore.RESET)


def show_help():
    justify = space(8)
    msg = [
        '\n',
        '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯'*3,
        justify*3 + '     ✯      Welcome to Yahtzee!     ✯',
        '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯'*3,
        '● Enter [Q]uit or [H]elp at any time.',
        '● To clear the Game Log history type RESET and press <ENTER>',
        '● The goal of the game is to get all categories of hands and earn the highest score.',
        '● You can only check off one category per game, so choose wisely.',
        '● Highest score wins!! Have fun!!',
        '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯'*3 + Fore.RESET
    ]
    for line in msg:
        print(Fore.CYAN + justify + line + '\n')
    print(Fore.YELLOW)
    res = None
    while res == None:
        res = input(space(40) + 'Press <ENTER> to continue\n' + Fore.RESET)


def calc_space(rule, str):
    res = ' '*(rule - len(str))
    return res


def print_champions(log, champion):
    subprocess.call(['tput', 'reset'])
    if champion:
        print(Fore.CYAN + f.renderText(f'{champion} is the NEW CHAMPION!'))
    else:
        print_big_yahtzee()
    champions = find_champions(log)
    k_rule = 20
    v_rule = 4
    space = ' '*18
    round = (
        space + Fore.YELLOW + '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯', 
        space + '✯                                     ✯',      
        space + '✯     ✯✯✯ ALL TIME CHAMPIONS ✯✯✯      ✯',      
        space + '✯                                     ✯',      
        space + '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯', 
        space + '✯' + ' '*37 + '✯'
        ) 
    count = 1
    for line in round:
        print(line)
    for k, v in champions:
        print(
            space + f'✯   #{count} {k.upper()}{calc_space(k_rule, k)}   {v}{calc_space(v_rule, str(v))}    ✯')
        print(space + '✯' + ' '*37 + '✯')
        count += 1
    print(space + '✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯✯\n\n' + Fore.RESET)


# Game Play Functions:
def game(player, dice):
    for i in range(len(player.card.game_board)):
        subprocess.call(['tput', 'reset'])
        print(Fore.CYAN + f.renderText(f'Round {Player.round}\n'))
        round(dice, player)
        Player.round += 1
    Player.round = 1
    # caluclates final score and adds it to final score on card
    player.card.calc_score()


def create_user_instance():
    # functionality to accept multiple players for extended features
    players = []
    player_instances = []
    # to refactor for multiple players us while loop to seed players
    player = None
    while True:
        player = input('Who is playing? ') or 'Lil Champion'  # request player name, if '' default is given
        req_filter = input_filter(player)
        if req_filter:
            match_request(req_filter)
            continue
        elif len(player) > 16:
            print('Players names have a maximum length of 16')
        else:
            players.append(player)
            break
    for player in players:
        new_instance = Player(player)
        player_instances.append(new_instance)
    return player_instances[0]


def round(dice, player):
    chances = 1
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


def print_round(dice, player, chances):
    subprocess.call(['tput', 'reset'])
    print(Fore.CYAN + f.renderText(f'Round {Player.round}\n'))
    player.show_card
    print(Fore.YELLOW + space(28) + f'***Roll {chances} of 3***')
    dice.hand


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