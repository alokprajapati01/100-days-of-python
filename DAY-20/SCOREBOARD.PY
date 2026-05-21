from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class GameScore(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
      #THIS IS A GAMEOVER FUNCTIN 
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
