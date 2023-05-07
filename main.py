from DiceClass import Dice
from CardClass import Card
from funcs import remove_prompt, game, create_user_instance
import card


players = create_user_instance(Card)
player = players[0]
dice = Dice()

game(player, dice)