import turtle
import random
import math

sc = turtle.Screen()
sc.bgcolor("grey")
sc.title("**** the dot")


class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle
        self.speed(0)
        self.color("blue")
        self.pensize(5)

    def border_dimen(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)

# killer


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("turtle")
        self.color("black")
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.right(60)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def acceleratespeed(self):
        self.speed += 1

    def deceleratespeed(self):
        self.speed -= 1

    def pausespeed(self):
        self.speed = 0


# victim
class Dot(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.speed = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.right(60)

    def pauses(self):
        self.speed = 0


def collision(t1, t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a**2)+(b**2))

    if distance < 20:
        return True
    else:
        return False


play = Player()
dot = Dot()
border = Border()

border.border_dimen()

# keyboard assignin
turtle.listen()
turtle.onkey(play.turnleft, "Left")
turtle.onkey(play.turnright, "Right")
turtle.onkey(play.acceleratespeed, "Up")
turtle.onkey(play.deceleratespeed, "Down")
turtle.onkey(play.pausespeed, "space")
#turtle.onkey(dot.pauses, "space")


while True:
    play.move()
    dot.move()

    if collision(play, dot):
        dot.jump()
