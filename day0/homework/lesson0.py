from turtle import *


#we want to paint a house

#step 1: draw a square
shape("turtle")
speed(10)
width(7)
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing of door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("green")
begin_fill()
penup()
goto(0, 160)
pendown()
left(120)
forward(50)
right(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
end_fill()

penup()
goto(200, 200)
pendown()
left(180)

color("green")
begin_fill()
penup()
goto(200, 160)
pendown()
forward(80)
right(90)
forward(50)
right(90)
forward(80)
right(90)
forward(50)
end_fill()



exitonclick()