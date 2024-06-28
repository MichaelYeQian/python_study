#List
#Syntax yu3fa3ge2shi4
#name_list = [item1,item2,......]
fruits = ["mango" , "orange" , "peach"] #creating list
print(fruits[0]) #calling
print(fruits[-1])#-1 is a special index to print last item.
fruits[0] = "apple" #modify xiu1gai3
print(fruits[0])
fruits.append("mango")#add
print(fruits[-1])
print(fruits) #print all
fruits.pop(0) #delete
print(fruits)
fruits.pop()
print(fruits)

vagetable = ["potato" , "tomato" ,"cabbage"]
food = [fruits , vagetable]
print(food)
print(food[1][1])