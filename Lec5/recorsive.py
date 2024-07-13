def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(5)
print(result)

#一定要设定停止节点