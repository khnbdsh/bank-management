class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
            if amount <= self.balance:
                 self.balance = self.balance - amount
                 print("Withdrawal successfull")
            else:
                 print("insufficient balance")     


account1 = BankAccount("Sohail", 5000)
print(account1.name)
print(account1.balance)

account2 = BankAccount("Ahmed", 3000)
print(account2.name)
print(account2.balance)

account1.deposit(2000)
print(account1.balance)

account1.withdraw(1000)
print(account1.balance)
