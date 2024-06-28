# one input function
def great_to(name):#name is argument(xingshicanshu)
    print(f"Hello {name}!")
great_to("jack")#'jack' is parameter(shijicanshu)

# mutuple positional argument
def great_to(name,location):
    print(f"hello {name}!")
    print(f"you are from {location}")
great_to("jack","victoria")

# multiple key arguments
great_to(location="vancouver", name="ben")

import math

height = int(input("please enter the height of the wall:\n"))
width = int(input("please enter the width of the wall:\n"))
def area(height,width):
    can = (height * width)/5
    print(type(can))
    print(f"you need {math.ceil(can)} can.")
area(height,width)







