# Turtle design
from turtle import *
from colorsys import *
setposition(50,-50)
speed(0)
bgcolor('white')
pensize(1)
n=100
r=0
for i in range(150):
    for i in range(3):
        color(hsv_to_rgb(r,1,1))
        r+=0.0
        circle(40+i*5,90)
        forward(90)
        left(90)
    rt(9)
    hideturtle()
done()

