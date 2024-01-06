import unittest

from lib.game import Game
from lib.bot_interface import *

"""
Randomly places all ships without overlap
"""
class TestRandomPlacement(unittest.TestCase):
    def test_randomly_places_all_ships_without_overlap(self):
        bot_game = Game()
        bot_interface = BotInterface(bot_game)
        bot_interface.run()

        # Get the printed board from the game
        printed_board = bot_interface._format_board()

        # Count the occurrences of 'S' in the printed board
        count_s = printed_board.count('S')

        # Assert that 'S' appears 17 times
        self.assertEqual(count_s, 17, f"Expected 'S' 17 times, but found {count_s}.")

    if __name__ == '__main__':
        unittest.main()