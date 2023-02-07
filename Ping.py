import turtle

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=600, height=400)

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-250, 0)

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(250, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Function to move the left paddle up
def paddle_left_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

# Function to move the left paddle down
def paddle_left_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Function to move the right paddle up
def paddle_right_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

# Function to move the right paddle down
def paddle_right_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for a collision with the top or bottom wall
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Check for a collision with the left paddle
    if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.dx *= -1

    # Check for a collision with the right paddle
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
            ball.dx *= -1

    # Check for a point scored
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1

wn.mainloop()
