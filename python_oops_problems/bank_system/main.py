class Account:
    bank_name = "Python National Bank"
    total_accounts = 0

    def __init__(self, account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        Account.total_accounts += 1
    
    def deposit(self, amount):
        if Account.validate_amount(amount):
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if not Account.validate_amount(amount):
            print("Invalid withdrawal amount")
        elif amount > self.balance + self.overdraft_limit:
            print("Exceeded overdraft limit")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def transfer(self, target_account, amount):
        if amount > self.balance:
            print("Insufficient funds for transfer")
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred {amount} to account {target_account.account_number}")

    def __str__(self):
        return (f"Account Holder : {self.holder_name}\n"
                  f"Account Number : {self.account_number}\n"
                  f"Balance        : {self.balance}"
                  f"\nBank Name      : {Account.bank_name}")
    
    def __repr__(self):
        return f"Account({self.account_number}, {self.holder_name}, {self.balance})"
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

class SavingsAccount(Account):
    def __init__(self, account_number,holder_name,balance,interest_rate):
        super().__init__(account_number,holder_name,balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Applied interest: {interest}. New balance: {self.balance}")

class CurrentAccount(Account):
        def __init__(self, account_number,holder_name,balance,overdraft_limit):
            super().__init__(account_number,holder_name,balance)
            self.overdraft_limit = overdraft_limit
        
        def withdraw(self, amount):
            if amount > self.balance + self.overdraft_limit:
                print("Exceeded overdraft limit")
            else:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
    

acc1 = SavingsAccount(1001, "Krishna", 50000, 5)
acc2 = CurrentAccount(1002, "Janvi", 10000, 20000)

acc1.deposit(5000)
acc1.withdraw(2000)

acc1.transfer(acc2, 10000)

acc1.apply_interest()

acc2.withdraw(25000)

print(acc1)
print(acc2)   















#FIRST STAGE OF TESTING ON THIS CLASS LOL 💀💀

# acc1 = Account("123456", "Krish", 100000)
# acc2 = Account("654321", "Janvi", 5000000)

# print(acc1.account_number)  # Output: 123456
# print(acc1.holder_name)     # Output: Krish
# print(acc1.balance)         # Output: 100000
# print(acc2.account_number)  # Output: 654321
# print(acc2.holder_name)     # Output: Janvi
# print(acc2.balance)         # Output: 5000000

# acc1.transfer(acc2, 50000)  # Output: Transferred 50000 to account 654321

# print(acc1)
# print(acc2.__repr__())
# print(acc1.__repr__())