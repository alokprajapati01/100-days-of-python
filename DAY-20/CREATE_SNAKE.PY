from  turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVEMENT_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for sug_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[sug_num - 1].xcor()
            new_y = self.segments[sug_num - 1].ycor()
            self.segments[sug_num].goto(new_x, new_y)
        self.head.forward(MOVEMENT_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

