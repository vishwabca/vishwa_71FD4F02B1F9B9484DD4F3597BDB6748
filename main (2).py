class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ₹{amount}. New balance: ₹{self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def get_balance(self):
        return f"Current balance for {self.owner}: ₹{self.balance}"
if __name__== "__main__":
    account = BankAccount("vishwa", 1000.0)
    print(account.get_balance())
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.withdraw(1500))