from board import Board
from player import Player


class Game:
    def __init__(self):
        self.level = 1
        self.board = Board(9)
        self.player = Player("A", "^", self.board.player_location)
        self.playing = True
        self.exit_location = [0, 0]
        self.walls = []
        self.new_level()

    def new_level(self):
        self.board = Board(9)
        self.exit_location = self.board.place_random("X")
        self.walls = []
        for w in range(self.board.size * self.level):
            self.walls.append(self.board.place_random("O"))

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
        self.player.old_location = self.player.location
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

        for w in self.walls:
            self.board.place(w[0], w[1], "O")
        self.board.place(self.exit_location[0], self.exit_location[1], "X")
        self.board.place(self.player.location[0], self.player.location[1], self.player.symbol)

    def apply_rules(self):
        #check for collisions
        for w in self.walls:
            if self.player.location == w:
                self.player.location = self.player.old_location
                print("block")

        if self.player.location == self.exit_location:
            print("YOU WIN THIS LEVEL")
            self.level += 1
            self.new_level()


game = Game()
game.loop()
