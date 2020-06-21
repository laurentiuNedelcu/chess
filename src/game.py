import chessboard
import menu
import turtle

pos_x = None
pos_y = None
chess_board = None
valid_move = False
i = 0


def update_pos_xy(x, y):
    print('(' + str(x) + ', ' + str(y) + ')')
    global pos_x, pos_y
    pos_x = x
    pos_y = y


if __name__ == '__main__':

    draw_chessboard = False
    draw_menu = True
    exit_game = False

    while not exit_game:
        if draw_menu:
            turtle.hideturtle()
            main_menu = menu.DrawMenu(turtle)

            turtle.onscreenclick(update_pos_xy)
            opt = main_menu.option_selected(pos_x, pos_y)

            if opt == 1:
                draw_menu = False
                draw_chessboard = True
                turtle.clear()
            elif opt == 2:
                pass
            elif opt == 3:
                exit_game = True

        else:
            if draw_chessboard:
                draw_chessboard = False
                chess_board = chessboard.ChessBoard(turtle)
                chess_board.draw_chess_board()
                chess_board.update_img(turtle)

            else:
                print('PIECE')
                move_piece = chess_board.on_click_piece()
                turtle.onscreenclick(chess_board.update_piece_img)
