import turtle

def drawing(same_turtle,same_turtle):
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(7)
    for i in range(1,5):
        same_turtle.forward(100)
        same_turtle.left(90)

def draw_item():
    window=turtle.screen()
    window.bgcolor("grey")
    angie=turtle.Turtle()
    angie.shape("circle")
    angie.color("grey")
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    window.exitonclick()
drawing()
draw_item()
