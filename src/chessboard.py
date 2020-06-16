class DrawChessBoard:

    def __init__(self, turtle):
        self.chessboard = turtle.Turtle()
        self.draw_screen = turtle.Screen()
        self.colour = 0  # 0 white, 1 black

        self.chessboard.speed(1000)
        self.chessboard.hideturtle()

        margin = self.draw_screen.window_width() / 8
        self.pos_x = margin - self.draw_screen.window_width() / 2
        self.pos_y = self.draw_screen.window_height() / 2 - margin

    def draw_chess_board(self):

        for i in range(8):
            for j in range(8):
                self.chessboard.penup()
                self.chessboard.goto(self.pos_x + i * 50, self.pos_y + j * (-50))
                self.chessboard.pendown()
                if self.colour == 0:
                    self.chessboard.fillcolor('white')
                    self.colour = 1
                else:
                    self.chessboard.fillcolor('black')
                    self.colour = 0
                self.chessboard.begin_fill()
                for k in range(4):
                    self.chessboard.forward(50)
                    self.chessboard.right(90)
                self.chessboard.end_fill()

            if (i + 1) % 2 == 0:
                self.colour = 0
            else:
                self.colour = 1

        return self.chessboard
