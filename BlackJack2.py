import random

def clear_console():
    """Clears the console for a new game."""
    print("\n")
    print("\n")

def display_logo():
    """Displays a simple logo for the game."""
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

def deal_card():
    """Returns a random card from the deck."""
    cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
   """Compare the user and computer scores and return the result."""
   if user_score > 21 and computer_score > 21:
       return " You went over, You lose"
   if user_score == computer_score:
       return "Draw🤣"
   elif computer_score == 0:
       return "Lose, computer has Blackjack😭"
   elif user_score == 0:
       return "Win with a Blackjack😎"
   elif user_score > 21:
       return "You went over, you lose😂"
   elif computer_score > 21:
       return "Computer went over, you win😆"
   elif user_score > computer_score:
       return "You win🤓"
   else:
       return "You lose🤣👌"
   
def play_game():
    display_logo()

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_cards}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass.")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards) 

    print(f"  Your final hand {user_cards}, final score {user_score}")
    print(f"  Your final hand {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))   

while input("Do you want to play a game of BlackJack? Type 'y' or 'n' ") == "y":
    clear_console()
    play_game()
       