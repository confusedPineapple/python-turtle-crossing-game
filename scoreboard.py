from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color('black')
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(-0, 250)
        self.write(f"Level: {self.level}", align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Courier', 80, 'normal'))
