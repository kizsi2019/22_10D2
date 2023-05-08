
szam = int(input('Hány oldalas szöget rajzoljak?!'))
szin = input('Add meg a tollszínt!(angolul)')
toll_vastagsag = int(input('Add meg a tollvastagságot!(számmal)'))
szin2 = input('Add meg a kitöltési színt!(angolul)')
ablak1 = int(input('add meg az ablak szélességét!(számmal)'))
ablak2 = int(input('add meg az ablak magasságát!(számmal)'))
szin3 = input('Add meg az ablak háttérszínét!(angolul)')
position = int(input('add meg a teknőc kezdő pozícióját(számmal,x érték)'))
position2 = int(input('add meg a teknőc kezdő pozícióját(számmal,y érték)'))





import turtle
import time

turtle.title('Turtle grafikai felület')
turtle.shape('turtle')
turtle.setup(width=ablak1, height=ablak2, startx=position, starty=position2)
turtle.screensize(bg=szin3)
turtle.pen(pencolor=szin, pensize=toll_vastagsag, fillcolor=szin2)

turtle.begin_fill()
szog = 360
for i in range(szam):
    turtle.forward(100)
    turtle.left(szog/szam)
turtle.end_fill()


time.sleep(2)