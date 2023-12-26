import random

class BotInterface:
    def __init__(self, game):
        self.game = game

    def run(self):
        self.place_ships_randomly_for_bot()

    def select_ship_orientation(self, ship_length):
        row_width = 10
        col_width = 10
        ship_orientation = random.choice(['v', 'h'])
        if ship_orientation == 'v':
            row_width -= int(ship_length)
        if ship_orientation == 'h':
            col_width -= int(ship_length)
        self.row_width = row_width
        self.col_width = col_width
        self.ship_orientation = ship_orientation
    
    def select_row_and_col(self, ship_length):
        self.select_ship_orientation(ship_length)
        ship_row = random.randint(1, 10)
        while int(ship_row) not in range(1, self.row_width + 2):
            ship_row = int(ship_row) - int(ship_length) + 1

        ship_col = random.randint(1, 10)
        while int(ship_col) not in range(1, self.col_width + 2):
            ship_col = int(ship_col) - int(ship_length) + 1
        self.ship_row = ship_row
        self.ship_col = ship_col

    def place_ships_randomly_for_bot(self):
        ship_lengths = [2, 3, 3, 4, 5]

        for ship_length in ship_lengths:
            self.select_row_and_col(ship_length)

            while self.game.ship_at(int(self.ship_row), int(self.ship_col), self.ship_orientation, ship_length):
                self.select_row_and_col(ship_length)

            self.game.place_ship(
                length=int(ship_length),
                orientation={"v": "vertical", "h": "horizontal"}[self.ship_orientation],
                row=int(self.ship_row),
                col=int(self.ship_col),
            )

    def _format_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)

    def show_board_to_dev(self):
        return self._format_board()