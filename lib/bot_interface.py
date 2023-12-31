import random

class BotInterface:
    def __init__(self, game):
        self.game = game # game instance
        self.row_width = 10
        self.col_width = 10
        self.valid_new_ship_placement = False
        self.ship_row = 0
        self.ship_col = 0
        self.dev_mode = True # change to False when going in production

    def run(self, runs = 5):
        while len(self.game.ships_unplaced) > 0:
            while runs > 0:
                if self.dev_mode == True:
                    print(f"<dev> Bot has these ships remaining: {', '.join(self.ships_unplaced())}")
                self.random_ship_placement()
                runs -= 1
                self.valid_new_ship_placement = False
            break
        
        if self.dev_mode == True:
            print(self._format_board())

    def ships_unplaced(self):
        ship_lengths = [str(ship.length) for ship in self.game.ships_unplaced]
        return ship_lengths
    
    def is_new_ship_placement_inside_board(self):
        if 0 < int(self.ship_row) < 11:
            if 0 < int(self.ship_col) < 11:
                if self.ship_orientation == 'v':
                    if 0 < int(self.ship_row) + int(self.ship_length) < 11:
                        # print('v - int(self.ship_row) + int(self.ship_length): ', int(self.ship_row) + int(self.ship_length))
                        # print('self.ship_row: ', self.ship_row)
                        # print('self.ship_col: ', self.ship_col)
                        return True
                    else:
                        return False
                if self.ship_orientation == 'h':
                    if 0 < int(self.ship_col) + int(self.ship_length) < 11:
                        # print('h - int(self.ship_col) + int(self.ship_length): ', int(self.ship_col) + int(self.ship_length))
                        # print('self.ship_row: ', self.ship_row)
                        # print('self.ship_col: ', self.ship_col)
                        return True
                    else:
                        return False
        else:
            return False
    
    def random_col_row_placement(self):
        max_attempts = 20  # Adjust as needed
        attempts = 0

        while not self.valid_new_ship_placement and attempts < max_attempts:
            self.ship_row = random.randint(1, 11 - int(self.ship_length))
            # print('self.ship_row: ', self.ship_row)
            self.ship_col = random.randint(1, 11 - int(self.ship_length))
            # print('self.ship_col: ', self.ship_col)
            if self.is_new_ship_placement_inside_board():
                self.valid_new_ship_placement = True
                break
            else:
                self.ship_row = 0
                self.ship_col = 0
                attempts += 1

    def find_new_ship_placement_points(self):
        self.ship_points = []
        counter = int(self.ship_length)
        if self.ship_orientation == 'v':
            for _ in range(0, int(self.ship_length)):
                self.ship_points.append([int(self.ship_row) + counter - 1, int(self.ship_col)])
                counter -= 1
        if self.ship_orientation == 'h':
            for _ in range(0, int(self.ship_length)):
                self.ship_points.append([int(self.ship_row), int(self.ship_col) + counter - 1])
                counter -= 1
    
    def random_ship_placement_helper(self):
        self.ship_orientation = random.choice(['v', 'h'])
        self.random_col_row_placement()
        self.find_new_ship_placement_points()
        self.checking_all_point = [self.game.ship_at(pair_row_col[0], pair_row_col[1]) for pair_row_col in self.ship_points]
        # print('self.checking_all_point: ', self.checking_all_point)

    def random_ship_placement(self):
        self.ship_length = random.choice(self.ships_unplaced())
        self.random_ship_placement_helper()
        # print('self.ship_length: ', self.ship_length)
        # print('self.ship_orientation: ', self.ship_orientation)

        while True in self.checking_all_point:
            self.valid_new_ship_placement = False
            self.random_ship_placement_helper()

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
        return "\n".join(rows)