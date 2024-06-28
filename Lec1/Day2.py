# If else
# water_level = 5
# if water_level > 10:
#     print("water_level is high")
# else:
#     print("NEED WATER!")

#comparator: > , < , >= , <= , == , != 

height = int(input("What's ur height?(cm)\n"))
if height >= 120:
    age = int(input("What's ur age?\n"))
    print("u can ride the rollercoaster.")
    if age < 18:
        print("Please pay 5 dollars")
    elif 12 < age <= 18:
        print("Please pay 7 dollars")
    else:
        print("Please pay 12 dollars")
    
    print("After riding the roller coaster")
    yes = (input("Do you want to buy photos of yourself (Y or N)?\n"))
    if yes == 'Y' or 'y' or 'yes' or 'Yes':
        print("Please pay 3 more dollars for photos.")
        if age < 18:
            print("You need to pay a total of 8 dollars")
        elif 12 < age <= 18:
            print("You need to pay a total of 10 dollars")
        elif age > 18:
            print("You need to pay a total of 15 dollars")
    else:
        print("ok, bye")
else:
    print("Sorry, u have to grow tallar before u can ride.")
    






