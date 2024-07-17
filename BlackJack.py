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

def deal_cards():
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        random_cards = random.choice(cards)
        return random_cards
#calculate the score
def calc_score(card_list):
    #优化当多个十一出现的时候，如何把所有十一都变成一
    if sum(card_list) > 21:
        if 11 in card_list:
            card_list.remove(11)
            card_list.append(1)           
    #要判断在刚开始发两张牌的时候21点就blackjack
    #其他情况回传本来的牌
    
    return card_list

res = calc_score([9,11,9])
print(res)
# start_game = input("Do you want to play a game of BlackJack? Type'y' or 'n':\n")
# if start_game == "n":
#     print("Bye")
# elif start_game == "y":
    
    
    
#     #random player's start cards
#     player_start_cards1 = deal_cards()
#     player_start_cards2 = deal_cards()
#     player_current_score = player_start_cards1 + player_start_cards2
#     print(f"Your card: {player_start_cards1}, {player_start_cards2}. current score: {player_current_score}")

#     #random computer's start cards
#     com_start_cards1 = deal_cards()
#     com_start_cards2 = deal_cards()
#     com_current_score = com_start_cards1 + com_start_cards2
#     print(f"Computer's first card: {com_start_cards1}.")

#     def determine_cards():
    
#         if  com_current_score == player_current_score :
#             print("draw")
#         elif player_current_score == 21:
#             print("BlackJack, you win")
#         elif com_current_score == 21:
#             print("Computer gets BlackJack, you lose")
#         elif player_current_score > 21:
#             if com_start_cards1 == 11 or com_start_cards2 == 11:
#                 cards[0] = 1
#                 if player_current_score > 21:
#                     print("you lose")
#                 else:
#                     pass
#             else:
#                 print("you lose")
#         else:
#             add_card = input("do you want to add card enter 'y'or'n'")
#             if add_card == "y":
#                 player_card3 = random.choice(cards)
#                 player_current_score += player_card3
#                 print(f"your score is {player_current_score}")
#             elif add_card == "n":


            

    
 









