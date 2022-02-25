from turtle import Turtle

coordinates = [(0, 0), (-20, 0), (-40, 0)]
distance = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.make_a_snake()
        self.head = self.segments[0]



    def make_a_snake(self):
        for position in coordinates:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("circle")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def increase_size(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_seg = self.segments[seg_num - 1]
            new_x = new_seg.xcor()
            new_y = new_seg.ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(distance)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)





