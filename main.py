from board import Board
from player import Player, Monster
import random


class Game:
    def __init__(self):
        self.level = 1
        self.moves = 0
        self.board = Board(9)
        self.player = Player("A", "^")
        self.playing = True
        self.exit_location = [0, 0]
        self.walls = []
        self.monsters = []
        self.new_level()

    def new_level(self):
        self.moves = 0
        self.board = Board(9)
        self.exit_location = self.board.place_random("X")
        self.walls = []
        self.monsters = []
        for m in range((self.board.size // 2) * self.level):
            monster = Monster("M")
            monster.location = self.board.place_random("M")
            self.monsters.append(monster)
        for w in range((self.board.size // 2) * self.level):
            self.walls.append(self.board.place_random("O"))
        self.player.health = 100

    def loop(self):
        while self.playing:
            self.update_display()
            self.user_input()
            self.apply_rules()
        print("Thanks for playing!")

    def update_display(self):
        print(f"LEVEL: {self.level}")
        self.populate()
        self.board.refresh()

    def user_input(self):
        text = input("Which direction? or q to quit.")
        upper = text.upper()
        self.player.old_location = [self.player.location[0], self.player.location[1]]

        self.moves += 1

        if upper == "Q":
            self.playing = False
        elif upper in ["NORTH", "UP", "W"]:
            self.move_player_up()
        elif upper in ["SOUTH", "DOWN", "S"]:
            self.move_player_down()
        elif upper in ["WEST", "LEFT", "A"]:
            self.move_player_left()
        elif upper in ["EAST", "RIGHT", "D"]:
            self.move_player_right()

    def move_player_up(self):
        self.player.location[1] -= 1

    def move_player_down(self):
        self.player.location[1] += 1

    def move_player_left(self):
        self.player.location[0] -= 1

    def move_player_right(self):
        self.player.location[0] += 1

    def populate(self):
        self.board.clear()

        for monster in self.monsters:
            self.board.place(monster.location[0], monster.location[1], "M")

        for w in self.walls:
            self.board.place(w[0], w[1], "O")

        self.board.place(self.exit_location[0], self.exit_location[1], "X")
        self.board.place(self.player.location[0], self.player.location[1], self.player.symbol)

    def apply_rules(self):
        #check for collisions
        for w in self.walls:
            if self.player.location == w:
                self.player.location = self.player.old_location
                self.player.location = [self.player.old_location[0], self.player.old_location[1]]

                print("BLOCKED!")
        for monster in self.monsters:
            if self.player.location == monster.location:
                print("FIGHT!")
                self.fight(self.player, monster)

        if self.player.location == self.exit_location:
            print(f"YOU WON THIS LEVEL IN {self.moves} MOVES!")
            self.level += 1
            self.new_level()

    def fight(self, c1, c2):
        round_count = 1
        while c1.health > 0 and c2.health > 0:
            c1.health -= random.randint(1, c2.attack)
            c2.health -= random.randint(1, c1.attack)
            print(f"ROUND: {round_count}", c1, c2)
            round_count += 1
        print("FIGHT OVER")
        if c1.health <= 0:
            if type(c1) is Monster:
                self.monsters.remove(c1)
            else:
                print("PLAYER HAS DIED. GAME OVER.")
                self.playing = False
        if c2.health <= 0:
            if type(c2) is Monster:
                self.monsters.remove(c2)
            else:
                print("PLAYER HAS DIED. GAME OVER.")
                self.playing = False


game = Game()
game.loop()
