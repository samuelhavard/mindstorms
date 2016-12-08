import turtle

window = turtle.Screen()
window.bgcolor("red")


def draw_square(angle):
    brad = turtle.Turtle()
    brad.right(angle * 10)
    for x in range(1, 4):
        brad.forward(100)
        brad.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.circle(100)


def draw_triangle():
    bert = turtle.Turtle()
    for x in xrange(2):
        bert.right(90)
        bert.forward(100)
    bert.home()

for x in range(0, 36):
    draw_square(x)

# draw_circle()
# draw_triangle()
window.exitonclick()