import turtle
import time
turtle.setup(starty=0, startx=0, width=1920, height=1080)
turtle.shape('turtle')
turtle.title('Teknőc rajzolás')

for i in range(2):
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

turtle.penup()
turtle.forward(200)
turtle.pendown()

for i in range(2):
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

time.sleep(2)