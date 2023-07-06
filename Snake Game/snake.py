from turtle import Turtle, Screen

MOVE_DISTANCE = 20
STARTING_POS = [(0,0), (0, -20), (0, -40)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.square_list = []
    self.create_snake()
    self.head = self.square_list[0]
  
  def create_snake(self):
    for i in STARTING_POS:
      self.add_snake(i)
      
  def add_snake(self, position):    
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(position)
    self.square_list.append(new_square)
  
  def eaten_food(self):
    self.add_snake(self.square_list[-1].position())
  
  def reset(self):
    for block in self.square_list:
      block.goto(1000, 1000)
    self.square_list.clear()
    self.create_snake()
    self.head = self.square_list[0]
  
  def move(self):
    for sq_num in range(len(self.square_list)-1, 0, -1):
      new_x = self.square_list[sq_num - 1].xcor()
      new_y = self.square_list[sq_num - 1].ycor()
      self.square_list[sq_num].goto(new_x, new_y)
    self.head.fd(MOVE_DISTANCE)
  
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(90)
  
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(270)
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(180)
    
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(0)


