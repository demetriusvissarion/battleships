class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        # print('ShipPlacement __init__ row/col: ', self.row, self.col)

    def covers(self, row, col, position = None, length = None):
        if position == None and length == None:
            if self.orientation == "vertical":
                if self.col != col:
                    return False
                return self.row <= row < self.row + self.length
            else:
                if self.row != row:
                    return False
                return self.col <= col < self.col + self.length
        
        if position == 'v':
            # print('here - v')
            counter = int(length)
            while counter > 0:
                counter_value = counter
                counter -= 1
                if self.orientation == "vertical":
                    if self.col <= col < self.col + self.length or self.row <= row + counter_value < self.row + self.length:
                        return True
                else:
                    if self.row <= row < self.row + self.length or self.col <= col < self.col + self.length:
                        return True
        
        if position == 'h':
            # print('here - h')
            counter = int(length)
            while counter > 0:
                counter_value = counter
                counter -= 1
                if self.orientation == "vertical":
                    if self.col <= col < self.col + self.length or self.row <= row < self.row + self.length:
                        return True
                else:
                    if self.row <= row < self.row + self.length or self.col <= col + counter_value < self.col + self.length:
                        return True

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
    


