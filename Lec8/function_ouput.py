def calculate():
    return 3*2 #result of 3*2 save back to the function "calculate()"

result = calculate()#varible 接住return回去的结果

print(result)#打印出来

#--------------------------------------------
# function with single return
def add_number(a,b):
    #this function takes tow numbers and return their sum."
    return a + b

#define the number to be added
number1 = 5
number2 = 7

#call the function and store the result
result = add_number(number1 , number2)

#print the result
print("the sum of", number1 , "and" , number2 , "is" , result)


#--------------------------------------------
# function with motiple unpacked return
def sum_and_product(a, b): 
    """This function takes two numbers and returns their sum and product.""" 
    sum_result = a + b 
    product_result = a * b 
    return sum_result, product_result 

# Define the numbers to be used 
number1 = 5 
number2 = 7 

# Call the function and store the results 
sum_res, product_res = sum_and_product(number1, number2) 

# Print the results
print("The sum of", number1, "and", number2, "is", sum_res) 
print("The product of", number1, "and", number2, "is", product_res)


#------------------------------------------
# function with motiple packed return

def sum_and_product(a, b): 
    """This function takes two numbers and returns their sum and product.""" 
    sum_result = a + b 
    product_result = a * b 
    return sum_result, product_result 
# Example usage 

number1 = 5 
number2 = 7 
# Using a single variable to hold the returned tuple 

res = sum_and_product(number1, number2) 
# Accessing the elements of the tuple 

sum_result = res[0] 
product_result = res[1] 
# Print the results 

print("The sum of", number1, "and", number2, "is", sum_result) 
# Outputs 12 

print("The product of", number1, "and", number2, "is", product_result) 
# Outputs 35