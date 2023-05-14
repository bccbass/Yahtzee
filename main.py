import json
import subprocess
import time
from Classes import Dice

from pyfiglet import Figlet

from funcs import (check_py_version, game, init_log_file, 
                   create_user_instance, player_from_log, log_final_score, 
                   wrap_up_message, print_big_yahtzee, play_again_prompt)


def main():
    f = Figlet(font='slant', justify='center')  # clear terminal

    subprocess.call(['tput', 'reset'])  # clear screen

    check_py_version()  # check to make sure installed python version is compatible Yahtzee

    print_big_yahtzee()

    player = create_user_instance()  # create new Player instance for user

    dice = Dice()  # Initialize Dice object

    log = init_log_file()  # Check for score-log.json. Creates new json if corrupted or missing. Saves to log var.

    player_from_log(log, player)  # checks if player has previous history

    player.greet  # flashes brief personalized msg before game start
    time.sleep(1.2)

    game(player, dice)  # Call game function to start

    log = log_final_score(player, log)  # updates log with game results

    wrap_up_message(log, player)  # display score results/leaderboard

    with open('score-log.json', 'w') as f:  # write log to score-log.json
        json.dump(log, f, indent=2)

    play_again_prompt(main)  # asks user if they like to play again or exit

if __name__ == "__main__":
    main()