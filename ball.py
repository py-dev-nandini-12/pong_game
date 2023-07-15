from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_mov = 10
        self.y_mov = 10
        self.mov_speed = 0.1


    def move(self):
        x_pos = self.xcor() + self.x_mov
        y_pos = self.ycor() + self.y_mov
        # print(f"{y_pos}")
        # print(f"{x_pos}")
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_mov *= -1

    def bounce_x(self): #paddle strikes
        self.x_mov *= -1
        self.mov_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.mov_speed = 0.1
        self.bounce_x()


