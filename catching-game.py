#imports

import turtle

import time

import random

import sys


# variables to store the number of apples caught and missed 

caught = 0

miss = 0 


#screen

win = turtle.Screen()

win.bgcolor("blue")

#width and height of the screen 
win.setup(1000,600)


#creating the turtle for basket

basket = turtle.Turtle()

basket.shape("square")

basket.penup()

basket.shapesize(2,13)

basket.color("dark green")

basket.hideturtle()

basket.goto(0,-250)

basket.showturtle()


#turtle for text

pen = turtle.Turtle()

pen.color("red")

pen.penup()

pen.hideturtle()

pen.goto(0 , 200)

pen.speed(0)

pen.pensize(6)


#functions to move basket left and right

def lt():

    basket.backward(20)


def rt():

    basket.forward(20)

#check if the basket touched the left border and right of the screen
def block():

    if (basket.xcor() <= -250):

        basket.setx(-250)


def rblock():

    if (basket.xcor() >= 250):

        basket.setx(250)


#Keys to move the basket

win.listen()


win.onkeypress(lt , "a")

win.onkeypress(rt , "d")



#game loop

while True:

    block()

    rblock()

    posx = (random.randint(-220,220))

    apple = turtle.Turtle()

    apple.rt(90)

    apple.penup()

    apple.color("red")

    apple.shape("circle")

    apple.shapesize(2)

    apple.hideturtle()

    apple.goto(posx , 250)

    apple.showturtle()

    apple.fd(500)

#check the collision
    if(apple.xcor() > basket.xcor() - 130 and apple.xcor() < basket.xcor() + 130 and apple.ycor() < basket.ycor() + 20 and apple.ycor() > basket.ycor() - 20):

        caught += 1

        pen.undo()

        pen.write("SCORE: " + str(caught) + " " + " MISSED: " + str(miss)  , align = "center" , font = ("Arial" , 24 , "bold"))

        apple.hideturtle()

    else:

        miss += 1

        apple.hideturtle()

        pen.undo()

        pen.write("SCORE: " + str(caught) + " " + " MISSED: " + str(miss)  , align = "center" , font = ("Arial" , 24 , "bold"))

        if (miss == 5):

            pen.undo()

            pen.write("GAME OVER", align = "center" , font = ("Arial" , 24 , "bold"))

            break

            sys.exit(3)

