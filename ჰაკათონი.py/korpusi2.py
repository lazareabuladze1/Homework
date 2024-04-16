from turtle import *

#we want to paint a house

#step l:  drow a sgu
speed(12)
width(7)

begin_fill()

color("gray")

left(90)
forward(280)
right(90)
forward(225)
right(90)
forward(280)
right(90)
forward(225)

end_fill()

begin_fill()

color("green")

forward(324)
left(90)
forward(263)
left(90)
forward(633)
left(90)
forward(263)
left(90)
forward(500)

end_fill()

goto(0,0)

penup()

color("black")

right(90)
forward(90)
right(90)

pendown()

forward(225)

penup()

left(90)
forward(80)

pendown()

left(90)







































exitonclick()