import json
from DiceClass import Dice
from funcs import game, create_user_instance
from PlayerLog import PlayerLog

player = create_user_instance()


# Create a log dict to store user scores in JSON file 
def create_new_log(name):
   return {
    'name': name,
    'high_score': 0,
    'past_scores': []
    }

# isolate player from json file and return index
def player_from_log(log, target_player):
    for i, el in enumerate(log):
        if el['name'] == target_player:
            return [i, el]
        
# Create empty log to store JSON object from file
log = None

with open('score-log.json', 'r') as f:
    log = json.load(f)

if any(player.name in el['name'] for el in log):
    print(f'Welcome back {player.name}!')
else: 
    log.append(create_new_log(player.name))

# Find user from log:
current_players_log = player_from_log(log, player.name)


with open('score-log.json', 'w') as f:
    json.dump(log, f, indent=2)

# Initialize Dice object
dice = Dice()

# Call game function to start:
game(player, dice)





