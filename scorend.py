from turtle import Turtle
import time



class End(Turtle):
    def __init__(self):
        super(End, self).__init__()
        self.color("white")
        self.hideturtle()
        self.font = ("Verdana", 14, "normal")



    def endtext(self, food_limit):
        self.penup()
        self.goto(0, 0)
        self.write(f"The caterpillar ate {food_limit} food pills and is now cocooning...", align='center', font=self.font)
        time.sleep(1)

    def ready(self):
        self.penup()
        self.goto(0, 260)
        self.write("The butterfly came out of the cocoon!!!", align='center', font=self.font)
        time.sleep(0.3)
