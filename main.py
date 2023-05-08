import json
from DiceClass import Dice
from funcs import game, create_user_instance
from PlayerLog import PlayerLog
import colorama
from colorama import Fore
colorama.init()
from pyfiglet import Figlet

colorama.init()
f = Figlet(font='slant', justify='center')



print(Fore.CYAN + f.renderText('Yahtzee!'))

player = create_user_instance()


# Create a log dict to store user scores in JSON file 
def create_new_log(name):
   return {
    'name': name,
    'high_score': 0,
    'past_scores': []
    }

# Takes current player from term input and checks agains log. If returning player result is player el from log. 
    # If new player 'new' flag is true on player obj and new log dict is created/appended to log. 
def player_from_log(log, target_player):
    # find and return name if player is already in log.
    name = [el for el in log if el['name'].lower() == target_player.lower()]
    if len(name):
        return name[0]
    else:
        # invoke method to change is_new to True on player instance
        player.new()
        # create new log object for player and append to json target
        new_player = create_new_log(player.name)
        log.append(new_player)
        # returns current player
        return new_player
# Create empty log to store JSON object from file
log = None

# open json file and set contents to var log
with open('score-log.json', 'r') as f:
    log = json.load(f)

current_players_log = player_from_log(log, player.name)





# Initialize Dice object
dice = Dice()

# Call game function to start:
game(player, dice)

# Final score wrap up and storage:
# isolates final score from card as var
final_score = player.card.final_score
# update players scores for log
current_players_log['past_scores'].append(final_score)
if current_players_log['high_score'] < final_score:
    current_players_log['high_score'] = final_score
    print(f'Congratulations! You have a new high score of {final_score}!!')
else:
    print(f'Congratulations! You have {final_score} points!')


with open('score-log.json', 'w') as f:
    json.dump(log, f, indent=2)