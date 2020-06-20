import os

import piece

TILE_SIZE = 50


class ChessBoard:

    def __init__(self, turtle):

        self.chessboard = turtle.Turtle()
        self.draw_screen = turtle.Screen()
        self.whitePieces = []
        self.blackPieces = []

        current_path = os.path.dirname(__file__)  # Where your .py file is located
        current_path = current_path.replace('src', 'resources')

        self.pieces_img = {'bishop_black': os.path.join(current_path, 'bishop_black.gif'),
                           'bishop_white': os.path.join(current_path, 'bishop_white.gif'),
                           'king_black': os.path.join(current_path, 'king_black.gif'),
                           'king_white': os.path.join(current_path, 'king_white.gif'),
                           'knight_black': os.path.join(current_path, 'knight_black.gif'),
                           'knight_white': os.path.join(current_path, 'knight_white.gif'),
                           'pawn_black': os.path.join(current_path, 'pawn_black.gif'),
                           'pawn_white': os.path.join(current_path, 'pawn_white.gif'),
                           'queen_black': os.path.join(current_path, 'queen_black.gif'),
                           'queen_white': os.path.join(current_path, 'queen_white.gif'),
                           'rook_black': os.path.join(current_path, 'rook_black.gif'),
                           'rook_white': os.path.join(current_path, 'rook_white.gif')}

        self.setup_pieces()

        self.colour = 0  # 0 white, 1 black
        margin = self.draw_screen.window_width() / 8
        self.pos_x = margin - self.draw_screen.window_width() / 2
        self.pos_y = self.draw_screen.window_height() / 2 - margin

    def setup_pieces_img(self, turtle):
        for key in self.pieces_img.keys():
            print(self.pieces_img.get(key))
            self.draw_screen.register_shape(self.pieces_img.get(key))

        # Black pieces
        pieces_in_board = []
        pieces = [
            [-230, 180, self.pieces_img['rook_black']],
            [-180, 180, self.pieces_img['knight_black']],
            [-130, 180, self.pieces_img['bishop_black']],
            [-80, 180, self.pieces_img['queen_black']],
            [-30, 180, self.pieces_img['king_black']],
            [20, 180, self.pieces_img['bishop_black']],
            [70, 180, self.pieces_img['knight_black']],
            [120, 180, self.pieces_img['rook_black']],
            [-230, -170, self.pieces_img['rook_white']],
            [-180, -170, self.pieces_img['knight_white']],
            [-130, -170, self.pieces_img['bishop_white']],
            [-80, -170, self.pieces_img['queen_white']],
            [-30, -170, self.pieces_img['king_white']],
            [20, -170, self.pieces_img['bishop_white']],
            [70, -170, self.pieces_img['knight_white']],
            [120, -170, self.pieces_img['rook_white']]
        ]

        for i in range(8):
            pieces.append([-230+50*i, 130, self.pieces_img['pawn_black']])
            pieces.append([-230+50*i, -120, self.pieces_img['pawn_white']])

        for p in pieces:
            piece_in_board = turtle.Turtle()
            piece_in_board.up()
            piece_in_board.goto(p[0], p[1])
            piece_in_board.shape(p[2])

            piece_in_board.width = 10
            piece_in_board.height = 10

            pieces_in_board.append(piece_in_board)

        return pieces_in_board

    def setup_pieces(self):

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
        for i in range(8):
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
                    self.chessboard.fillcolor('brown')
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
