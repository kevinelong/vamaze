import random


class Character:
    def __init__(self, name, symbol, location=[0, 0]):
        self.name = name
        self.symbol = symbol
        self.location = location
        self.old_location = location

        self.health = 100
        self.attack = 10
        self.items = []

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


class Treasure(Character):
    def __init__(self, symbol="T"):
        super().__init__("Treasure", symbol)
        self.items = []
        possibilities = [
            Sword(),
            Sword(),
            Hammer(),
            Hammer(),
            Hammer(),
            Gold(),
            Gem(),
            Gold(),
            Gem(),
            Gold(),
            Gem(),
            Gold(),
            Gem(),
        ]
        item_count = random.randint(1, 4)
        for i in range(item_count):
            self.items.append(possibilities[random.randint(0, len(possibilities) - 1)])


class InventoryItem:
    def __init__(self, name, quantity=1):
        self.name = name
        self.quantity = quantity


class Gold(InventoryItem):
    def __init__(self):
        super().__init__("Gold", 100)


class Gem(InventoryItem):
    def __init__(self):
        super().__init__("Gem", 10)


class Weapon(InventoryItem):
    def __init__(self, name, damage_modifier = 5):
        super().__init__(name)
        self.damage_modifier = damage_modifier


class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 15)


class Hammer(Weapon):
    def __init__(self):
        super().__init__("Hammer", 10)
