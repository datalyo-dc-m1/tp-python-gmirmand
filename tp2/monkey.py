class Monkey:
    def __init__(self, name, banana):
        self.name = name
        self.banana = banana
    def eat(self):
        print(self.name, 'a mangé une banane', self.banana.color)

class Banana:
    def __init__(self, color):
        self.color = color


banana_green = Banana('verte')
banana_yellow = Banana('jaune')
pierre = Monkey("Pierre", banana_green)
bob = Monkey("bob", banana_yellow)

pierre.eat()
bob.eat()
