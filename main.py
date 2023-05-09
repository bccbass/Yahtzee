import json
from DiceClass import Dice
from funcs import game, create_user_instance, log_final_score, wrap_up_message, player_from_log
import colorama
from colorama import Fore
colorama.init()
from pyfiglet import Figlet

colorama.init()
f = Figlet(font='slant', justify='center')



print(Fore.CYAN + f.renderText('Yahtzee!'))

player = create_user_instance()

with open('score-log.json', 'r') as f: # open json file and set contents to var log
    log = json.load(f)

current_players_log = player_from_log(log, player)





# Initialize Dice object
dice = Dice()

# Call game function to start:
game(player, dice)





log = log_final_score(player, log)


wrap_up_message(log, player.name)

with open('score-log.json', 'w') as f:
    json.dump(log, f, indent=2)
