from DiceClass import Dice
from CardClass import Card
from funcs import remove_prompt, game, create_user_instance
import card


players = create_user_instance()
player = players[0]
print(player.card.game_board)
dice = Dice()

game(player, dice)