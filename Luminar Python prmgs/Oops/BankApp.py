import datetime

class Person:
    def setValue(self,name,age):
        self.name=name
        self.age=age

    def printValues(self):
        print(self.name)
        print(self.age)


class Bank(Person):

    bnk_name="SBI"

    def __init__(self,ac_no):
        self.ac_no =ac_no
        self.bal=3000

    def print_Acc_Values(self):
        print("Account Nummber:",self.ac_no)
        print("Bank Name:",Bank.bnk_name)
        print("Balance:",self.bal)


    def withdraw(self,amount):


        if(self.bal<amount):
            print("Insufficient Balance")
        else:
            self.bal -= amount
            print("your", Bank.bnk_name, " has been debited with ", amount, datetime.date.today(),
                  " your current balance is", self.bal)

    def deposit(self,amount):
        self.bal+=amount
        print("your" ,Bank.bnk_name, " has been credited with ",amount ,datetime.date.today()," your current balance is", self.bal)

    def balanceEnquiry(self):
        print("your current balance :", self.bal)


obj=Bank(100)
obj.setValue("Akshay",22)
obj.printValues()
obj.print_Acc_Values()
obj.deposit(5000)
obj.withdraw(2000)
obj.balanceEnquiry()



