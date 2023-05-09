import json
from DiceClass import Dice
from funcs import game, create_user_instance, log_final_score, wrap_up_message, player_from_log, play_again_prompt
import colorama
from colorama import Fore
colorama.init()
from pyfiglet import Figlet
from playsound import playsound

colorama.init()


def main():
    f = Figlet(font='slant', justify='center')

    print(Fore.CYAN + f.renderText('Yahtzee!'))

    player = create_user_instance()
    # Initialize Dice object
    dice = Dice()


    with open('score-log.json', 'r') as f: # open json file and set contents to var log
        log = json.load(f)

    current_players_log = player_from_log(log, player)




    # playsound('./Yahtzee_Remix.mp3')
    # Call game function to start:
    game(player, dice)

    log = log_final_score(player, log)

    wrap_up_message(log, player.name)

    with open('score-log.json', 'w') as f:
        json.dump(log, f, indent=2)

    play_again_prompt(main)


if __name__ == "__main__":
    main()