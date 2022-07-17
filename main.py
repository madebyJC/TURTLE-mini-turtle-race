import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color "
                                                         "(red, orange, yellow, green, blue, purple): ").lower()
is_race_on = False

# (red, orange, yellow, green, blue, purple)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-225, y=y_positions[turtle_index])
    all_turtles.append(t)

if user_bet in colors:
    print(f"You chose the colour {user_bet}")
    is_race_on = True
else:
    print("Invalid Color! Please restart the game.")

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
