import random
import sys
import time

import match
import rally
import util

def score():
    pass
    
def ask_play_game(prompt):
    response = input(prompt).lower()
    if response in ["no", "n", "no thanks", "no thank you"]:
        print("Ok! Next time!")
        keep_playing = False
    else:
        print("Great! Game on!")
        keep_playing = True
    return keep_playing

# Assign numbers to moves and roll die? (functions?)

# Make a loop that plays a point by continuesly rolling die

# NOTE TO SELF: make a recieve function

# NOTE TO SELF: make a service game function that calls the serve functions

# NOTE TO SELF: make function that generates HOW MANY shots there are in a point
# NOTE TO SELF: make a function that generates the outcome of the point
# - Like serve function

if __name__ == '__main__':
    keep_playing = ask_play_game("Do you want to play tennis? ")
    
        
    while keep_playing:
        first_server = match.determine_first_server()
        if first_server == "player":
            serve = rally.serve()
        else:
            serve = rally.receive()
        
        if serve == "server wins point":
            print("You won the point! 15 - 0")
        elif serve == "returner wins point":
            print("You lost the point! 0 - 15")
        else:
            in_play = True
            while in_play:
                rally.select_shot()
                swing_result = util.swing()
                if swing_result == "critical success":
                    print("Yay! You hit a winner!")
                    in_play = False
                elif swing_result == "success":
                    print("You made your shot!")
                    # NEW BALL STATUS!!!! (opponent has to return) #
                elif swing_result == "critical failure":
                    print("You fell on your face and accidentally hit your ball into the crowd!")
                    in_play = False
                else:
                    print("You missed your shot :(")
                    in_play = False
        keep_playing = ask_play_game("Play again? ")

        
    # End of "while" loop
    print("Good match! To play another, restart the program!")
    print("I hope to play you again!")

# NOTE TO SELF: USE 100 SCALE NOT 10 SCALE (done)
# NOTE TO SELF: ADD HEADS/TAILS FOR SERVE (in process)
# NOTE TO SELF: MAKE PROSET/SET/MATCH OPTION?
# NOTE TO SELF: MAKE EXPERIANCE POINTS? EXAMPLE: HIGHER EXPERIENCE MEANS MORE ACES AND FEWER FOOT FAULTS
# IDEA: XP POINTS- GIVE OPTION FOR DIF. SERVES WHEN HIGHER XP?

# IDEA: MAKE A DICTIONARY OF TENNIS TERMS FOR PLAYER TO ACCESS IN BETWEEN GAMES? (EX: LET, 15-LOVE?)
