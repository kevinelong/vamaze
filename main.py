
from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board(9)
        self.player = Player("A", "^", self.board.player_location)
        self.playing = True
        self.loop()

    def loop(self):
        while self.playing:
            self.update_display()
            self.user_input()
            self.apply_rules()

    def update_display(self):
        self.board.refresh()

    def user_input(self):
        text = input("Which direction? or q to quit.")
        upper = text.upper()
        if upper in ["NORTH", "UP", "W"]:
            self.move_player_up()

    def move_player_up(self):
        x = self.player.location[0]
        y = self.player.location[1]
        y = y - 1
        self.board.clear()
        self.board.place(x, y, self.player.symbol)
        self.player.location[0] = x
        self.player.location[1] = y

    def apply_rules(self):
        pass

game = Game()
