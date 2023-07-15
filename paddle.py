from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)  # width =20,length =100,since turtle size is 20,20
        self.penup()
        self.goto(position)

    def mov_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def mov_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)