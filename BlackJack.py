import random

def display_logo():
    """displays a simple logo for the game."""
    logo = """
    .------.            _     _            _    _            _
    |A_  _ |.          | |   | |          | |  (_)          | |
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |
          `------'                           |__/
    """
    print(logo)
display_logo()

start_game = input("Do you want to play a game of BlackJack? Type'y' or 'n':\n")
if start_game == "n":
    print("Bye")
elif start_game == "y":
    #random player's start cards
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_start_cards1 = random.choice(cards)
    player_start_cards2 = random.choice(cards)
    player_current_score = player_start_cards1 + player_start_cards2
    print(f"Your card: {player_start_cards1}, {player_start_cards2}. current score: {player_current_score}")

    #random computer's start cards
    com_start_cards1 = random.choice(cards)
    com_start_cards2 = random.choice(cards)
    com_current_score = com_start_cards1 + com_start_cards2
    print(f"Computer's first card: {com_start_cards1}.")

    if  com_current_score == player_current_score:
        print("draw")
    elif player_current_score == 21:
        print("BlackJack, you win")
    elif com_current_score == 21:
        print("Computer gets BlackJack, you lose")
    elif player_current_score >= 21:
        if com_start_cards1 == 11 or com_start_cards2 == 11:
            cards[0] = 1
        else:
            print("you lose")
    else:
        input()
            
    
    
 









