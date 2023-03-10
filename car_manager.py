from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5




class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_increment = 10


    def create(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        new_car.penup()
        random_y = random.randint(-250,250)
        new_car.goto(-300, random_y)
        self.all_cars.append(new_car)



    def move(self):
        for car in self.all_cars:
            x = car.xcor() + self.move_increment
            car.goto(x,car.ycor())

    def increase_speed(self):
        self.move_increment += 5
