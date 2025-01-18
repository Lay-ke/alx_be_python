class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            return False
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0 or amount > self.balance:
            return False
        self.balance -= amount
        return self.balance

    def display_balance(self):
        return self.balance