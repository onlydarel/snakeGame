from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Default Start
snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")  

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
    
  #Detect collision
  if snake.head.distance(food) < 15:
    snake.eaten_food()
    food.refresh()
    scoreboard.increase_score()
  
  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
    scoreboard.reset_scoreboard()
    snake.reset()
  
  for parts in snake.square_list[1:]:
    if snake.head.distance(parts) < 10:
      scoreboard.reset_scoreboard()
      snake.reset()
    




































screen.exitonclick()