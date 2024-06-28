import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.")
sign_choice = int(input("choose your sign:\n"))
if sign_choice == 0 or sign_choice == 1 or sign_choice == 2:
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---._(___)
    '''

    paper = '''
        ______
    ---'   ___)___
            ______)
            _______)
           _______)
    ---._______)
    '''

    scissors = '''
        _______
    ---'   ____)___
             ______)
          __________)
         (____)
    ---._(___)
    '''
    sign = [rock , paper , scissors]
    print(sign[sign_choice])
    print("computer chose:")
    computer_choice = random.choice([0,1,2])
    print(sign[computer_choice])
    if sign_choice == computer_choice:
        print("It's a draw")
    elif (sign_choice == 0 and computer_choice == 2) or (sign_choice == 1 and computer_choice == 0) or (sign_choice == 2 and computer_choice == 1):
        print("you win")
    elif (sign_choice == 0 and computer_choice == 1) or (sign_choice == 1 and computer_choice == 2) or (sign_choice == 2 and computer_choice == 0):
        print("you lose")
else:
    print("Are you a fool? I ask you to enter 012 and you enter something else.")
    

