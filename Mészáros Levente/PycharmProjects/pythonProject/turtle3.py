import turtle
import time
import random

colors = ['orange', 'black', 'red', 'yellow', 'blue', 'green']


turtle.title('William Dripfoe')
turtle.shape('turtle')

turtle.pen(pencolor=random.choice(colors), fillcolor='red', pensize=random.randint(0, 10))


turtle.begin_fill()
x = 0
while x < 4:
    turtle.fd(150)
    turtle.lt(90)
    x += 1
turtle.end_fill()


time.sleep(1)