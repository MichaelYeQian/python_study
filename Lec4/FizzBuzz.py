target = int(input("please enter a positive integer:\n"))
for number in range(1,target+1): 
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

