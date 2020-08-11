import random

def coin_toss():
    return random.choice(["heads", "tails"])

def roll_die(sides = 20):
    return random.randint(1, sides)

def swing():
    difficulty = 10

    roll = roll_die()
    if roll == 20:
        result = "critical success"
    elif roll == 1:
        result = "critical failure"
    elif roll >= difficulty:
        result = "success"
    else:
        result = "failure"
    return result
