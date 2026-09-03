class BankAccount:
    def __init__(self,name,balance):
        self.account_holder=name
        self.balance=balance
    def deposit(self,amount):
        self.balance =self.balance + amount
        print(f"deposited {amount} to your account")
    def withdraw(self,amount):
        if amount>self.balance:
            print("not enough balance !!")
        else:
            self.balance=self.balance - amount            
    def __str__(self):
        return f"Account Holder name: {self.account_holder} \nBalance: {self.balance}"    
obj=BankAccount("ramesh",1000)    
print(obj) 
obj.deposit(200)  
obj.withdraw(500)
print(obj)