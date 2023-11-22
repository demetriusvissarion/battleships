from lib.ship_placement import ShipPlacement

"""
Initialises with a length, orientation, row, and col
"""
def test_initialises_with_a_length_orientation_row_and_col():
    ship_placement = ShipPlacement(
        length=5, orientation="vertical", row=3, col=2)
    assert ship_placement.length == 5
    assert ship_placement.orientation == "vertical"
    assert ship_placement.row == 3
    assert ship_placement.col == 2


"""
Checks if vertical ships cover a given row and col
"""
def test_checks_if_vertical_ships_cover_a_given_row_and_col():
    ship_placement = ShipPlacement(
        length=5, orientation="vertical", row=3, col=2)
    assert ship_placement.covers(3, 2)
    assert ship_placement.covers(4, 2)
    assert ship_placement.covers(5, 2)
    assert ship_placement.covers(6, 2)
    assert ship_placement.covers(7, 2)
    assert not ship_placement.covers(2, 2)
    assert not ship_placement.covers(8, 2)
    assert not ship_placement.covers(3, 1)
    assert not ship_placement.covers(3, 3)


"""
Checks if horizontal ships cover a given row and col
"""
def test_checks_if_horizontal_ships_cover_a_given_row_and_col():
    ship_placement = ShipPlacement(
        length=5, orientation="horizontal", row=3, col=2)
    assert ship_placement.covers(3, 2)
    assert ship_placement.covers(3, 3)
    assert ship_placement.covers(3, 4)
    assert ship_placement.covers(3, 5)
    assert ship_placement.covers(3, 6)
    assert not ship_placement.covers(3, 1)
    assert not ship_placement.covers(3, 7)
    assert not ship_placement.covers(2, 2)
    assert not ship_placement.covers(4, 2)


"""
Has a friendly string representation
"""
def test_has_a_friendly_string_representation():
    ship_placement = ShipPlacement(
        length=5, orientation="horizontal", row=3, col=2)
    assert str(
        ship_placement) == "ShipPlacement(length=5, orientation=horizontal, row=3, col=2)"
    

"""
Checks if vertical ships are constrained to be on the board
"""
def test_checks_if_vertical_ships_are_on_the_board():
    ship_placement = ShipPlacement(
        length=5, orientation="vertical", row=10-4, col=10)
    assert ship_placement.covers(6, 10)
    assert ship_placement.covers(7, 10)
    assert ship_placement.covers(8, 10)
    assert ship_placement.covers(9, 10)
    assert ship_placement.covers(10, 10)
    assert not ship_placement.covers(1, 10)
    assert not ship_placement.covers(2, 10)
    assert not ship_placement.covers(3, 10)
    assert not ship_placement.covers(4, 10)
    assert not ship_placement.covers(5, 10)


"""
Checks if horizontal ships are constrained to be on the board
"""
def test_checks_if_horizontal_ships_are_on_the_board():
    ship_placement = ShipPlacement(
        length=5, orientation="horizontal", row=10, col=10-4)
    assert ship_placement.covers(10, 6)
    assert ship_placement.covers(10, 7)
    assert ship_placement.covers(10, 8)
    assert ship_placement.covers(10, 9)
    assert ship_placement.covers(10, 10)
    assert not ship_placement.covers(10, 1)
    assert not ship_placement.covers(10, 2)
    assert not ship_placement.covers(10, 3)
    assert not ship_placement.covers(10, 4)
    assert not ship_placement.covers(10, 5)
