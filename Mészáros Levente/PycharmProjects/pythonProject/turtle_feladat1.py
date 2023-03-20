import turtle
import time

turtle.shape('turtle')

turtle.pen(pencolor='blue', fillcolor='yellow')



turtle.begin_fill()
y = 0
while y < 5:
    turtle.fd(100)
    turtle.lt(70)
    y += 1
turtle.end_fill()

time.sleep(4)