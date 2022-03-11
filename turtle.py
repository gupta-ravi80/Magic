import turtle
import colorsys
t = turtle.Turle()
s = turtle.Screen()
s.bgcolor('black')
t.speed (0)
n=80
h = 0
for i in range (70)
    c = colorsys.hsv_to_rbg(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(104)
    t.forward(i*3)
    for j in range(3):
        t.left(5)
        t.forward(i*2)
        t.left(52)
turtle.done()