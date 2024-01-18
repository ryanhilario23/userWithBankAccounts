class BankAccount:
    def __init__(self, checkings,savings,checkingID, savingID):
        self.checkings = checkings
        self.savings = savings
        self.checkingID = checkingID
        self.savingID = savingID
    #Display account 
    def display_account_info(cls):
        print(f"Current Balance: ${cls.checkings}\nCurrent Savings: ${cls.savings}")
        return cls
#Make a deposit
    def make_deposit(cls, key, amount):
    #checking if the selected account is Checking or Savings
        if key == cls.checkingID:
            cls.checkings += amount
            print(f'Deposit Sucessful: ${amount}\nNew Balance: ${cls.checkings}')
        elif key == cls.savingID:
            cls.savings += amount
            print(f'Deposit Sucessful: ${amount}\nNew Balance: ${cls.savings}')
    #THe account does not match to the user's accounts
        else:
            print("error: Account not owned")
        return cls
#Make a withdraw
    def make_withdraw(cls, key, amount):
        if key == cls.checkingID:
            cls.checkings -= amount
            print(f'Withdraw Sucessful: ${amount}\nNew Balance: ${cls.checkings}')
        elif key == cls.savingID:
            cls.savings -= amount
            print(f'Withdraw Sucessful: ${amount}\nNew Balance: ${cls.savings}')
        else:
            print("error: Account not owned")
        return cls

class User:
    def __init__(self, name, email,checkingID, savingID,checkings, savings,):
        self.name = name
        self.email = email
        self.account = BankAccount(checkings, savings,checkingID, savingID )


GoGo = User("Gogo", 'Gogo@BH6.org',4012, 1009, 20, 100)
Fred = User("Fred", 'Fredmister@BH6.org', 1037, 14123, 1000, 200000)

# GoGo.manaic()
print("----------")
GoGo.account.make_deposit(1009,100).make_deposit(1009,100)
print("----------")
Fred.account.display_account_info().make_deposit(14123,10000) 
