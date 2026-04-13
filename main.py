from  turtle import Turtle , Screen
import  random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet",prompt="which turtle win the race ?, Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20 , 50 , 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x= -230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You won the race ! {wining_color}")
            else:
                print(f"You lost the race ! {wining_color} is winning !")


        rendom_distane = random.randint(0, 10)
        turtle.forward(rendom_distane)

screen.exitonclick()
