class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        # print('ShipPlacement __init__ row/col: ', self.row, self.col)

    def covers(self, row, col):
        if self.orientation == "vertical":
            # if col is different
            if self.col != col:
                return False
            # if col is the same check rows
            # if old row <= new row < old row + old length
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length