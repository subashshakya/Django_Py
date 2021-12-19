# assignment 2

from itertools import count

accounts = {}


class Account:
    count = count(start=1)

    def __init__(self, name, balance, pin):
        ac_n = next(self.count)
        self.ac_n = ac_n
        self.name = name
        self.balance = balance
        self.pin = pin
        accounts[ac_n] = self
        print(f"Account is created for {self.name}. Account number is: {self.ac_n}")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            print("The pin you have entered is invalid")

    def check_balance(self):
        print(f"The balance of your account is: {self.balance}")

    def __str__(self):
        return f"Account Number: {self.ac_n}. Account holder's name: {self.name}"

    def transfer(self, receiver, pin, amount):
        print(self)
        if self.pin == pin:
            if receiver.name != self.name:
                if amount < self.balance:
                    my_amount = self.balance - amount
                    self.balance = my_amount
                    receiver_balance = receiver.balance + amount
                    receiver.balance = receiver_balance
                    receiver.check_balance()
                    self.check_balance()
                else:
                    print("The passed amount is out of bounds")
            else:
                print("You cant transfer amount to yourself!!")
        else:
            print('The entered pin is invalid')


my_acc = Account(name='Subash', balance=100000, pin=1234)

not_my_acc = Account(name='Nishla', balance=100000, pin=5678)

my_acc.transfer(receiver=my_acc, pin=1234, amount=10000)

# output:
# Account is created for Subash. Account number is: 1
# Account is created for Nishla. Account number is: 2
# Account Number: 1. Account holder's name: Subash
# You cant transfer amount to yourself!!

