from CardClass import Card

class Player: 
    round = 1
    def __init__(self, name='player'):
        self.is_new = False
        self.name = name
        self.high_score = 0
        self.card = Card()
    def new(self):
        self.is_new = True
    @property
    def greet(self):
        if not self.is_new:
            print(f'Welcome back {self.name}!')
        else:
            print(f'Welcome to Yahtzee, {self.name}!')

    @property
    def show_card(self):
        def calc_space(rule, str):
            res = ' '*(rule - len(str))
            return res 
        space = ' '*22
        plyr_rule = 14
        k_rule = 16
        v_rule = 6
        round = (
'┌────────────────────────────┐',
f'│       ***Round {self.round}***        │ ',     
f'│       {self.name}\'s Card{calc_space(plyr_rule, self.name)}│',     
'│────────────────────────────│ ')          
        for line in round:
            print(space + line)
        for k,v in self.card.game_board.items():
            print(
            space + f'│ *{k}*{calc_space(k_rule, k)}│  {v}{calc_space(v_rule, str(v))}│'
            )
        print(space + '└────────────────────────────┘')