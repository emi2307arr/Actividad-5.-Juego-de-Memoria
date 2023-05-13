from random import *
from turtle import *
from freegames import path
import string

car = path('car.gif')
tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e']
state = {'mark': None}
hide = [True] * 64
tap_count = 0
tap_display = Turtle(visible=False)
tap_display.penup()
tap_display.goto(150, 180)
tap_display.write("Taps: 0", font=('Arial', 16, 'normal'))

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global tap_count
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        tap_count += 1
        tap_display.clear()
        tap_display.write("Taps: " + str(tap_count), font=('Arial', 16, 'normal'))

    # Check if all tiles are uncovered
    if False not in hide:
        tap_display.goto(-80, 180)
        tap_display.write("You won!", font=('Arial', 16, 'normal'))

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Calcula el centro del cuadrado
        x += 25
        y += 25
        # Mueve la letra al centro de cada cuadrado
        goto(x, y - 12)  # Adjust the y-coordinate by subtracting 5
        color('black')
        # Escribe el número de fila en el código para el análisis
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

