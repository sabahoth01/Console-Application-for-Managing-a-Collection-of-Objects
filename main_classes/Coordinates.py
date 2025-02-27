class Coordinates:
    def __init__(self, x, y):
        if x <= -61 or None:
            raise ValueError("x must be greater than -61, cannot be null!!")
        else:
            self.x = x  # Must be greater than -61, cannot be null
        if y is None:
            raise ValueError("y cannot be null!!")
        else:
            self.y = y  # Cannot be null
