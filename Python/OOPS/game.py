import turtle
import random
import math
import os
import winsound

sc = turtle.Screen()
sc.bgcolor("grey")
sc.title("**** the turts")
sc.bgpic("tort.gif")
# sc.register_shape("")


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
        self.write("Kills : {}".format(self.score), False,
                   align="Left", font=("Ariel", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

    def play_sound(self):
        winsound.Beep(2000, 100)


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

# killer


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("triangle")
        self.color("black")
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 240 or self.xcor() < -240:
            self.left(60)
        if self.ycor() > 240 or self.ycor() < -240:
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
        self.color("yellow")
        self.shape("turtle")
        self.speed = 3
        self.goto(random.randint(-240, 240), random.randint(-240, 240))
        self.setheading(random.randint(0, 270))

    def jump(self):
        self.goto(random.randint(-240, 240), random.randint(-240, 240))
        self.setheading(random.randint(0, 270))

    def move(self):
        self.forward(self.speed)

        if self.xcor() > 240 or self.xcor() < -240:
            self.left(60)
        if self.ycor() > 240 or self.ycor() < -240:
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

border = Border()
pts = Pts()

border.border_dimen()

# multiple victims
dots = []
for i in range(6):
    dots.append(Dot())

# keyboard assignin
turtle.listen()
turtle.onkey(play.turnleft, "Left")
turtle.onkey(play.turnright, "Right")
turtle.onkey(play.acceleratespeed, "Up")
turtle.onkey(play.deceleratespeed, "Down")
turtle.onkey(play.pausespeed, "space")
#turtle.onkey(dot.pauses, "space")

sc.tracer(0)  # speed up the game


while True:
    sc.update()
    play.move()

    for dot in dots:
        dot.move()

        if collision(play, dot):
            dot.jump()
            pts.change_score(10)
            pts.play_sound()
