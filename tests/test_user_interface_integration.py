import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


class TestUserInterface(unittest.TestCase):
    def test_ship_setup_scenario(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which ship do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        interface.run(1)


    """
    When we select a position to place a ship on the board
    Ships to be constrained not to overlap if the first point intersects
    """
    def test_when_we_place_a_ship_not_to_overlap_first_point_intersection(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")

        # place ship 1
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which ship do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))

        # place ship 2
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which ship do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        # try to place it on a covered position
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("That position is taken by another ship, chose again")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "SSS.......",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))

        interface.run(2)



    """
    When we select a position to place a ship on the board
    Ships to be constrained not to overlap if middle points intersect
    """
    def test_when_we_place_a_ship_not_to_overlap_middle_intersection(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")

        # place ship 1
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which ship do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            "....S.....",
            "....S.....",
            "....S.....",
            "....S.....",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))

        # place ship 2
        io.expect_print("You have these ships remaining: 2, 3, 3, 5")
        io.expect_print("Which ship do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        # try to place it on a covered position
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("3")
        io.expect_print("That position is taken by another ship, chose again")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("1")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "SSSSS.....",
            "..........",
            "....S.....",
            "....S.....",
            "....S.....",
            "....S.....",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))

        interface.run(2)