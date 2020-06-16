import chessboard
import menu
import turtle

pos_x = None
pos_y = None


def update_pos_xy(x, y):
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

        elif draw_chessboard:
            draw_chessboard = False
            chessboard = chessboard.DrawChessBoard(turtle)
            chessboard.draw_chess_board()
