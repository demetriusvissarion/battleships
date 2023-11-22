class UserInterface:
    def __init__(self, io, game):
        self.io = io
        self.game = game

    def run(self):
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")
        self._show("You have these ships remaining: {}".format(
            self._ships_unplaced_message()))
        self._prompt_for_ship_placement()
        self._show("This is your board now:")
        self._show(self._format_board())

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.unplaced_ships()]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        row_width = 10
        col_width = 10
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")

        if ship_orientation == 'v':
            row_width -= int(ship_length)
        if ship_orientation == 'h':
            col_width -= int(ship_length)

        ship_row = self._prompt(f"Which row?")
        while int(ship_row) not in range(1, row_width + 2):
            ship_row = int(ship_row) - int(ship_length) + 1

        ship_col = self._prompt(f"Which column?")
        while int(ship_col) not in range(1, col_width + 2):
            ship_col = int(ship_col) - int(ship_length) + 1

        self._show("OK.")
        self.game.place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
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
