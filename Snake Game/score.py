from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.start = 0
    with open('highscore.txt', mode='r') as file:
        self.highscore = int(file.read())
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.write(f"Score: {self.start}", align=ALIGNMENT, font=FONT)
    self.hideturtle()
    self.check_score()
  
  def check_score(self): 
    self.clear()
    self.write(f"Score: {self.start} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
  
  def reset_scoreboard(self):
    if self.start > self.highscore:
      self.highscore = self.start
      with open('highscore.txt', mode='w') as file:
        file.write(str(self.highscore))
    self.start = 0
    self.check_score()
  
  def increase_score(self):
    self.start += 1
    self.check_score()