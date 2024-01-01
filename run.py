import sys
from lib.game import Game
from lib.user_interface import UserInterface
from lib.bot_interface import BotInterface


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)

############## User player instance of the game
io = TerminalIO()
user_game = Game()
user_interface = UserInterface(io, user_game)
user_interface.run()

############## Bot player instance of the game
bot_game = Game()
bot_interface = BotInterface(bot_game)
bot_interface.run()

############## "Play" class uses both players game instances to fire shots and decide the winner
# play = Play()
# while not play.decide_winner(player1, player2):