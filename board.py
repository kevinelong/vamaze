import random
class Board:
    def __init__(self, size=9):
        self.size = size
        self.clear()
        self.player_location = self.place_random()

    def place(self, x, y, symbol):
        self.board[y][x] = symbol

    def place_random(self, symbol="^"):
        row = random.randint(0, self.size - 1)
        column = random.randint(0, self.size - 1)
        self.place(column, row, symbol)
        return [column, row]

    def clear(self):
        self.board = []
        for y in range(self.size):
            row = []
            for x in range(self.size):
                row.append(".")
            self.board.append(row)

    def refresh(self):
        for row in self.board:
            for value in row:
                print(value, end=" ")
            print("")

    def __str__(self):
        row_list = []
        for row in self.board:
            row_list.append(" ".join(row))
        return "\n".join(row_list)