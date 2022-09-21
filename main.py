from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake("red")
food = Food("blue", 0.75)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.title(f'Snake')
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food ===================================================================
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    
    # Detect collision with wall ===================================================================
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False
    
    # Detect collision with tail ===================================================================
    
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail ================================================
    # ====trigger game_over ========================================================================

screen.exitonclick()