fruits = ["Apple", "Cherry", "Pear"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
#For Calling
print("-------------------------------")
for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
print(fruits)


print("-------------------------------")
#range(a,b) b os not included
for number in range(1,10):
    print(number)

print("-------------------------------")
#range(a,b,step) b os not included
for number in range(1,10,3):
    print(number)

print("-------------------------------")
sum = 0
for num in range(1,101):
    sum = sum + num
print(sum)
