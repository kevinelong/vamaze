class Character:
    def __init__(self, name, symbol, location=[0, 0]):
        self.name = name
        self.symbol = symbol
        self.location = location
        self.old_location = location

        self.health = 100
        self.attack = 10

    def __str__(self):
        return f"{self.name} has {self.health}."


class Player(Character):
    def __init__(self, name, symbol="^"):
        super().__init__(name, symbol)
        self.attack = 20


class Monster(Character):
    def __init__(self, name, symbol="M"):
        super().__init__(name, symbol)
        self.attack = 5
