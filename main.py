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
        self.board.refresh()

    def user_input(self):
        text = input("Which direction? or q to quit.")
        upper = text.upper()
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
        x = self.player.location[0]
        y = self.player.location[1]
        y = y - 1
        self.board.clear()
        self.board.place(self.exit_location[0], self.exit_location[1], "X")
        self.board.place(x, y, self.player.symbol)
        self.player.location[0] = x
        self.player.location[1] = y

    def move_player_down(self):
        x = self.player.location[0]
        y = self.player.location[1]
        y = y + 1
        self.board.clear()
        self.board.place(self.exit_location[0], self.exit_location[1], "X")
        self.board.place(x, y, self.player.symbol)
        self.player.location[0] = x
        self.player.location[1] = y

    def move_player_left(self):
        x = self.player.location[0]
        y = self.player.location[1]
        x = x - 1
        self.board.clear()
        self.board.place(self.exit_location[0], self.exit_location[1], "X")
        self.board.place(x, y, self.player.symbol)
        self.player.location[0] = x
        self.player.location[1] = y

    def move_player_right(self):
        x = self.player.location[0]
        y = self.player.location[1]
        x = x + 1
        self.board.clear()
        self.board.place(self.exit_location[0], self.exit_location[1], "X")
        self.board.place(x, y, self.player.symbol)
        self.player.location[0] = x
        self.player.location[1] = y

    def apply_rules(self):
        if self.player.location == self.exit_location:
            print("YOU WIN THIS LEVEL")
            self.level += 1
            self.new_level()


game = Game()
game.loop()
