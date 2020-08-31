import turtle
import os
import winsound
import math

stupid = turtle.Screen()
stupid.bgcolor("black")
stupid.title("make him poop")
stupid.bgpic("poop.gif")
stupid.register_shape("dust.gif")


class Pts(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup
        self.hideturtle
        self.speed(0)
        self.color("black")
        self.goto(-200, 230)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("colctd : {}".format(self.score), False,
                   align="Left", font=("Ariel", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

    def play_sound(self):
        winsound.Beep(2000, 100)


# border
class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle
        self.speed(0)
        self.color("black")
        self.pensize(5)

    def border_dimen(self):
        self.penup()
        self.goto(-250, -250)
        self.pendown
        self.goto(-250, 250)
        self.goto(250, 250)
        self.goto(250, -250)
        self.goto(-250, -250)

# head of the person


class Head(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle
        self.speed(0)
        self.shape("circle")
        self.goto(-100, 230)
        self.color("black")
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 240 or self.xcor() < -240:
            self.left(60)
        if self.ycor() > 240 or self.ycor() < -240:
            self.right(60)


class Body(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()

        self.speed(0)
        self.shape("square")
        self.color("black")
        self.goto(-100, 210)
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 240 or self.xcor() < -240:
            self.left(60)
        if self.ycor() > 240 or self.ycor() < -240:
            self.right(60)


class Shit(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(-100, 210)
        self.shape("classic")
        self.color("black")
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 240 or self.xcor() < -240:
            self.left(60)

    def shoot(self):
        self.right(90)
        self.speed += 4

    def collected(self):
        self.goto(500, 500)


class Binn(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("dust.gif")
        self.speed = 2
        self.goto(100, -230)

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 240 or self.xcor() < -240:
            self.left(60)
        if self.ycor() > 240 or self.ycor() < -240:
            self.right(60)


def inbinn(t1, t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a**2)+(b**2))

    if distance < 20:
        return True
    else:
        return False


head = Head()
body = Body()

binn = Binn()
pts = Pts()
border = Border()
border.border_dimen()

shit = Shit()

# keyboard assign
turtle.listen()
turtle.onkey(shit.shoot, "space")
# stupid.tracer(0)

while True:

    head.move()
    body.move()
    binn.move()
    shit.move()

    if inbinn(shit, binn):
        shit.collected()
        pts.change_score(1)
        pts.play_sound()
