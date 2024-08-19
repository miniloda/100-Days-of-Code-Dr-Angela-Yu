from turtle import Turtle, Screen
import random

# Define available colors
colors = ['red', 'orange', 'yellow', 'green', 'blue']

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)
init_prompt = True
correct_input = False
user_bet = None
while correct_input is False:
    # Ask for user input
    if init_prompt is True:
        user_bet = screen.textinput("Make your bet", prompt="Enter a color: \n" + "\n".join(colors))
        init_prompt = False
    else:
        user_bet = screen.textinput("Make your bet", prompt="WRONG COLORS!\nEnter a color: \n" + "\n-".join(colors))
    # Exit loop if user cancels the input
    if user_bet is None:
        correct_input = True
        break

    # Check if input is valid
    if user_bet in colors:
        correct_input = True
race = False
# initialize turtles
turtles = []
y = 100
for color in colors:
    tim = Turtle(shape = "turtle")
    tim.color(color)
    tim.penup()
    tim.goto(-230, y)
    y -= 50
    turtles.append(tim)
if user_bet:
    race = True

while race:
    for turtle in turtles:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
    for turtle in turtles:
        print(turtle.color())
        if turtle.pos()[0] >= 200:
            if turtle.color()[0] == user_bet:
                screen.textinput(str(turtle.color()[0]) + " won","You win")
            else:
                screen.textinput(str(turtle.color()[0]) + " won", "You lost")
            race = False
# Keep the window open
screen.mainloop()
