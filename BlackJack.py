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
    if sum(card_list) == 21 and len(card_list) == 2:
        return sum(card_list)
    if sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)    
    return sum(card_list)
    #要判断在刚开始发两张牌的时候21点就blackjack
    #其他情况回传本来的牌

player_card_list = [deal_cards(),deal_cards()]
sum_of_player_score = sum(player_card_list)
comp_card_list = [deal_cards(),deal_cards()]
sum_of_comp_score = sum(comp_card_list)
print(player_card_list)
print(comp_card_list)

def compare(sum_of_player_score,sum_of_comp_score):
    #如果两个都超过21，都输
    #如果平局
    #判断电脑是不是bj
    #判断玩家是不是bj
    #判断玩家自己超过21，玩家输
    #判断电脑。。。。。
    #判断玩家超过电脑，玩家赢
    #else玩家输
    if sum_of_player_score > 21 and sum_of_comp_score > 21:
         print("you lose")
    elif sum_of_player_score == sum_of_comp_score:
         print("draw")
    elif sum_of_player_score > 21:
         print("you lose")
    elif sum_of_comp_score > 21:
         print("you win")
    elif sum_of_comp_score == 21:
         print("you lose")
    elif sum_of_player_score == 21:
         print("BlackJack")
    elif sum_of_player_score > sum_of_comp_score:
         print("you win")
    else:
         print("you lose")

game_running = True

while game_running:
    print(f"your cards:{player_card_list}, current score:{calc_score(player_card_list)}")
    print(f"computer's first card: {player_card_list[0]}")
    if sum_of_player_score == 21 or sum_of_comp_score == 21 or calc_score(player_card_list) > 21:
        game_running =False
    else:
        user_add_card = input("Type'y' to get another card,type 'n' to pass:")
        if user_add_card == "n":
            game_running  = False
        else:
            player_card_list.append(deal_cards())
            
while sum_of_comp_score != 21 and sum_of_comp_score < 17:
     comp_card_list.append(deal_cards())
print(f"computer's final hand:{}")
     
             
         



compare(sum_of_player_score , sum_of_comp_score)


            

    
 









