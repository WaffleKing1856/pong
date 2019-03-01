#Pong That Matt Made
#Howdy people that like looking at code
#bet you don't like looking at python, because no one does


import turtle
import winsound

wn = turtle.Screen()
wn.title("Matt's Epic Version Of Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


 #Left Paddle
l_paddle = turtle.Turtle()
l_paddle.speed(0)
l_paddle.shape("square")
l_paddle.color("white")
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.penup()
l_paddle.goto(-350, 0)


#Right Paddle
r_paddle = turtle.Turtle()
r_paddle.speed(0)
r_paddle.shape("square")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.penup()
r_paddle.goto(350, 0)

#Bouncy Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

#Score
score_l = 0
score_r = 0

# Pen?
pen = turtle.Turtle()
pen.speed(0)
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write(str(score_l) + "  " + str(score_r), align='center', font=("Courier", 40, "bold"))


#Functions that do funny things
def l_paddle_up():
    y = l_paddle.ycor()
    y += 20
    l_paddle.sety(y)


def l_paddle_down():
    y = l_paddle.ycor()
    y -= 20
    l_paddle.sety(y)


def r_paddle_up():
    y = r_paddle.ycor()
    y += 20
    r_paddle.sety(y)


def r_paddle_down():
    y = r_paddle.ycor()
    y -= 20
    r_paddle.sety(y)


#Keyboard Bindings
wn.listen()
wn.onkeypress(l_paddle_up, "w")
wn.onkeypress(l_paddle_down, "s")
wn.onkeypress(r_paddle_up, "Up")
wn.onkeypress(r_paddle_down, "Down")


#Main Game Loop
while True:
    wn.update()

    #Ball Movment
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border for Ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        score_l += 1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        score_r += 1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    #Ball Point Scorage
    if ball.xcor() > 390:
        winsound.PlaySound("insta grama.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write(str(score_l) + "  " + str(score_r), align='center', font=("Courier", 40, "bold"))

    if ball.xcor() < -390:
        winsound.PlaySound("insta grama.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write(str(score_l) + "  " + str(score_r), align='center', font=("Courier", 40, "bold"))

    #Paddle wackin dat ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < r_paddle.ycor() + 40 and ball.ycor() > r_paddle.ycor() -40):
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < l_paddle.ycor() + 40 and ball.ycor() > l_paddle.ycor() - 40):
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1



