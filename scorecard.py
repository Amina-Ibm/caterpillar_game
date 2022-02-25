from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.color("white")
        self.hideturtle()
        self.font = ("Verdana", 15, "normal")
        self.scoring()


    score_now = 0

    def scoring(self):
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score_now}", align='center', font=self.font)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=self.font)




