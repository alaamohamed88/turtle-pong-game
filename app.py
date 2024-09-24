"""
Ping Pong Game using Turtle Graphics.

This is a simple two-player ping pong game where players use keyboard keys to control paddles. 
Player 1 controls the left paddle with the 'W' and 'S' keys, while Player 2 controls the right paddle 
with the 'Up' and 'Down' arrow keys. The ball bounces off the top and bottom walls, and the paddles. 
The first player to reach the maximum score (default is 11) wins the game. 

Key Features:
- Player 1: Controls left paddle ('W' to move up, 'S' to move down)
- Player 2: Controls right paddle ('Up' arrow to move up, 'Down' arrow to move down)
- Players earn points when the opponent misses the ball
- The game announces a winner when one player reaches the maximum score
"""

import turtle

# Set up the game window
window = turtle.Screen()
window.title("Ping Pong Game")  # Set the title of the window
window.bgcolor("black")         # Set the background color to black
window.setup(width=800, height=600)  # Set the dimensions of the window
window.tracer(0)                # Turn off automatic updates for smooth gameplay

# Paddle 1 (Left Paddle)
paddle1 = turtle.Turtle()
paddle1.speed(0)                # Set the drawing speed to the fastest
paddle1.color('blue')           # Set the paddle color to blue
paddle1.shape('square')         # Paddle is a square shape
paddle1.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle vertically
paddle1.penup()                 # Disable drawing trail
paddle1.goto(-350, 0)           # Place the paddle on the left side of the screen

# Paddle 2 (Right Paddle)
paddle2 = turtle.Turtle()
paddle2.speed(0)                # Set the drawing speed to the fastest
paddle2.color('red')            # Set the paddle color to red
paddle2.shape('square')         # Paddle is a square shape
paddle2.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle vertically
paddle2.penup()                 # Disable drawing trail
paddle2.goto(350, 0)            # Place the paddle on the right side of the screen

# Ball
ball = turtle.Turtle()
ball.speed(0)                   # Set the drawing speed to the fastest
ball.color('white')             # Set ball color to white
ball.shape('square')            # Ball is a square shape
ball.penup()                    # Disable drawing trail
ball.goto(0, 0)                 # Start ball in the center
ball.dx = ball.dy = 0.1         # Set ball movement increments for x and y axes

# Display welcome message and instructions
print('#' * 100)
print(' Welcome To Ping Pong Game '.center(100, '#'))
print('#' * 100)
print('For Player 1: Press "W" to move your paddle upwards, "S" to move your paddle downwards')
print('#' * 100)
print('For Player 2: Press "Up" arrow to move your paddle upwards, "Down" arrow to move your paddle downwards')
print('#' * 100)
print('The first to reach 11 points wins!')
print('#' * 100)

# Player names input
player1_name = input('Player 1, please enter your name: ')
player2_name = input('Player 2, please enter your name: ')

# Set maximum score to win
max_score = 11
score1 = score2 = 0  # Initialize both players' scores

# Score display setup
score = turtle.Turtle()
score.speed(0)
score.color('white')            # Set score color to white
score.penup()                   # Disable drawing trail
score.hideturtle()              # Hide turtle to only show text
score.goto(0, 250)              # Set position of the score display
score.write(f'{player1_name}: {score1}\t\t   {player2_name}: {score2}', align='center', font=('Arial', 24, 'normal'))

pen = turtle.Turtle() # Create a turtle object for displaying text on the screen
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()    # Hide the turtle to only show text

# Function to move paddle 1 up
def paddle1_moveup():
    y_paddle1 = paddle1.ycor()  # Get current y-coordinate of paddle 1
    y_paddle1 += 20             # Move the paddle up by 20 units
    paddle1.sety(y_paddle1)     # Set the new y-coordinate of paddle 1

# Function to move paddle 1 down
def paddle1_movedown():
    y_paddle1 = paddle1.ycor()  # Get current y-coordinate of paddle 1
    y_paddle1 -= 20             # Move the paddle down by 20 units
    paddle1.sety(y_paddle1)     # Set the new y-coordinate of paddle 1

# Function to move paddle 2 up
def paddle2_moveup():
    y_paddle2 = paddle2.ycor()  # Get current y-coordinate of paddle 2
    y_paddle2 += 20             # Move the paddle up by 20 units
    paddle2.sety(y_paddle2)     # Set the new y-coordinate of paddle 2

# Function to move paddle 2 down
def paddle2_movedown():
    y_paddle2 = paddle2.ycor()  # Get current y-coordinate of paddle 2
    y_paddle2 -= 20             # Move the paddle down by 20 units
    paddle2.sety(y_paddle2)     # Set the new y-coordinate of paddle 2

# Keyboard bindings to control paddles
window.listen()  # Listen for keyboard input
window.onkeypress(paddle1_moveup, 'w')  # Move paddle 1 up when 'w' is pressed
window.onkeypress(paddle1_movedown, 's')  # Move paddle 1 down when 's' is pressed
window.onkeypress(paddle2_moveup, 'Up')  # Move paddle 2 up when 'Up' arrow is pressed
window.onkeypress(paddle2_movedown, 'Down')  # Move paddle 2 down when 'Down' arrow is pressed

# Game loop
while True:
    window.update()  # Refresh the screen with any changes

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Update ball's x-coordinate
    ball.sety(ball.ycor() + ball.dy)  # Update ball's y-coordinate

    # Ball collision with top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse y direction

    # Ball collision with bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reverse y direction

    # Paddle 1 collision with top border
    if paddle1.ycor() >= 250:
        paddle1.sety(250)

    # Paddle 2 collision with top border
    if paddle2.ycor() >= 250:
        paddle2.sety(250)

    # Paddle 1 collision with bottom border
    if paddle1.ycor() <= -250:
        paddle1.sety(-250)

    # Paddle 2 collision with bottom border
    if paddle2.ycor() <= -250:
        paddle2.sety(-250)

    # Player 1 scores if ball passes paddle 2
    if ball.xcor() > 390:
        paddle1.goto(-350, 0)
        paddle2.goto(350, 0)
        ball.goto(0, 0)       # Reset ball position
        ball.dx *= -1         # Reverse x direction
        score1 += 1           # Increment player 1's score
        score.clear()         # Clear the previous score display
        score.write(f'{player1_name}: {score1}\t\t   {player2_name}: {score2}', align='center', font=('Arial', 24, 'normal'))

    # Player 2 scores if ball passes paddle 1
    if ball.xcor() < -390:
        paddle1.goto(-350, 0)
        paddle2.goto(350, 0)
        ball.goto(0, 0)       # Reset ball position
        ball.dx *= -1         # Reverse x direction
        score2 += 1           # Increment player 2's score
        score.clear()         # Clear the previous score display
        score.write(f'{player1_name}: {score1}\t\t   {player2_name}: {score2}', align='center', font=('Arial', 24, 'normal'))

    # Ball collision with paddle 2
    if (340 < ball.xcor() < 345) and (paddle2.ycor() - 40 < ball.ycor() < paddle2.ycor() + 40):
        ball.setx(340)
        ball.dx *= -1  # Reverse x direction

    # Ball collision with paddle 1
    if (-345 < ball.xcor() < -340) and (paddle1.ycor() - 40 < ball.ycor() < paddle1.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1  # Reverse x direction

    # Check if Player 1 wins
    if score1 == max_score:
        window.setup(width=800, height=400)  # Adjust window size for winner message
        paddle1.hideturtle()  # Hide paddles and ball
        paddle2.hideturtle()
        ball.hideturtle()
        pen.goto(0, 0)  # Position the message in the center
        pen.write(f'Congratulations, {player1_name}. You Win!', align='center', font=('jokerman', 24, 'normal'))

    # Check if Player 2 wins
    elif score2 == max_score:
        window.setup(width=800, height=400)  # Adjust window size for winner message
        paddle1.hideturtle()  # Hide paddles and ball
        paddle2.hideturtle()
        ball.hideturtle()
        pen.goto(0, 0)  # Position the message in the center
        pen.write(f'Congratulations, {player2_name}. You Win!', align='center', font=('jokerman', 24, 'normal'))
