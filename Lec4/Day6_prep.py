# Method1
#num = int(input("please enter a number between 1 to 999:\n"))
#sum = 0
#for num in range(2,num+1,2):
#    sum = sum + num
#print(sum)

# Method2
target = int(input())
even_sum = 0
for number in range(1, target+1):
    if number %2 == 0:
        even_sum = even_sum + number
print(even_sum)













