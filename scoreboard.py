from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 14, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        # self.life=3
        # self.high_score=0
        self.goto(0,260)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_scoreboard()
        # self.lives()

        # self.write(f"Score :{self.score}",align="center",font=("Arial", 24, "normal"))

    def update_scoreboard(self):
        self.clear()
        with open("Data.txt") as file:
            contents = file.read()
        self.write(f"Score : {self.score}" f"  High Score : {contents}", align=ALIGNMENT, font=FONT)

    # def lives(self):
    #     self.goto(-100,260)
    #     self.write(f"Life left : {self.life}",align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 25, "normal"))

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

        # self.write(f"Score :{self.score}",align="center",font=("Arial", 24, "normal"))

    # def endgame(self):
    #     # self.clear()
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
    def reset_score(self):
        with open("Data.txt") as file:
            contents=file.read()
            if self.score>int(contents):
                with open("Data.txt",mode='w') as file:
                    file.write(f"{self.score}")

            # self.high_score=self.score
        self.score=0
        self.update_scoreboard()




