enemies = 1
def increase_enemies():
    enemies = 2
    test = 3
    print(f"enemies inside function:{enemies}")

increase_enemies()
print(f"enemies outside function:{enemies}")

#print(test)  域里面是local variable，外面无法打印
#--------------------------------------------------
#作用域叫scopy
#global scope
player_health = 10#global varible

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)

#------------------------------------------------------
enemies = 1

def increase_enemies():
    print(f"enemies inside function:{enemies}")
    return enemies + 1
    

increase_enemies()
print(f"enemies outside function:{enemies}")


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function:{enemies}")

increase_enemies()
print(f"enemies outside function:{enemies}")




