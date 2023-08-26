import turtle

wn = turtle.Screen()
wn.title("Pizza Clicker")
wn.bgcolor("black")

wn.register_shape("pizza.gif")

pizza = turtle.Turtle()
pizza.shape("pizza.gif")
pizza.speed(0) #center of screen

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup
pen.goto(0, 300)
pen.write(f"Clicks: {clicks}", align ="center", font=("Courier New", 32, "normal"))

def clicker(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align ="center", font=("Courier New", 32, "normal"))

pizza.onclick(clicker)

wn.mainloop()

