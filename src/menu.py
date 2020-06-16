"""
    With this class we personalize our menu.
"""


class DrawMenu:

    def __init__(self, turtle):

        style_title = ('Courier', 60, 'bold')
        self.move_y(turtle, 150)
        turtle.write('Chess', font=style_title, align='center')

        style_menu = ('Courier', 25, '')
        self.move_y(turtle, -20)
        turtle.write('Start game', font=style_menu, align='center')
        self.move_y(turtle, -60)
        turtle.write('Options', font=style_menu, align='center')
        self.move_y(turtle, -100)
        turtle.write('Exit', font=style_menu, align='center')

    def move_y(self, turtle, y):
        turtle.up()
        turtle.sety(y)
        turtle.down()
        return

    def option_selected(self, x, y):
        print("(", x, ",", y, ")")
        if x is not None and y is not None:
            if 98.0 > x > -99.0 and 12.0 > y > -10.0:
                return 1
            elif 67.0 > x > -70.0 and -29.0 > y > -55.0:
                return 2
            elif 37.0 > x > -39.0 and -69.0 > y > -90.0:
                return 3
        return -1