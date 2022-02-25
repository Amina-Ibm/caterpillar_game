import time
from turtle import Screen

from snake import Snake
from food import Food
from scorecard import Score
from butterfly import CreateButterfly
from scorend import End
food = Food()
screen = Screen()
score = Score()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
eat_food = screen.textinput(title="food pills", prompt="How many food pills do you want the caterpillar to eat?")
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
food_limit = int(eat_food)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    score.scoring()
    snake.move()
    snake_pos = snake.head.pos()
    if snake.head.distance(food) < 20:
        food.reset_colour()
        food.reset_position()
        score.clear()
        score.score_now += 1
        snake.increase_size()
    if snake_pos[0] >= 295 or snake_pos[0] <= -295 or snake_pos[1] >= 295 or snake_pos[1] <= -295:
        game_is_on = False
        score.game_over()

    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    if score.score_now > food_limit:
        game_is_on = False
        end = End()
        end1 = End()
        end.endtext(food_limit)
        time.sleep(0.3)
        screen.update()
        screen.clear()
        end.ready()
        CreateButterfly()

screen.exitonclick()