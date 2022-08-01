import turtle

# setting up the game window
window = turtle.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# main game loop
while True:
	# every time the loop runs it updates the screen
	window.update()
