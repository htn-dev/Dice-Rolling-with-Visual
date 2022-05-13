# dice.py
import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.

    If so, return an integer with the same value. Otherwise, tell

    the user to enter a valid number and quit the program.

    """
    if input_string.strip() in {"1","2","3","4","5","6"}:
        return int(input_string)
    else:
        print("Please enter a valid number 1-6: ")
        raise SystemExit(1)

def roll_dice(num_dice):
    """ Return a list of integers with length `num_dice`.
    
    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,6)
        roll_results.append(roll)
    return roll_results

def generate_dice_faces_doagram(dice_values):
    """Return an ASCII diagram of dice faces from `dice_values`.
    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:


    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~

    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐

    │  ●   ●  │ │         │ │  ●      │ │  ●      │

    │         │ │    ●    │ │    ●    │ │         │

    │  ●   ●  │ │         │ │      ●  │ │      ●  │

    └─────────┘ └─────────┘ └─────────┘ └─────────┘

    """
# ~~~ App's main code block ~~~

# 1. Get and Validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)

# 2. Roll the dice
roll_results = roll_dice(num_dice)
print(roll_results)    # Remove this line after testing the app
