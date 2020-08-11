import util

def _player_pick():
    while True:
        pick = input("Pick heads or tails. ").lower()
        if pick == "heads" or pick == "tails":
            break
        else:
            print("ERROR: You must type either 'heads' or 'tails'")
    return pick

def _player_chooses_service():
    first_server = ""
    while not first_server:
        decision = input("Do you want to serve or receive? ").lower()
        if decision == "serve":
            first_server = "player"           
        elif decision == "receive":           
            first_server = "computer"
        else:
            print("ERROR: You must type either 'serve' or 'receive'")
    return first_server


def _computer_chooses_service():
    toss_result = util.coin_toss()
    if toss_result == "heads":
        computer_choice = "serve"
        first_server = "computer"
    else:
        computer_choice = "return"
        first_server = "player"
    print(f"Your opponent has chosen to {computer_choice}.")
    return first_server

def determine_first_server():
    pick = _player_pick()
    toss = util.coin_toss()
    print("And the result of the toss is...\n")

    if toss == pick:
        print(f"{toss.title()}! :)")
        first_server = _player_chooses_service()
    else:
        print(f"{toss.title()}. :(")
        first_server = _computer_chooses_service()
    return first_server
