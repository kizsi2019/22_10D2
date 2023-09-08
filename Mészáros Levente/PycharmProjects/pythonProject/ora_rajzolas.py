import turtle
import keyboard  # szükséges telepíteni a keyboard modult

def on_press(key):
    if key.name == '':
        turtle.bye()

turtle.listen()  # Turtle modul figyeli a billentyűeseményeket
keyboard.on_press(on_press)  # keyboard modul figyeli a billentyűnyomásokat

turtle.mainloop()  # futtatja a Turtle programot
