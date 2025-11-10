#Challenge: Banking System
# Using multilevel inheritance, design a banking system with a savings and premium savings account



class Account:
    def __init__(self,account_name, account_number, account_balance):
        self.name = account_name
        self.account_no = account_number
        self.balance = account_balance
        self.fee = 10.50

    def account_info(self):
        print(f"Account name: {self.name} | Account number: {self.account_no} | Account Balance: ${self.balance}")

    def deposit(self,amount):
        self.balance = (amount + self.balance) - self.fee
        print(f"${amount} Deposited, Your new balance is ${self.balance}. Txn fee: ${self.fee}")
        return(self.balance)
    
    def withdraw(self,amount):
        if amount > self.balance or (self.balance - (amount + self.fee) < 0):
            print(f"Insufficient Balance, Your current balance is ${self.balance}")
        else:
            self.balance = self.balance - (amount + self.fee)
            print(f"Withdrawal Successful! ${amount} withdrawn. Your new balance is {self.balance}. Txn fee: {self.fee}")
            return(self.balance)


class Savings(Account):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.interest = interest_rate

    def add_interest(self):
       self.balance = self.balance + (self.balance * self.interest/100)
       print(f"Your interest have been added for this month, your new balance is {self.balance}")
       return self.balance
    

class PremiumSavingsAccount(Savings):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance, interest_rate)
        self.cashback = 0.1
        self.fee = 5.0
    

    def deposit(self,amount):
        self.balance += (amount - self.fee) + (amount * self.cashback)
        print(f"${amount} Deposited, Your new balance is ${self.balance}. Txn fee: ${self.fee}. Cashback 10%")
        return(self.balance)
    
    def withdraw(self,amount):
        super().withdraw(amount)

#user = Savings("John Doe", "123456789", 30000, 15)
#user.account_info()

#user.deposit(25000)
#user.withdraw(30000)
#user.add_interest()

#user.account_info()



#user1 = PremiumSavingsAccount("Doe John", 234567891, 30000, 10 )

#user1.account_info()
#user1.deposit(25000)
#user1.withdraw(30000)
#user1.account_info()
