import turtle
import termcolor2

star = turtle.Turtle()
collors = ["red","blue","yellow","cyan","green"]
turtle.bgcolor("black")


for x in range(5):
    star.right(75)
    star.forward(100) 
    star.pensize(3)
    for i in range(5): 
        star.right(144) 
        star.forward(100)
        star.pencolor(collors[x%5])
        star.speed(5)
    star.right(2)
    star.left(2)
        

turtle.done()
turtle.exitonclick()