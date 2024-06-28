#random
import random

num1 = random.randint(1,10) #Can only take values within a given range
print(num1)

num2 = random.choice([1,3,7]) #Only the given number will be taken
print(num2)



random_int = random.randint(1,2)
if random_int == 1:
    print("head")
else:
    print("tail")


#create my own module
import my_module
name = my_module.my_name
print(name)