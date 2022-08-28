from board import Board


class Game:
    is_over = False
    player1 = 'White'
    player2 = 'Black'
    board = Board()

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def is_game_over(self):
        return self.is_over

    def new_game(self):
        self.board = Board()

    def get_black_player(self):
        if self.player1 == 'Black':
            return "player1"
        else:
            return "player2"

    def get_white_player(self):
        if self.player1 == 'White':
            return "player1"
        else:
            return "player2"
