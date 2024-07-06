def calculator(a,b):
    sum_result = a+b
    sub_result = a-b
    mut_result = a*b
    div_result = a/b
    return sum_result,sub_result,mut_result,div_result

num1_enter = int(input("enter the first number:"))
num2_enter = int(input("enter the second number:"))
oprator = input("你想用什么计算方法呢(+,-,*,/):")

res = calculator(num1_enter,num2_enter)

sum_result = res[0]
sub_result = res[1]
mut_result = res[2]
div_result = res[3]

if oprator == "+":
    print(sum_result)
elif oprator == "-":
    print(sub_result)
elif oprator == "*":
    print(mut_result)
elif oprator == "/":
    print(div_result)
else:
    print("please enter the right oprator")


