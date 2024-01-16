class BankAccount:
    def __init__(self,int_rate, checkings,savings):
        self.int_rate = int_rate
        self.checkings = checkings
        self.savingings = savings

class User:
    def __init__(self, name, email,checking):
        self.name = name
        self.email = email
        self.checking = checking
        self.account = BankAccount(int_rate=0.02, checkings=100, savings=0 )
    
    # other methods
    def display_account_info(self):
        print(f"Current Balance: ${self.account.checkings}\nSavings:${self.account.savingings}")
        return self

    def make_deposit(self,account_num, amount):
        if account_num == self.checking:
            self.account.checkings += amount
            print(f'Deposit Sucessful: ${amount}\nNew Balance: ${self.account.checkings}')
        else:
            # self.account.savingings += amount
            # print(f'Deposit Sucessful: ${amount}\nNew Balance: ${self.account.savingings}')
            print("error: Account not owned")
        return self
    def make_withdrawal(self,amount):
        self.account.checkings -= amount
        print(f'Withdrawal Sucessful: {amount}\nNew Balance: ${self.account.checkings}')
        return self

GoGo = User("Gogo", 'Gogo@BH6.org',412)
GoGo.make_deposit(412,100).make_deposit('savings',50).display_account_info()