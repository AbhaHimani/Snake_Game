from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial",20,"normal"))
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
    def increase_score(self):
        self.score= self.score+1
        self.clear()
        self.update_scoreboard()
    def Game_Over(self):
        self.goto(0,0)
        self.write(f"Game Over, your score is {self.score}", align="center", font=("Arial", 20, "normal"))





