import turtle


class Piece:

    def __init__(self, x, y, pos_x, pos_y, colour, tile_size, letter, img=None):
        self.piece = turtle.Turtle()
        self.colour = colour
        self.img = img
        self.taken = False
        self.movingPiece = False
        self.tile_size = tile_size
        self.letter = letter

        self.posImg = (pos_x, pos_y)
        self.position = (x, y)

    def get_pos_img(self, index):
        return self.posImg[index]

    def get_img(self):
        return self.img

    def in_boards(self):
        if 8 > self.position[0] >= 0 and 8 > self.position[1] >= 0:
            return True
        return False

    def move(self, x, y, board):
        opponent_piece = board.get_piece_at(x, y)
        if opponent_piece is not None:
            opponent_piece.taken = True

        self.posImg = (x * self.tile_size + self.tile_size / 2, y * self.tile_size + self.tile_size / 2)
        self.position = (x, y)

    def attacking_ally(self, x, y, board):
        opponent_piece = board.get_piece_at(x, y)
        if opponent_piece is not None:
            if opponent_piece.colour == self.colour:
                return True
        return False


