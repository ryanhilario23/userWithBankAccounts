class BankAccount:
    def __init__(self,int_rate, checkings,savings):
        self.int_rate = int_rate
        self.checkings = checkings
        self.savings = savings

class User:
    def __init__(self, name, email,checking, savings):
        self.name = name
        self.email = email
        self.checking = checking
        self.savings = savings
        self.account = BankAccount(int_rate=0.02, checkings=100, savings=0 )
#Display account 
    def display_account_info(self):
        print(f"Current Balance: ${self.account.checkings}\nCurrent Savings:${self.account.savings}")
        return self

#Make a deposit
    def make_deposit(self,account_num, amount):
    #checking if the selected account is Checking or Savings
        if account_num == self.checking:
            self.account.checkings += amount
            print(f'Deposit Sucessful: ${amount}\nNew Balance: ${self.account.checkings}')
        elif account_num == self.savings:
            self.account.savings += amount
            print(f'Deposit Sucessful: ${amount}\nNew Balance: ${self.account.checkings}')
    #THe account does not match to the user's accounts
        else:
            print("error: Account not owned")
        return self

#Make a make_withdrawal
    def make_withdrawal(self,account_num,amount):
        if account_num == self.checking:
            self.account.checkings -= amount
            print(f'Withdrawl Sucessful: ${amount}\nNew Balance: ${self.account.checkings}')
        elif account_num == self.savings:
            self.account.savings -= amount
            print(f'Withdrawl Sucessful: ${amount}\nNew Balance: ${self.account.checkings}')
        else:
            print("error: Account not owned")
        return self

GoGo = User("Gogo", 'Gogo@BH6.org',4012, 1009)
Fred = User("Fred", 'Fredmister@BH6.org', 1037, 14123)

print("Gogo's Account")
GoGo.display_account_info().make_deposit(4012,100).make_deposit(1009,50).display_account_info()
print("----------")
print("Fred's Account")
Fred.display_account_info().make_deposit(1037,2000).make_deposit(14123,5000).display_account_info()