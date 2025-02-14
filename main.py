from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(100)



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.exitonclick()