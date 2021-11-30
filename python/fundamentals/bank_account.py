"""
Not sure exactly what the ninja bonus was referring to. I think it was referring to
storing all instances in a single class variable list.
"""
class BankAccount:
    all_accounts = []

    def __init__(self, int_rate=0.01, balance=0.00):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def Deposit(self, amount):
        self.balance += amount
        return self

    def Withdraw(self, amount):
        self.balance -= amount
        return self

    def YieldInterest(self):
        self.balance = self.balance * (1.0 + self.int_rate)

    def DisplayAccountInfo(self):
        print(self)

    @classmethod
    def PrintAllAccounts(cls):
        for account in cls.all_accounts:
            print(account)

    def __str__(self) -> str:
        return (f"int_rate: {(self.int_rate * 100.0):.0f}%\n"
                f"balance:  ${self.balance:.2f}")
    
    def __repr__(self) -> str:
        return str(self)

if __name__ == "__main__":
    a1 = BankAccount(0.05, 10000)
    a2 = BankAccount(0.05, 10000)
    BankAccount.PrintAllAccounts()

    a1.Deposit(200).Deposit(200).Deposit(200).Withdraw(500).YieldInterest()
    a2.Deposit(100).Deposit(100).Withdraw(500).Withdraw(500).Withdraw(500).Withdraw(500).YieldInterest()
    BankAccount.PrintAllAccounts()