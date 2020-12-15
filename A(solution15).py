# 15 . Imagine you are designing a banking application.What would a customer look like?What attributes would she have?What methods would she have?
class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def dump(self):
        s = '%s, %s, balance: %s' % \
            (self.name, self.no, self.balance)
        print(s)

a1 = Account('shyam Poudel', '19371554951', 20000)
a2 = Account('Ram Chhetri', '19371554951', 45000)
a1.deposit(1000)
a1.withdraw(4000)
print("A1 balance is:", a1.balance)
a2.deposit(1000)
a2.withdraw(4000)
print("A2 balance is:", a2.balance)