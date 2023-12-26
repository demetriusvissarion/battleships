# from lib.bot_interface import *
# from lib.game import Game

# """
# Randomly places all ships without overlap
# """
# def test_randomly_places_all_ships_without_overlap():
#     game = Game()
#     bot_player = BotInterface(game)
#     bot_player.run()
#     board = bot_player._format_board()
#     print(print)
#     total_length = 0
#     for ship in game.ships_placed:
#         total_length += ship.length

#     total_covered = 0
#     for char in board:
#         if char == 'S':
#             total_covered += 1

#     assert total_length == total_covered
#     bot_player.place_ships_randomly_for_bot.assert_called()