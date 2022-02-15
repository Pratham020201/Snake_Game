from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move=20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self , position):
            new_segment = Turtle()
            new_segment.color("white")
            new_segment.penup()
            new_segment.shape("square")
            new_segment.goto(position)
            self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    # snake.move() will enable it to move forward continously
    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            x = self.segments[segnum - 1].xcor()
            y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(x, y)
        self.segments[0].forward(move)

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)


