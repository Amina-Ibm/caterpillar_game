from turtle import Turtle, Screen
t = Turtle()
screen = Screen()
t.speed(0)
screen.bgcolor("black")
t.right(90)
t.hideturtle()
class CreateButterfly(Turtle):
    def __init__(self):
        super(CreateButterfly, self).__init__()
        self.speed(0)
        screen.bgcolor("black")
        self.right(90)
        self.hideturtle()
        self.make_butterfly()


    def make_butterfly(self):

        #1st
        for i in range(100):
            t.color("hotpink")
            t.left(90)
            t.circle(i * 2, 180)
        t.penup()
        t.home()
        t.pendown()

        #2nd
        for j in range(80):
            t.color("yellow")
            t.left(90)
            t.circle(j * 2, 180)
        t.penup()
        t.home()
        t.pendown()

        #3rd
        for k in range(60):
            t.color("red")
            t.left(90)
            t.circle(k * 2, 180)
        t.penup()
        t.home()
        t.pendown()
        #4th
        for l in range(40):
            t.color("royalblue")
            t.left(90)
            t.circle(l * 2, 180)
        t.penup()
        t.home()
        t.pendown()
        #5th
        for m in range(20):
            t.color("white")
            t.left(90)
            t.circle(m * 2, 180)
        t.penup()
        t.home()
        t.pendown()

        screen.exitonclick()

