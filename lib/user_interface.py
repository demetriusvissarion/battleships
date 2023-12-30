class UserInterface:
    def __init__(self, io, game):
        self.io = io # game terminal interface
        self.game = game # game instance
        self.row_width = 10
        self.col_width = 10
        self.valid_new_ship_placement = False
        # self.board = []

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
    
    def is_new_ship_placement_inside_board(self):
        if 0 < int(self.ship_row) < 10:
            if 0 < int(self.ship_col) < 10:
                if self.ship_orientation == 'v':
                    if 0 < int(self.ship_col) + int(self.ship_length) < 10:
                        return True
                if self.ship_orientation == 'h':
                    if 0 < int(self.ship_row) + int(self.ship_length) < 10:
                        return True
        else:
            self._show('Position outside the board, chose again')
            return False

    def find_new_ship_placement_points(self):
        self.ship_points = {}
        counter = int(self.ship_length)
        if self.ship_orientation == 'v':
            for _ in range(0, counter):
                self.ship_points[self.row + counter] = self.col
    
    def _prompt_for_selection_row_column(self):
        while not self.valid_new_ship_placement:
            self.ship_row = self._prompt("Which row?")
            self.ship_col = self._prompt("Which column?")
            if self.is_new_ship_placement_inside_board():
                self.valid_new_ship_placement = True
                break

    def _prompt_for_ship_placement(self):
        self.ship_length = self._prompt("Which ship do you wish to place?")
        self.ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        self._prompt_for_selection_row_column()
        self.find_new_ship_placement_points()
        while True in [self.game.ship_at(row, col) for row,col in self.ship_points.items()]:
            self._show('That position is taken by another ship, chose again')
            self._prompt_for_selection_row_column()

        self._show("OK.")
        self.game.place_ship(
            length=int(self.ship_length),
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
        # print('game.ships_placed: ', self.game.ships_placed)
        return "\n".join(rows)