from Tools.scripts.gprof2html import add_escapes
#Dunder methods - magic methods double underscore

class Money:
    def __init__(self, amount=0):
        self.amount = amount
    def __str__(self):
        return f'money: {self.amount}'
    def __add__(self, other):
        return Money(self.amount + other.amount)
    def __sub__(self, other):
        return Money(self.amount - other.amount)
    def __mul__(self, other):
        return Money(self.amount * other.amount)
    def __eq__(self, other):
        return Money(self.amount == other.amount)
    #gt - greater than - self > other
    #ge - greater than or equal - self => other
    #lt - less than - self < other
    #le less than or equal - self <= other
    def __gt__(self, other):
        return Money(self.amount > other.amount)
igor_money = Money(100)
print(igor_money)
adilet_money = Money(150)
print(adilet_money)
total_money = igor_money == adilet_money
print(total_money)