import turtle
import time

turtle.screensize(canvwidth=1900, canvheight=1080)
turtle.shape('turtle')
turtle.title('ez egy elbaszott kör')

circle = 200
for i in range(20):
    circle -= 10
    turtle.circle(circle)


time.sleep(2)