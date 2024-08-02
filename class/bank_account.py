class BankAccount:
    def __init__(self):
        self.num_of_money = 0
    
    # 存钱
    def deposit(self):
        pass
    
    # 取钱
    def withdraw(self):
        pass
        
    # 检查余额
    def check_balance(self):
        return self.num_of_money
    
    # 转账给指定账户
    def transfer(self):
        pass
    
Michael_account = BankAccount()
Michael_account.num_of_money
print(Michael_account.check_balance())

Michael_account.deposit(50)
# Micheal_account.withdraw(???)


Alex_account = BankAccount()
Alex_account.num_of_money

# Micheal_account.transfer(xxxxx>?????)
# Micheal_account.check_balance()
# Alex_account.check_balance()