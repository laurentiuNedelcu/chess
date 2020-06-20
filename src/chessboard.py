import piece

TILE_SIZE = 50


class ChessBoard:

    def __init__(self, turtle):

        self.chessboard = turtle.Turtle()
        self.draw_screen = turtle.Screen()
        self.whitePieces = []
        self.blackPieces = []
        self.pieces_img = {'bishop_black': 'resources/bishop_black.gif', 'bishop_white': 'resources/bishop_white.gif',
                           'king_black': 'resources/king_black.gif', 'king_white': 'resources/king_white.gif',
                           'knight_black': 'resources/knight_black.gif', 'knight_white': 'resources/knight_white.gif',
                           'pawn_black': 'resources/pawn_black.gif', 'pawn_white': 'resources/pawn_white.gif',
                           'queen_black': 'resources/queen_black.gif', 'queen_white': 'resources/queen_white.gif',
                           'rook_black': 'resources/rook_black.gif', 'rook_white': 'resources/rook_white.gif'}
        self.setup_pieces()

        self.colour = 0  # 0 white, 1 black
        margin = self.draw_screen.window_width() / 8
        self.pos_x = margin - self.draw_screen.window_width() / 2
        self.pos_y = self.draw_screen.window_height() / 2 - margin

    def setup_pieces(self):

        for i in self.pieces_img:
            self.draw_screen.register_shape(i)

        # White pieces
        self.whitePieces.append(piece.Piece(0, 0, 'white', TILE_SIZE, 'R'))
        self.whitePieces.append(piece.Piece(0, 1, 'white', TILE_SIZE, 'Kn'))
        self.whitePieces.append(piece.Piece(0, 2, 'white', TILE_SIZE, 'B'))
        self.whitePieces.append(piece.Piece(0, 3, 'white', TILE_SIZE, 'Q'))
        self.whitePieces.append(piece.Piece(0, 4, 'white', TILE_SIZE, 'K'))
        self.whitePieces.append(piece.Piece(0, 5, 'white', TILE_SIZE, 'B'))
        self.whitePieces.append(piece.Piece(0, 6, 'white', TILE_SIZE, 'Kn'))
        self.whitePieces.append(piece.Piece(0, 7, 'white', TILE_SIZE, 'R'))

        # Black pieces
        self.blackPieces.append(piece.Piece(7, 0, 'black', TILE_SIZE, 'R'))
        self.blackPieces.append(piece.Piece(7, 1, 'black', TILE_SIZE, 'Kn'))
        self.blackPieces.append(piece.Piece(7, 2, 'black', TILE_SIZE, 'B'))
        self.blackPieces.append(piece.Piece(7, 3, 'black', TILE_SIZE, 'Q'))
        self.blackPieces.append(piece.Piece(7, 4, 'black', TILE_SIZE, 'K'))
        self.blackPieces.append(piece.Piece(7, 5, 'black', TILE_SIZE, 'B'))
        self.blackPieces.append(piece.Piece(7, 6, 'black', TILE_SIZE, 'Kn'))
        self.blackPieces.append(piece.Piece(7, 7, 'black', TILE_SIZE, 'R'))

        # Pawns for white and black pieces
        for i in range(7):
            self.whitePieces.append(piece.Piece(1, i, 'white', TILE_SIZE, 'P'))
            self.blackPieces.append(piece.Piece(6, i, 'black', TILE_SIZE, 'P'))

    def draw_chess_board(self):

        self.chessboard.speed(1000)
        self.chessboard.hideturtle()

        for i in range(8):
            for j in range(8):
                self.chessboard.penup()
                self.chessboard.goto(self.pos_x + i * TILE_SIZE, self.pos_y + j * (-TILE_SIZE))
                self.chessboard.pendown()
                if self.colour == 0:
                    self.chessboard.fillcolor('white')
                    self.colour = 1
                else:
                    self.chessboard.fillcolor('black')
                    self.colour = 0
                self.chessboard.begin_fill()
                for k in range(4):
                    self.chessboard.forward(TILE_SIZE)
                    self.chessboard.right(90)
                self.chessboard.end_fill()

            if (i + 1) % 2 == 0:
                self.colour = 0
            else:
                self.colour = 1

        return self.chessboard
