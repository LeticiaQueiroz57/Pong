import turtle

window = turtle.Screen()
window.title("Pong by Leticia Queiroz")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Border
bd = turtle.Turtle()
bd.speed(0)
bd.color("white")
bd.shape("square")
bd.shapesize(stretch_wid=1, stretch_len=40)
bd.penup()
bd.goto(0, 290)

bd2 = turtle.Turtle()
bd2.speed(0)
bd2.color("white")
bd2.shape("square")
bd2.shapesize(stretch_wid=1, stretch_len=40)
bd2.penup()
bd2.goto(0, -285)

bd3 = turtle.Turtle()
bd3.speed(0)
bd3.color("white")
bd3.shape("square")
bd3.shapesize(stretch_wid=30, stretch_len=1)
bd3.penup()
bd3.goto(-390, 0)

bd4 = turtle.Turtle()
bd4.speed(0)
bd4.color("white")
bd4.shape("square")
bd4.shapesize(stretch_wid=30, stretch_len=1)
bd4.penup()
bd4.goto(385, 0)

# object 1
obj_1 = turtle.Turtle()
obj_1.speed(0)
obj_1.color("white")
obj_1.shape("square")
obj_1.shapesize(stretch_wid=5, stretch_len=1)
obj_1.penup()
obj_1.goto(-350, 0)


# object 2
obj_2 = turtle.Turtle()
obj_2.speed(0)
obj_2.color("white")
obj_2.shape("square")
obj_2.shapesize(stretch_wid=5, stretch_len=1)
obj_2.penup()
obj_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.shapesize(stretch_wid=1.3, stretch_len=1.3)
ball.penup()
ball.goto(0, 0)

ball_x = 0.5
ball_y = 0.5

# Functions - Objects movement


def obj1_up():
    y = obj_1.ycor()
    y += 20
    obj_1.sety(y)


def obj2_up():
    y = obj_2.ycor()
    y += 20
    obj_2.sety(y)


def obj1_down():
    y = obj_1.ycor()
    y -= 20
    obj_1.sety(y)


def obj2_down():
    y = obj_2.ycor()
    y -= 20
    obj_2.sety(y)


# Score
player_a = 0
player_b = 0
sc = turtle.Turtle()
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 250)
sc.write("0 X 0", align="center", font=("Courier", 20, "normal"))

# Keyboard Binding
window.listen()
window.onkeypress(obj1_up, "w")
window.onkeypress(obj1_down, "s")
window.onkeypress(obj2_up, "Up")
window.onkeypress(obj2_down, "Down")

while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball_x)
    ball.sety(ball.ycor() + ball_y)

    # Colision - Border
    if ball.ycor() > 280:
        ball.sety(280)
        ball_y *= -1

    if ball.ycor() < -270:
        ball.sety(-270)
        ball_y *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_x *= -1
        player_a += 1
        sc.clear()
        sc.write("{} X {}".format(player_a, player_b),
                 align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_x *= -1
        player_b += 1
        sc.clear()
        sc.write("{} X {}".format(player_a, player_b),
                 align="center", font=("Courier", 20, "normal"))

    # Colision - Objects
    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < obj_1.ycor()+50 and ball.ycor() > obj_1.ycor()-50):
        ball_x *= -1

    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < obj_2.ycor()+50 and ball.ycor() > obj_2.ycor()-50):
        ball_x *= -1
