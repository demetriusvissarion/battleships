from lib.game import Game
from lib.user_interface import UserInterface
from lib.bot_interface import BotInterface

class Play:
    def __init__(self, io):
        self.io = io
        ############## User player instance of the game
        self.user_game = Game()
        self.user_interface = UserInterface(self.io, self.user_game)
        ############## Bot player instance of the game
        self.bot_game = Game()
        self.bot_interface = BotInterface(self.bot_game)
        self.shots_fired = []

    def run(self):
        self.user_interface.run()
        self.bot_interface.run()
        # while not self.winner:
        print(self.show_shots_to_opponent_board())


    def fire_at_opponent(self, row, col):
        # add firing at opponent here
        shot = self.bot_game.receive_attack(row, col)
        self.shots_fired.append((row, col, shot))
            # get 'hit' or 'miss' message after firing
            # show opponent board with only the shots fired
                # show hits with 'X' and misses with 'O'
                # if 'hit':
                    # I get another consecutive free shot until a 'miss'
                    # the oponent ship that gets hit gets a attribute 'hit' at that precise coordinates
                        # change user_interface._format_board() to mark with 'X' hits
                        # change bot_interface._format_board() to mark with 'X' hits
                # if 'miss':
                    # pass the turn to the opponent
        
    def show_shots_to_opponent_board(self):
        rows = []
        for row in range(1, self.bot_game.rows + 1):
            row_cells = []
            for col in range(1, self.bot_game.cols + 1):
                if (row, col, "X") in self.shots_fired:
                    row_cells.append("X")  # display 'X' for a hit
                elif (row, col, "O") in self.shots_fired:
                    row_cells.append("O")  # display 'O' for a miss
                else:
                    row_cells.append(".")  # display '.' for empty space
            rows.append("".join(row_cells))
        return "\n".join(rows)
        
    def opponent_fires_at_me(self):
        # add opponent firing at me here
            # see my board with 'hit' or 'miss' message after firing
                # if 'hit':
                    # opponent gets another consecutive free shot until a 'miss'
                # if 'miss':
                    # turn gets passed to me
        pass
    
    def decide_winner(self):
        # check both players ships after every shot fired
        # if a players ships all have the 'sunk' attribute than the other player name is saved as self.winner
        pass