import random
import time

import util

def serve():
    serve_modifier = 0
    result = ""
    while not result:
        first_serve = random.randint(1, 100)
        if first_serve <= (5 - serve_modifier):
            print("Yay! You hit an ace!")
            result = "server wins point"
        elif first_serve <= (10 - serve_modifier):
            print("Oh no! You foot faulted. :(")
            if serve_modifier != 0:
                result = "returner wins point"
        elif first_serve <= 60:
            print("Great! You made your serve!")
            result = "continue point"
        elif first_serve <= (90 + serve_modifier):
            print("You missed your serve. :(")
            if serve_modifier != 0:
                result = "returner wins point"
            serve_modifier = 5
        elif first_serve > 90:
            print("The serve hit the net and went in! Serve again.")
        else:
            print("Oops! Something went wrong :(")

    return result

def receive():
    receive_modifier = 0
    returner_game_score = 0
    server_game_score = 0
    result = ""
    while not result:
        first_serve = random.randint(1, 100)
        if first_serve <= (5 - receive_modifier):
            print("Oof! Your opponent hit an ace!")
            result = "server wins point"            
        elif first_serve <= (10 - receive_modifier):
            print("Your opponent foot faulted.")
            if receive_modifier != 0:
                result = "returner wins point"
        elif first_serve <= 60:
            print("Your opponent made their serve. The ball is now in play.")
            result = "continue point"
        elif first_serve <= (90 + receive_modifier):
            print("Your opponent missed their serve.")
            if receive_modifier != 0:
                result = "returner wins point"
            receive_modifier = 5
        elif first_serve > 90:
            print("The serve hit the net and went in! Your opponent has to re-serve.")
        else:
            print("Oops! Something went wrong :(")

    return result

def get_shot(shot_type, choices):
    while True:
        try:
            print("How do you want to hit your shot?")
            i = 1
            for option in choices:
                print(f"Press {i} for {option}")
                i += 1
            choice = int(input(f"Choose your {shot_type}: "))
            if choice in range(1, len(choices) + 1):
                return choices[choice - 1]
            else:
                print("\nERROR: Please type a numbered option.\n")
                time.sleep(1)
        except ValueError:
           print("\nERROR: Please type a numbered option.\n")
           time.sleep(1)

def select_shot():
    last_shot = "playable serve"
    ball_status = ""
    winner_is = ""
    while not winner_is:
        print(f"The ball is a {last_shot}.")

        print("Choose how to return the ball:")
        stroke = get_shot("stroke", ["forehand", "backhand"])
        side = get_shot("side", ["crosscourt", "down-the-line"])
        depth = get_shot("depth", ["deep", "short"])
        force = get_shot("force", ["offensive", "defensive", "neutral"])
        ball_status = f"{force} {depth} {side} {stroke}"
        print(f"Ok! You are countering your opponent's {last_shot} with a {ball_status}.")

        if util.roll_die() > 10:
            winner_is = "someone"
            print(f"AND THE WINNER IS... \n{winner_is}!")

