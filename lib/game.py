from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.ships_placed = []
        self.ships_unplaced = [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]
        self.rows = rows
        self.cols = cols

    def unplaced_ships(self):
        return self.ships_unplaced

    def place_ship(self, length, orientation, row, col):
        ship_placement = ShipPlacement(
            length=length,
            orientation=orientation,
            row=row,
            col=col,
        )
        self.ships_placed.append(ship_placement)
        self.remove_ship(ship_placement.length)

    def remove_ship(self, length):
        # find first occurrence of ship with the specified length and remove it
        for ship in self.ships_unplaced:
            if ship.length == length:
                self.ships_unplaced.remove(ship)
                break


    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
    
    def fire_at_opponent(self):
        pass