# itertools

from itertools import count

accounts = {}  # this dictionary acts as a database


class Account:

    count = count(start=1) # count is a function from count

    def __init__(self, name, balance, pin):
        ac_n = next(self.count)
        self.ac_n = ac_n
        self.name = name
        self.balance = balance
        self.pin = pin
        accounts[ac_n] = self
        print(f"Congrats {name} you have sucessfully created a bank account. Your Current balance is: {balance} and your account number is: {ac_n}")

    def change_pin(self, old_pin, new_pin): # for changing pin
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            print("The pin you have entered is invalid")

    def __str__(self): # sting representation
        return f"Account number: {self.ac_n}. Name: {self.name}."

    def check_balance(self): # balance check of object
        print(f"The balance of {self.name} is: {self.balance}")

    def transfer(self, receiver, pin, amount):
        print(self)
        if self.pin == pin: # checks pin of sender
            if amount < self.balance:  # checks if the amount is not transferable or not
                my_amount = self.balance - amount  # decreasing amount of sender
                self.balance = my_amount  # assigning value for sender balance
                receiver_balance = receiver.balance + amount  # increases balance of receiver
                receiver.balance = receiver_balance  # assigns new value to receiver balance
                receiver.check_balance()
                self.check_balance()
            else:
                print("The passed amount is out of bounds")
        else:
            print('The entered pin is invalid')



my_acc = Account(name='Subash', balance=100000, pin=1234)

not_my_acc = Account(name='Nishla', balance=100000, pin=5678)

my_acc.transfer(receiver=not_my_acc, pin=1234, amount=10000)

# output:
# Congrats Subash you have sucessfully created a bank account. Your Current balance is: 100000 and your account number is: 1
# Congrats Nishla you have sucessfully created a bank account. Your Current balance is: 100000 and your account number is: 2
# Account number: 1. Name: Subash.
# The balance of Nishla is: 110000
# The balance of Subash is: 90000
