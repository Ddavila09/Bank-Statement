class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

        BankAccount.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
            
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.int_rate}")
        return self
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


bankAccount1 = BankAccount(0.05, 5000)
bankAccount2 = BankAccount(0.10, 20000)


bankAccount1.display_account_info()
bankAccount1.deposit(2000).deposit(6000).deposit(3000).withdraw(10250).yield_interest()

bankAccount2.display_account_info()
bankAccount2.deposit(2000).deposit(6000).withdraw(3000).withdraw(10250).yield_interest()

BankAccount.all_accounts()


