import colorama
from colorama import Fore
colorama.init()


dice_art = {
    1: (
        '┌─────────┐',
        '│         │',
        '│    ●    │',
        '│         │',
        '└─────────┘'
        ),
    2: (
        '┌─────────┐',
        '│  ●      │',
        '│         │',
        '│      ●  │',
        '└─────────┘'
        ),
    3: (
        '┌─────────┐',
        '│ ●       │',
        '│    ●    │',
        '│       ● │',
        '└─────────┘'
        ),
    4: (
        '┌─────────┐',
        '│  ●   ●  │',
        '│         │',
        '│  ●   ●  │',
        '└─────────┘'
        ),
    5: (
        '┌─────────┐',
        '│ ●     ● │',
        '│    ●    │',
        '│ ●     ● │',
        '└─────────┘'
        ),
    6: (
        '┌─────────┐',
        '│  ●   ●  │',
        '│  ●   ●  │',
        '│  ●   ●  │',
        '└─────────┘'
        )
    }


def print_hand(hand):
    for i in range(6):
        for die in hand:
            print(Fore.YELLOW + dice_art[die][i], end=Fore.RESET+'   ')
        print(' ')
    print(Fore.RESET)

