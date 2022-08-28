class Piece:
    symbol = ""
    color = ""
    x = 0
    y = 0

    def __init__(self, symbol, color):
        self.symbol = symbol
        self.color = color


class Pawn(Piece):

    def __init__(self, symbol, color):
        super().__init__(symbol, color)


class Rook(Piece):

    def __init__(self, symbol, color):
        super().__init__(symbol, color)


class Bishop(Piece):

    def __init__(self, symbol, color):
        super().__init__(symbol, color)


class Knight(Piece):

    def __init__(self, symbol, color):
        super().__init__(symbol, color)


class Queen(Piece):

    def __init__(self, symbol, color):
        super().__init__(symbol, color)


class King(Piece):

    def __init__(self, symbol, color):
        super().__init__(symbol, color)
