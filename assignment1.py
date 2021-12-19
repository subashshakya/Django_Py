# OOP assignment django workshop

class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def eat(self):
        print("Eat")

    def walk(self):
        print("Walk")

    def run(self):
        print("Run")

    def display(self):
        print(f"Name: {self.name}, Address: {self.address}, Age: {self.age}")


class Male(Person):
    def __init__(self, name, address, age):
        Person.__init__(self, name, address, age)


class Female(Person):
    def __init__(self, name, address, age):
        Person.__init__(self, name, address, age)


Ram = Male(name='Ram', address='Kathmandu', age=25)
Ram.display()
print()

Sita = Female(name='Sita', address='Janakpur', age=25)
Sita.display()

# output:
# Name: Ram, Address: Kathmandu, Age: 25

# Name: Sita, Address: Janakpur, Age: 25
