# Create a heart with python and turtle library
from turtle import *
import turtle
turtle.hideturtle()
title('I Love You')
bgcolor('lightyellow')
color('red')
begin_fill()
pensize(10)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
up()
setpos(25,-25)
down()
turtle.write('i love you 😊🌷',
font=('Verdana',12,'bold'))
turtle.done()