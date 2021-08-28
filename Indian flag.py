import turtle

t = turtle.Turtle()
t.pensize(4)
def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):

        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()



t.up()
t.speed(4)
t.goto(0,-300)
t.down()
t.goto(0,300)
rectangle('#FF9933')

t.goto(0, 200)
t.down()
t.forward(200)
t.color('#000088')
t.circle(-50)
t.right(90)
t.forward(50)
t.setheading(0)
for i in range(24):
    t.forward(45)
    t.bk(45)
    t.left(15)
t.setheading(90)
t.forward(50)
t.setheading(0)

t.color('black')
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.right(180)

t.up()
t.goto(0,100)
t.down()
rectangle('#128807')




sc = turtle.Screen()
sc.exitonclick()