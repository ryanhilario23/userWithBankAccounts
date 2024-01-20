class BankAccount:
    def __init__(self, checkings,savings,checkingID, savingID):
        self.checkings = checkings
        self.savings = savings
        self.checkingID = checkingID
        self.savingID = savingID
    #Display account 
    def display_account_info(self):
        print(f"Current Balance: ${self.checkings}\nCurrent Savings: ${self.savings}")
        return self
    
#Make a deposit
    def make_deposit(self, key, amount):
    #checking if the selected account is Checking or Savings
        if key == self.checkingID:
            self.checkings += amount
            print(f'Deposit Sucessful: ${amount}\nNew Balance: ${self.checkings}')
        elif key == self.savingID:
            self.savings += amount
            print(f'Deposit Sucessful: ${amount}\nNew Balance: ${self.savings}')
    #THe account does not match to the user's accounts
        else:
            print("error: Account not owned")
        return self
#Make a withdraw
    def make_withdraw(self, key, amount):
        if key == self.checkingID:
            self.checkings -= amount
            print(f'Withdraw Sucessful: ${amount}\nNew Balance: ${self.checkings}')
        elif key == self.savingID:
            self.savings -= amount
            print(f'Withdraw Sucessful: ${amount}\nNew Balance: ${self.savings}')
        else:
            print("error: Account not owned")
        return self

class User:
    def __init__(self, name, email,checkingID, savingID,checkings, savings,):
        self.name = name
        self.email = email
        self.account = BankAccount(checkings, savings,checkingID, savingID )

    def displaying(self):
        self.account.display_account_info()
        return self
    def depositing(self,key,amount):
        self.account.make_deposit(key,amount)
        return self
    def withdrawing(self,key,amount):
        self.account.make_withdraw(key,amount)
        return


GoGo = User("Gogo", 'Gogo@BH6.org',4012, 1009, 20, 100)
Fred = User("Fred", 'Fredmister@BH6.org', 1037, 14123, 1000, 200000)

# GoGo.manaic()
print("----------")
# GoGo.account.make_deposit(1009,100).make_deposit(1009,100)
GoGo.depositing(4012,100).withdrawing(4012,200)
print("----------")
# Fred.account.display_account_info().make_withdraw(14123,10000) 
