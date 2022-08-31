import turtle
window = turtle.Screen()
window.setup(800,600)
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(-300,200)
line.pendown()
line.right(90)
line.forward(400)
line.penup()
line.goto(300,200)
line.pendown()
line.forward(400)
steps=0
turtle2 = turtle.Turtle()
turtle2.shape("turtle")
while steps <= 2000:
    steps += 1
    if turtle2.position()[0] >= 300: # Check if turtle reached the right line
        turtle2.right(180) # Reverse turtle by 180
    elif turtle2.position()[0] <= -300: # Check if turtle reached the left line
        turtle2.right(180) # Reverse turtle by 180
    turtle2.forward(1) # Move turtle by 1 step each time
turtle.exitonclick()
