class BankAccount():
    def __init__(self,my_name):
        self.balance = 0
        self.name = my_name
    
Alex_account = BankAccount("Alex")
print(Alex_account.balance)
print(Alex_account.name)
m_account = BankAccount("Michael")
print(m_account.balance)
print(m_account.name)