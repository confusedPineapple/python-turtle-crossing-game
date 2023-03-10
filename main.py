from turtle import Screen
from player import Player
from car_manager import CarManager
import sched, time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Avoid the Cars!!!')
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.up, 'Up')
car = CarManager()
scoreboard = Scoreboard()

timer = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    timer += 1
    if timer == 6:
        car.create()
        timer = 0
    car.move()

    #Detect collision with car
    for cars in car.all_cars:
        if player.distance(cars) < 30:
            scoreboard.game_over()
            game_is_on = False

    #Detect end of Level
    if player.ycor() > 300:
        player.goto(0, -280)
        car.increase_speed()
        scoreboard.update_level()




screen.exitonclick()

