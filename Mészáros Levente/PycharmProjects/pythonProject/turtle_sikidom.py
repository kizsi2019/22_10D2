oldal = int(input('Hány oldalas szöget rajzöljak? '))

import turtle
import time

turtle.shape('turtle')
turtle.title('Síkidom rajzoló')
turtle.setup(width=1366, height=768, starty=0, startx=0)

for i in range(oldal):
    turtle.forward(100)
    turtle.left(360/oldal)

time.sleep(2)