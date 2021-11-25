from modularizing.bank_account import BankAccount

class TestAccount:
    def __init__(self):
        self.balance = 500.00
    def Deposit(self, amount):
        self.balance += amount
    def __str__(self) -> str:
        return f"balance:  ${self.balance:.2f}"
    def __repr__(self) -> str:
        return str(self)

class User:
    def __init__(self, full_name, email) -> None:
        self.full_name = full_name
        self.email = email
        self.accounts = {"checking" : BankAccount(balance=5000)} 

    def __str__(self) -> str:
        return (f"{self.full_name}\n"
                f"{self.email}")

    def AddAccount(self, account_name, int_rate=None, balance=None):
        if account_name in self.accounts:
            print(f"Account {account_name} already exists.")
        else:
            self.accounts[account_name] = temp = BankAccount()
            if int_rate:
                temp.int_rate = int_rate
            if balance:
                temp.balance = balance

    def Deposit(self, amount, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name].Deposit(amount)
        else:
            print(f"Account '{account_name}' does not exist. Can't deposit.")

    def Withdraw(self, amount, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name].Withdraw(amount)
        else:
            print(f"Account '{account_name}' does not exist. Can't withdraw.")

    def YieldInterest(self, account_name):
        if account_name in self.accounts:
            return self.accounts[account_name].YieldInterest()
        else:
            print(f"Account '{account_name}' does not exist. Can't yield interest.")

    def YieldInterestAll(self):
        for key,account in self.accounts.items():
            account.YieldInterest()

    def DisplayAccountInfo(self, account_name):
        if account_name in self.accounts:
            print(f"{account_name}:")
            print(self.accounts[account_name])
        else:
            print(f"Account '{account_name}' does not exist. Can't display.")

    def DisplayAccountInfoAll(self):
        for key,account in self.accounts.items():
            print(f"{key.capitalize()} account:")
            print(account)


acc = [BankAccount(), TestAccount()]
for a in acc:
    a.Deposit(200)

print(acc)