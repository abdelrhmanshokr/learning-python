import turtle

# setting up the game window
window = turtle.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# pong game has 3 items 
# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation for this item
paddle_a.shape("square") # giving the item a shape
paddle_a.color("white") # giving the item a color
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # increasing the default 20*20 size
paddle_a.penup() # prevent the default behavior of drawing a line
paddle_a.goto(-350, 0) # an (x, y) coordinates for default starting position
paddle_a.score = 0

# paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation for this item
paddle_b.shape("square") # giving the item a shape
paddle_b.color("white") # giving the item a color
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # increasing the default 20*20 size
paddle_b.penup() # prevent the default behavior of drawing a line
paddle_b.goto(350, 0) # an (x, y) coordinates for default starting position
paddle_b.score = 0

# ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation for this item
ball.shape("square") # giving the item a shape
ball.color("white") # giving the item a color
ball.shapesize(stretch_wid=0.75, stretch_len=0.75) # increasing the default 20*20 size
ball.penup() # prevent the default behavior of drawing a line
ball.goto(0, 0) # an (x, y) coordinates for default starting position
ball.dx = 0.1 # delta in x direction
ball.dy = 0.1 # delta in y direction

# score an object called Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"PlayerA: {paddle_a.score}  PlayerB: {paddle_b.score}", align="center", font=("Courtier", 24, "normal"))


# function to control paddles
def paddle_a_up():
	y = paddle_a.ycor()
	if y < 250: 
		y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	if y > -250: 
		y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	if y < 250: 
		y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	if y > -250: 
		y -= 20
	paddle_b.sety(y)

# keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
	# every time the loop runs it updates the screen
	window.update()

	# move the ball 
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Y border checking up and down 
	if ball.ycor() > 290:
		ball.dy *= -1 # to reverse the direction
	if ball.ycor() < -290:
		ball.dy *= -1

	# X border checking right and left
	if ball.xcor() > 390:
		ball.setx(0)
		ball.sety(0)
		ball.dx *= -1
		paddle_a.score += 1
		pen.clear()
		pen.write(f"PlayerA: {paddle_a.score}  PlayerB: {paddle_b.score}", align="center", font=("Courtier", 24, "normal"))
	if ball.xcor() < -390:
		ball.setx(0)
		ball.sety(0)
		ball.dx *= -1
		paddle_b.score += 1
		pen.clear()
		pen.write(f"PlayerA: {paddle_a.score}  PlayerB: {paddle_b.score}", align="center", font=("Courtier", 24, "normal"))


	# detect collision with the right paddle (paddle_b)
	if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor() - 40 < ball.ycor() and ball.ycor() < paddle_b.ycor() + 40):
		ball.setx(340)
		ball.dx *= -1

	# detect collision with the left paddle (paddle_a)
	if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() - 40 < ball.ycor() and ball.ycor() < paddle_a.ycor() + 40):
		ball.setx(-340)
		ball.dx *= -1