class UserInterface:
    def __init__(self, io, game):
        self.io = io
        self.game = game
        self.board = []

    def run(self, runs = 5):
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")

        while len(self.game.ships_unplaced) > 0:
            while runs > 0:
                self._show("You have these ships remaining: {}".format(
                    self._ships_unplaced_message()))
                self._prompt_for_ship_placement()
                self._show("This is your board now:")
                self._show(self._format_board())
                runs -= 1
            break

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.ships_unplaced]
        return ", ".join(ship_lengths)
    
    def _prompt_for_selection_vert_or_hor(self, ship_length):
        row_width = 10
        col_width = 10
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        if ship_orientation == 'v':
            row_width -= int(ship_length)
        if ship_orientation == 'h':
            col_width -= int(ship_length)
        self.ship_orientation = ship_orientation
        self.row_width = row_width
        self.col_width = col_width
    
    def _prompt_for_selection_row_column(self, ship_length):
        self._prompt_for_selection_vert_or_hor(ship_length)

        ship_row = self._prompt("Which row?")
        while int(ship_row) not in range(1, self.row_width + 2):
            ship_row = int(ship_row) - int(ship_length) + 1
        self.ship_row = ship_row

        ship_col = self._prompt("Which column?")
        while int(ship_col) not in range(1, self.col_width + 2):
            ship_col = int(ship_col) - int(ship_length) + 1
        self.ship_col = ship_col

    def _prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        self._prompt_for_selection_row_column(ship_length)
        while self.game.ship_at(int(self.ship_row), int(self.ship_col)):
            print('That postion is taken by another ship, chose again')
            self._prompt_for_selection_row_column(ship_length)

        self._show("OK.")
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
        # self.board = rows
        # print('self.board: ', self.board)
        print('game.ships_placed: ', self.game.ships_placed)
        return "\n".join(rows)
