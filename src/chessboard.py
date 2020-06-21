import os

import piece

TILE_SIZE = 50


class ChessBoard:

    def __init__(self, turtle):

        self.chessboard = turtle.Turtle()
        self.draw_screen = turtle.Screen()
        self.whitePieces = []
        self.blackPieces = []
        self.pieces_in_board = []
        self.piece_index = -1
        self._exit = False

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

    def update_piece_img(self, x, y):
        print('UPDATING')
        p = self.whitePieces[self.piece_index]
        p.update_position_img(x, y)
        piece_in_board = self.pieces_in_board[self.piece_index]
        piece_in_board.up()
        piece_in_board.goto(p.get_pos_img(0), p.get_pos_img(1))
        piece_in_board.shape(p.get_img())

    def update_img(self, turtle):

        # White pieces
        for p in self.whitePieces:
            piece_in_board = turtle.Turtle()
            piece_in_board.up()
            piece_in_board.goto(p.get_pos_img(0), p.get_pos_img(1))
            piece_in_board.shape(p.get_img())
            self.pieces_in_board.append(piece_in_board)

        # Black pieces
        for p in self.blackPieces:
            piece_in_board = turtle.Turtle()
            piece_in_board.up()
            piece_in_board.goto(p.get_pos_img(0), p.get_pos_img(1))
            piece_in_board.shape(p.get_img())

        self.chessboard.hideturtle()

    def setup_pieces(self):

        # White pieces
        self.whitePieces.append(
            piece.Piece(0, 0, -230, -170, 'white', TILE_SIZE, 'R', self.pieces_img.get('rook_white')))
        self.whitePieces.append(
            piece.Piece(0, 1, -180, -170, 'white', TILE_SIZE, 'Kn', self.pieces_img.get('knight_white')))
        self.whitePieces.append(
            piece.Piece(0, 2, -130, -170, 'white', TILE_SIZE, 'B', self.pieces_img.get('bishop_white')))
        self.whitePieces.append(
            piece.Piece(0, 3, -80, -170, 'white', TILE_SIZE, 'Q', self.pieces_img.get('queen_white')))
        self.whitePieces.append(
            piece.Piece(0, 4, -30, -170, 'white', TILE_SIZE, 'K', self.pieces_img.get('king_white')))
        self.whitePieces.append(
            piece.Piece(0, 5, 20, -170, 'white', TILE_SIZE, 'B', self.pieces_img.get('bishop_white')))
        self.whitePieces.append(
            piece.Piece(0, 6, 70, -170, 'white', TILE_SIZE, 'Kn', self.pieces_img.get('knight_white')))
        self.whitePieces.append(
            piece.Piece(0, 7, 120, -170, 'white', TILE_SIZE, 'R', self.pieces_img.get('rook_white')))

        # Black pieces
        self.blackPieces.append(
            piece.Piece(7, 0, -230, 180, 'black', TILE_SIZE, 'R', self.pieces_img.get('rook_black')))
        self.blackPieces.append(
            piece.Piece(7, 1, -180, 180, 'black', TILE_SIZE, 'Kn', self.pieces_img.get('knight_black')))
        self.blackPieces.append(
            piece.Piece(7, 2, -130, 180, 'black', TILE_SIZE, 'B', self.pieces_img.get('bishop_black')))
        self.blackPieces.append(
            piece.Piece(7, 3, -80, 180, 'black', TILE_SIZE, 'Q', self.pieces_img.get('queen_black')))
        self.blackPieces.append(piece.Piece(7, 4, -30, 180, 'black', TILE_SIZE, 'K', self.pieces_img.get('king_black')))
        self.blackPieces.append(
            piece.Piece(7, 5, 20, 180, 'black', TILE_SIZE, 'B', self.pieces_img.get('bishop_black')))
        self.blackPieces.append(
            piece.Piece(7, 6, 70, 180, 'black', TILE_SIZE, 'Kn', self.pieces_img.get('knight_black')))
        self.blackPieces.append(piece.Piece(7, 7, 120, 180, 'black', TILE_SIZE, 'R', self.pieces_img.get('rook_black')))

        # Pawns for white and black pieces
        for i in range(8):
            self.whitePieces.append(
                piece.Piece(1, i, -230 + 50 * i, -120, 'white', TILE_SIZE, 'P', self.pieces_img.get('pawn_white')))
            self.blackPieces.append(
                piece.Piece(6, i, -230 + 50 * i, 130, 'black', TILE_SIZE, 'P', self.pieces_img.get('pawn_black')))

        # Register shape of pieces images
        for key in self.pieces_img.keys():
            self.draw_screen.register_shape(self.pieces_img.get(key))

    def on_click_piece(self):
        self._exit = False
        self.draw_screen.listen()
        i = 0

        while not self._exit:
            p = self.pieces_in_board[i]
            p.onclick(self.piece_selected)
            if not self._exit:
                i += 1
                if i == len(self.pieces_in_board):
                    i = 0

        self.piece_index = i

        return True

    def piece_selected(self, x, y):
        print('x: ' + str(x) + ', y: ' + str(y))
        self._exit = True

    def draw_chess_board(self):

        self.chessboard.speed(0)
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
